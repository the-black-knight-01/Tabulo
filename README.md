[![Tabulo](https://github.com/interviewBubble/Tabulo/raw/master/docs/images/Tabulo_logo.png)](https://github.com/interviewBubble/Tabulo)

---

[![Build Status](https://travis-ci.org/tryolabs/luminoth.svg?branch=master)](https://travis-ci.org/tryolabs/luminoth)
[![Documentation Status](https://readthedocs.org/projects/luminoth/badge/?version=latest)](http://luminoth.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/tryolabs/luminoth/branch/master/graph/badge.svg)](https://codecov.io/gh/tryolabs/luminoth)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Tabulo is an open source toolkit for **computer vision**. Currently, we support table detection, but we are aiming for much more. It is built in Python, using [Luminoth](https://github.com/tryolabs/luminoth), [TensorFlow](https://www.tensorflow.org/) and [Sonnet](https://github.com/deepmind/sonnet).

## 1. Installation

Tabulo currently supports Python 2.7 and 3.4–3.6.

### 1.1 Pre-requisites

To use Tabulo, [TensorFlow](https://www.tensorflow.org/install/) must be installed beforehand. If you want **GPU support**, you should install the GPU version of TensorFlow with `pip install tensorflow-gpu`, or else you can use the CPU version using `pip install tensorflow`.



### 1.2 Installing Tabulo

First, clone the repo on your machine and then install with `pip`:

```bash
git clone https://github.com/interviewBubble/Tabulo.git
cd tabulo
pip install -e .
```


### 1.3 Check that the installation worked

Simply run `tabulo --help`.

## 2. Avaiable API's
* localhost:5000/api/fasterrcnn/predict/   - To detect table in the image
* localhost:5000/api/fasterrcnn/extract/   - Extract table content from detected tables

## 3. Runnning Tabulo

### 3.1 Running Tabulo as Web Server:
![Running Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/tabulo_server.png)

### 3.2 Example of Table Detection with Faster R-CNN By Tabulo:
![Example of Table Detection with Faster R-CNN By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_detect.png)

### 3.3 Example of Table Data Extraction with tesseract By Tabulo:
![Example of Table Data Extraction with tesseract By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_data_extract.png)

## 4. Runnning Tabulo As Service:

### 4.1 Using Curl command
```Curl command to detect tabel
curl -X POST \
  http://localhost:5000/api/fasterrcnn/predict/ \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 70478bd2-e1e8-442f-b0bf-ea5ecf7bf4d8' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F image=@/path/to/image/page_8-min.jpg
``` 
#### 4.2 With PostMan
![Table Detection using Postman](https://github.com/interviewBubble/Tabulo/raw/master/docs/images/table_detect_API.png)

## 5. Supported models

Currently, we support the following models:

* **Object Detection**
  * [Faster R-CNN](https://arxiv.org/abs/1506.01497)
  * [SSD](https://arxiv.org/abs/1512.02325)

We also provide **pre-trained checkpoints** for the above models trained on popular datasets such as [COCO](http://cocodataset.org/) and [Pascal](http://host.robots.ox.ac.uk/pascal/VOC/).

## 6. Usage

There is one main command line interface which you can use with the `tabulo` command. Whenever you are confused on how you are supposed to do something just type:

`tabulo --help` or `tabulo <subcommand> --help`

and a list of available options with descriptions will show up.

## 7. Working with pretrained Models:
* DOWNLOAD pretrained model from [Google drive](https://drive.google.com/drive/folders/1aUh9RfGn2XGgG2EtpKFh7P6PmcC3Q48z?usp=sharing)
* Unzip and Copy downloaded luminoth folder inside luminoth/utils/pretrained_models folder

## 8. Working with datasets

See [Adapting a dataset](http://luminoth.readthedocs.io/en/latest/usage/dataset.html).

## 9. Training

See [Training your own model](https://github.com/interviewBubble/Table-Detection-using-Deep-Learning) to learn how to train locally or in Google Cloud.

Released under the [BSD 3-Clause](LICENSE).

--------------
# References
* https://github.com/Sargunan/Table-Detection-using-Deep-learning
* https://github.com/tryolabs/luminoth
