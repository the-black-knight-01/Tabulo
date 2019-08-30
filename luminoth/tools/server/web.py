import click
import tensorflow as tf

from flask import Flask, jsonify, request, render_template
from threading import Thread
from PIL import Image
from six.moves import _thread

from luminoth.tools.checkpoint import get_checkpoint_config
from luminoth.utils.config import get_config, override_config_params
from luminoth.utils.predicting import PredictorNetwork
from luminoth.vis import vis_objects
import cv2 
from pytesseract import image_to_string


app = Flask(__name__)
import numpy as np


def get_image():
    image = request.files.get('image')
    if not image:
        raise ValueError
    basewidth = 300
    #wpercent = (basewidth/float(Image.open(image.stream).size[0]))
    #hsize = int((float(Image.open(image.stream).size[1])*float(wpercent)))
    img = Image.open(image.stream).convert('RGB')
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b = cv2.distanceTransform(img, distanceType=cv2.DIST_L2, maskSize=5)
    g = cv2.distanceTransform(img, distanceType=cv2.DIST_L1, maskSize=5)
    r = cv2.distanceTransform(img, distanceType=cv2.DIST_C, maskSize=5)
    
    # merge the transformed channels back to an image
    transformed_image = cv2.merge((b, g, r))
    
    return transformed_image


@app.route('/')
def index():
    return render_template('index.html')

import json
@app.route('/api/<model_name>/predict/', methods=['GET', 'POST'])
def predict(model_name):
    print ("preditct")
    if request.method == 'GET':
        return jsonify(error='Use POST method to send image.'), 400

    try:
        image_array = get_image()
    except ValueError:
        return jsonify(error='Missing image'), 400
    except OSError:
        return jsonify(error='Incompatible file type'), 400

    total_predictions = request.args.get('total')
    if total_predictions is not None:
        try:
            total_predictions = int(total_predictions)
        except ValueError:
            total_predictions = None

    # Wait for the model to finish loading.
    NETWORK_START_THREAD.join()

    objects = PREDICTOR_NETWORK.predict_image(image_array)
    image = request.files.get('image')
    if not image:
        raise ValueError

    img = Image.open(image.stream).convert('RGB')
    #vis_objects(np.array(image_array), objects).save("c:\\temp\\data.png")
    vis_objects(np.array(img), objects).save("c:\\temp\\data.png")
    global ouputObjects
    ouputObjects = objects
    objects = objects[:total_predictions]

    return jsonify({'objects': objects})

@app.route('/api/<model_name>/extract/', methods=['GET', 'POST'])
def extract(model_name):
    print ("extract")
    if request.method == 'GET':
        return jsonify(error='Use POST method to send image.'), 400

    #total_predictions = request.args.get('total')

    # Wait for the model to finish loading.

    image = request.files.get('image')
    thres = request.values.get("th")

    img = Image.open(image.stream).convert('RGB')
    #vis_objects(np.array(image_array), objects).save("c:\\temp\\data.png")
    s = ""
    for obj in ouputObjects:
        if (obj['prob'] > (int(thres)/100)):
            coordinates = obj['bbox']
            print (coordinates)
            width, height = img.size
            print (height, width)
            width_percentage = (coordinates[2]-coordinates[0])/width*100
            if width_percentage >= 70:
                coordinates[0] = 0
                coordinates[2] = width
            coordinates[1] = coordinates[1] - 15
            coordinates[3] = coordinates[3] + 10
            print (width_percentage)
            print (coordinates)
            cropped = img.crop( ( coordinates[0], coordinates[1], coordinates[2], coordinates[3] ) ) 
            file = "c:\\temp\\" +str(obj['prob']) +".jpg"
            cropped.save(file)
            #print (file)
            print (image_to_string(Image.open(file)))
            # Define config parameters.
            # '-l eng'  for using the English language
            # '--oem 1' for using LSTM OCR Engine
            config = ('-l eng --oem 1 --psm 6')
            s +=  image_to_string(Image.open(file).convert('LA'),config=config)
            #print (s)
    return s

    
def start_network(config):
    global PREDICTOR_NETWORK
    try:
        PREDICTOR_NETWORK = PredictorNetwork(config)
    except Exception as e:
        # An error occurred loading the model; interrupt the whole server.
        tf.logging.error(e)
        _thread.interrupt_main()


@click.command(help='Start basic web application.')
@click.option('config_files', '--config', '-c', multiple=True, help='Config to use.')  # noqa
@click.option('--checkpoint', help='Checkpoint to use.')
@click.option('override_params', '--override', '-o', multiple=True, help='Override model config params.')  # noqa
@click.option('--host', default='127.0.0.1', help='Hostname to listen on. Set this to "0.0.0.0" to have the server available externally.')  # noqa
@click.option('--port', default=5000, help='Port to listen to.')
@click.option('--debug', is_flag=True, help='Set debug level logging.')
def web(config_files, checkpoint, override_params, host, port, debug):
    if debug:
        tf.logging.set_verbosity(tf.logging.DEBUG)
    else:
        tf.logging.set_verbosity(tf.logging.INFO)

    if checkpoint:
        config = get_checkpoint_config(checkpoint)
    elif config_files:
        config = get_config(config_files)
    else:
        click.echo(
            'Neither checkpoint not config specified, assuming `accurate`.'
        )
        config = get_checkpoint_config('accurate')

    if override_params:
        config = override_config_params(config, override_params)

    # Bounding boxes will be filtered by frontend (using slider), so we set a
    # low threshold.
    if config.model.type == 'fasterrcnn':
        config.model.rcnn.proposals.min_prob_threshold = 0.01
    elif config.model.type == 'ssd':
        config.model.proposals.min_prob_threshold = 0.01
    else:
        raise ValueError(
            "Model type '{}' not supported".format(config.model.type)
        )

    # Initialize model
    global NETWORK_START_THREAD
    NETWORK_START_THREAD = Thread(target=start_network, args=(config,))
    NETWORK_START_THREAD.start()

    app.run(host=host, port=port, debug=debug)
