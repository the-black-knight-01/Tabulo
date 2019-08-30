[![Tabulo](https://github.com/interviewBubble/Tabulo/raw/master/docs/images/Tabulo_logo.png)](https://github.com/interviewBubble/Tabulo)

---

[![Build Status](https://travis-ci.org/tryolabs/luminoth.svg?branch=master)](https://travis-ci.org/tryolabs/luminoth)
[![Documentation Status](https://readthedocs.org/projects/luminoth/badge/?version=latest)](http://luminoth.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/tryolabs/luminoth/branch/master/graph/badge.svg)](https://codecov.io/gh/tryolabs/luminoth)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Tabulo is an open source toolkit for **computer vision**. Currently, we support table detection, but we are aiming for much more. It is built in Python, using [Luminoth](https://github.com/tryolabs/luminoth), [TensorFlow](https://www.tensorflow.org/) and [Sonnet](https://github.com/deepmind/sonnet).

## 1. Installation

Tabulo currently supports Python 2.7 and 3.4–3.6.

#### 1.1 Pre-requisites

To use Tabulo, [TensorFlow](https://www.tensorflow.org/install/) must be installed beforehand. If you want **GPU support**, you should install the GPU version of TensorFlow with `pip install tensorflow-gpu`, or else you can use the CPU version using `pip install tensorflow`.



#### 1.2 Installing Tabulo

First, clone the repo on your machine and then install with `pip`:

```bash
git clone https://github.com/interviewBubble/Tabulo.git
cd tabulo
pip install -e .
```


#### 1.3 Check that the installation worked

Simply run `tabulo --help`.

## 2. Runnning Tabulo

#### 2.1 Running Tabulo as Web Server
![Running Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/tabulo_server.png)

#### 2.2 Example of Table Detection with Faster R-CNN By Tabulo
![Example of Table Detection with Faster R-CNN By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_detect.png)

#### 2.3 Example of Table Data Extraction with tesseract By Tabulo
![Example of Table Data Extraction with tesseract By Tabulo](https://github.com/interviewBubble/Tabulo/blob/master/docs/images/table_data_extract.png)



## 3. Supported models

Currently, we support the following models:

* **Object Detection**
  * [Faster R-CNN](https://arxiv.org/abs/1506.01497)
  * [SSD](https://arxiv.org/abs/1512.02325)

We also provide **pre-trained checkpoints** for the above models trained on popular datasets such as [COCO](http://cocodataset.org/) and [Pascal](http://host.robots.ox.ac.uk/pascal/VOC/).

## 4. Usage

There is one main command line interface which you can use with the `lumi` command. Whenever you are confused on how you are supposed to do something just type:

`tabulo --help` or `tabulo <subcommand> --help`

and a list of available options with descriptions will show up.

## 5. Working with datasets

See [Adapting a dataset](http://luminoth.readthedocs.io/en/latest/usage/dataset.html).

## 6. Training

See [Training your own model](https://github.com/interviewBubble/Table-Detection-using-Deep-Learning) to learn how to train locally or in Google Cloud.

Released under the [BSD 3-Clause](LICENSE).
