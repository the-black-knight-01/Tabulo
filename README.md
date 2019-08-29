[![Luminoth](https://user-images.githubusercontent.com/270983/31414425-c12314d2-ae15-11e7-8cc9-42d330b03310.png)](https://luminoth.ai)

---

[![Build Status](https://travis-ci.org/tryolabs/luminoth.svg?branch=master)](https://travis-ci.org/tryolabs/luminoth)
[![Documentation Status](https://readthedocs.org/projects/luminoth/badge/?version=latest)](http://luminoth.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/tryolabs/luminoth/branch/master/graph/badge.svg)](https://codecov.io/gh/tryolabs/luminoth)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Tabulo is an open source toolkit for **computer vision**. Currently, we support table detection, but we are aiming for much more. It is built in Python, using [Luminoth](https://github.com/tryolabs/luminoth), [TensorFlow](https://www.tensorflow.org/) and [Sonnet](https://github.com/deepmind/sonnet).

Read the full documentation [here](http://luminoth.readthedocs.io/).

![Example of Object Detection with Faster R-CNN](https://user-images.githubusercontent.com/1590959/36434494-e509be42-163d-11e8-99c1-d1aa728929ec.jpg)

> **DISCLAIMER**: Luminoth is still alpha-quality release, which means the internal and external interfaces (such as command line) are very likely to change as the codebase matures.

# Installation

Tabulo currently supports Python 2.7 and 3.4–3.6.

## Pre-requisites

To use Tabulo, [TensorFlow](https://www.tensorflow.org/install/) must be installed beforehand. If you want **GPU support**, you should install the GPU version of TensorFlow with `pip install tensorflow-gpu`, or else you can use the CPU version using `pip install tensorflow`.

## Installing Luminoth

First, clone the repo on your machine and then install with `pip`:

```bash
git clone https://github.com/tryolabs/tabulo.git
cd tabulo
pip install -e .
```

## Check that the installation worked

Simply run `lumi --help`.

# Supported models

Currently, we support the following models:

* **Object Detection**
  * [Faster R-CNN](https://arxiv.org/abs/1506.01497)
  * [SSD](https://arxiv.org/abs/1512.02325)

We also provide **pre-trained checkpoints** for the above models trained on popular datasets such as [COCO](http://cocodataset.org/) and [Pascal](http://host.robots.ox.ac.uk/pascal/VOC/).

# Usage

There is one main command line interface which you can use with the `lumi` command. Whenever you are confused on how you are supposed to do something just type:

`lumi --help` or `lumi <subcommand> --help`

and a list of available options with descriptions will show up.

## Working with datasets

See [Adapting a dataset](http://luminoth.readthedocs.io/en/latest/usage/dataset.html).

## Training

See [Training your own model](http://luminoth.readthedocs.io/en/latest/usage/training.html) to learn how to train locally or in Google Cloud.

Released under the [BSD 3-Clause](LICENSE).
