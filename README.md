# PyCat

[![Release](https://img.shields.io/github/release/aweimeow/PyCat.svg)](https://github.com/aweimeow/PyCat)
[![Build Status](https://api.travis-ci.org/aweimeow/PyCat.svg?branch=master)](https://travis-ci.org/aweimeow/PyCat)
[![LICENSE](https://img.shields.io/github/license/aweimeow/PyCat.svg)](https://github.com/aweimeow/PyCat/blob/master/LICENSE)
[![Coverage Status](https://coveralls.io/repos/github/aweimeow/PyCat/badge.svg?branch=master)](https://coveralls.io/github/aweimeow/PyCat?branch=master)

** An implementation of netcat in Python ** 🎉 

## Installation

```bash
git clone https://github.com/aweimeow/PyCat
cd PyCat

python setup.py install
```

## Usage

```
pycat [ -h ] -t IP [ -p PORT ]

-t IP
    Required, 
    Accept IPv4 format and IPv4 with netmask.

-p PORT
    Optional, 
    Accept comma seperated number(e.g. 1,2,3,4) and port range with dash(e.g. 1-100), 
    If PORT is not given, pycat will scan port from 1 to 1023.
```

---

## Development Guide

#### Develop environment prepare

```bash
$ cd PyCat
$ virtualenv venv -p python3
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python setup.py install
```

