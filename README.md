# Quantum-Circuits-for-Dynamic-Runtime-Assertions-in-Quantum-Computation
This repository contains artifacts and test files to reproduce experiments from the ASPLOS 2020 paper "Quantum circuits for dynamic runtime assertions in quantum computation" by J.Liu, G.Byrd and H.Zhou

Use at your own risk! In no event shall the authors be liable for any damages whatsoever (including without limitation damages for loss of business profits, business interruption, loss of business information, or any other pecuniary loss) arising from the use of or inability to use the software, even if the authors have been advised of the possibility of such damages.

If you have any questions feel free to contact us using jliu45@ncsu.edu

System pre-requisities for Qiskit
========================
* Ubuntu 16.04 or later
* macOS 10.12.6 or later
* Windows 7 or later

Software pre-requisites
=======================

* Python 3.5+
* Qiskit version 0.13.0+
* Jupyter notebook


You can install above dependencies on Linux via:
```
$ pip install qiskit
```
You can also check the following documentation for installing Qiskit:
https://qiskit.org/documentation/install.html

Installation
============

If Qiskit is installed successfully, copy and paste the assertion.py file under compiler folder "...\qiskit\compiler" in Qiskit installation directory.

Testing installation
=======================

You can run the testing.ipydb file to test.

Running experimental workflows
=======================

To run the experiments for the fidelity of our assertion circuit, run the jupyter notebooks under the folder named "fidelity". Tests should take less than 10 mins for the 20-qubit quantum computers, depending on the number of jobs submitted to the machine.

To run the experiments for the success rate of different benchmarks, run the jupyter notebooks under the folder named "benchmark". Test could take dozens of minutes, depending on the number of jobs submitted to the machine.

Validation of results
=======================

You can run the jupyter notebooks in benchmark folder to validate the experiments for assertion circuit fidelity and successrate improvement. The jupyter notebooks in benchmark folder contains the results that we run on "ibmqx2" machine.


Experiment customization 
=======================
The jupyter notebooks are all customizable to run different assertions with different benchmarks. To insert different assertion circuits, first import the corresponding assertion function:

from qiskit.compiler.assertion import classical_assertion, superposition_assertion, entanglement_assertion, calcSuccessrate

Then call the functions as described in Section.4. The assertion function will insert the assertion circuits to the circuit under test.

"calcSuccessrate" function is designed to calculate the success rate of the circuit based on the output from the backend.
For example, calcSuccessrate(result = res.get_counts(0), correct_output = ['0 1111', '0 0000'], num_assertion = 1) calculates the success rate based on the output result.get_counts(0). The correct outputs are '0 1111' and '0 0000', the number of assertion bit is 1. The assertion bits will always be the most significant bits of the output.
For calculate the success rate without assertion, set the num_assertion = 0.


Notes
=======================

Due to the hardware property difference of different backends, the results of fidelity and success rate may differ.  When running the experiments on backends with limited connectivity, the inserted assertion circuit may introduce too many extra swap gates and therefore hurt the success rate of the circuit under test. In our paper, we ran our experiments on ibmq_20_tokyo quantum computer which offers the best connectivity among all the 20-qubit machines. However, this quantum computer has retired. Among the currently available 20-qubit machines, imbq_boeblingen has the lowest noise level, so we recommend to reproduce the experiments on boeblingen machine. If you do not have access to the 20 qubit machines, among the publically available machines, ibmqx2 has the best connectivity and we recommend to reproduce the experiments on ibmqx2 machine.

The transpiler from Qiskit uses the stochastic swap pass, so the number of swap gates (each swap gate consists of three CNOT gates) inserted for the logical-to-physical mapping may vary for the reproductions of the same experiment. We recommend use the circuit.count_ops() function in Qiskit to check minimum number of CNOT gates is inserted after logical-to-physical mapping.

