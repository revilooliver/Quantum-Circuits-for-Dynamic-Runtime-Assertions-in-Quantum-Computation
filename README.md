# Quantum-Circuits-for-Dynamic-Runtime-Assertions-in-Quantum-Computation
This repository contains artifacts and test files to reproduce experiments from the ASPLOS 2020 paper "Quantum circuits for dynamic runtime assertions in quantum computation" by J.Liu and H.Zhou

System pre-requisities for Qiskit
========================
* Ubuntu 16.04 or later
* macOS 10.12.6 or later
* Windows 7 or later

Software pre-requisites
=======================

* Python 3.5+
* Qiskit version 0.13.0+


You can install above dependencies on Linux via:
```
$ pip install qiskit
```
You can also check the following documentation for installing Qiskit:
https://qiskit.org/documentation/install.html

Installation
============

If Qiskit is installed successfully, copy and paste the assertion.py file under compiler folder "\qiskit\compiler" in Qiskit installation directory.

Testing installation
=======================

You can run the testing.ipydb file to test.

Running experimental workflows
=======================

Validation of results
=======================
You can run the validation files in test folder to validate the experiments for assertion circuit fidelity and successrate improvement.
