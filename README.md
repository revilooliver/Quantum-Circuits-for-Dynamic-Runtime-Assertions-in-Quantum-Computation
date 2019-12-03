# Quantum-Circuits-for-Dynamic-Runtime-Assertions-in-Quantum-Computation
This repository contains artifacts and test files to reproduce experiments from the ASPLOS 2020 paper "Quantum circuits for dynamic runtime assertions in quantum computation" by J.Liu and H.Zhou
# Software pre-requisites
Python

Hardware pre-requisities
========================
Any of the following architectures:
* Intel-based 
* ARM64 with 64-bit kernel

Software pre-requisites
=======================

* Python 2.7 or 3.3+
* git client
* Collective Knowledge Framework (CK) - http://cKnowledge.org
* All other dependencies will be installed by CK (LLVM 3.9 and plugins)

You can install above dependencies on Ubuntu via:
```
$ sudo apt-get install python python-pip git
$ sudo pip install ck
```

Installation
============

You can install this repository via CK as follows:

```
$ ck pull repo --url=https://github.com/SamAinsworth/reproduce-cgo2017-paper
```

