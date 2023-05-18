<p align="center">
  <!-- Python -->
  <a href="https://www.python.org" alt="Python">
      <img src="https://badges.aleen42.com/src/python.svg" />
  </a>
  <!-- Version -->
  <a href="https://badge.fury.io/py/multipipe"><img src="https://badge.fury.io/py/multipipe.svg" alt="PyPI version" height="18"></a>
  <!-- Black -->
  <a href="https://github.com/psf/black" alt="Code style: black">
      <img src="https://img.shields.io/badge/code%20style-black-000000.svg" />
  </a>
  <!-- License -->
  <a href="https://lbesson.mit-license.org/"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <!-- Google Colab -->
  <!-- <a href="https://colab.research.google.com/github/AmenRa/multipipe/blob/master/notebooks/1_overview.ipynb"> -->
      <!-- <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> -->
  </a>
</p>



## ⚡️ Introduction

[multipipe](https://github.com/AmenRa/multipipe) is a Python utility that allows you to create pipelines of functions to be executed on any given iterable (e.g., lists, generators) leveraging multiprocessing. [multipipe](https://github.com/AmenRa/multipipe) is built on top of [multiprocess](https://github.com/uqfoundation/multiprocess).


## 🔌 Requirements
```
python>=3.8
```

## 💾 Installation
```bash
pip install multipipe
```

## 💡 Examples

### Basic usage
```python
from multipipe import Multipipe

def add(x):
    return x + 1

def mul(x):
    return x * 2

pipe = Multipipe([ add, mul ])
pipe(range(10))
```
Output:
```python
[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
```

### Using partials
```python
from multipipe import Multipipe
from functools import partial

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

pipe = Multipipe([ partial(add, y=1), partial(mul, y=2) ])
pipe(range(10))
```
Output:
```python
[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
```





## 🎁 Feature Requests
Would you like to see other features implemented? Please, open a [feature request](https://github.com/AmenRa/multipipe/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=%5BFeature+Request%5D+title).


## 🤘 Want to contribute?
Would you like to contribute? Please, drop me an [e-mail](mailto:elias.bssn@gmail.com?subject=[GitHub]%20multipipe).


## 📄 License
[multipipe](https://github.com/AmenRa/multipipe) is an open-sourced software licensed under the [MIT license](LICENSE).