from qiskit import *
from qiskit.compiler import transpile
from qiskit.providers.aer import noise
from qiskit.quantum_info.operators import Operator
from qiskit.quantum_info.synthesis import two_qubit_cnot_decompose
import math
from math import cos
from math import sin
pi = math.pi


# assertion circuits
def classical_assertion(qProg, qubitList, value):
    qr_assert = QuantumRegister(len(qubitList), name="classical_assertion")
    cr_assert = ClassicalRegister(len(qubitList), name="cr_classical_assertion")
    assertCircuit = QuantumCircuit(qr_assert, cr_assert)
    qProg += assertCircuit
    if (value >= pow(2, len(qubitList))):
        print("Value larger than 2^number of qubits")
        return False
    for i in range(len(qubitList)):
        if (value & (1 << i)):
            qProg.x(qr_assert[i])
    for j in range(len(qubitList)):
        qProg.cx(qubitList[j], qr_assert[j])
    qProg.measure(qr_assert, cr_assert)
    return True


def superposition_assertion(qProg, qubitList, phaseDict, flag):
    qr_assert = QuantumRegister(len(qubitList), name="superposition_assertion")
    cr_assert = ClassicalRegister(len(qubitList), name="cr_superposition_assertion")
    assertCircuit = QuantumCircuit(qr_assert, cr_assert)
    # assertion for uniform superposition state
    if flag == 0:
        qProg += assertCircuit
        for i in range(len(qubitList)):
            qProg.cx(qubitList[i], qr_assert[i])
            qProg.h(qubitList[i])
            qProg.h(qr_assert[i])
            qProg.cx(qubitList[i], qr_assert[i])
        qProg.measure(qr_assert, cr_assert)
    elif flag == 1:
        qProg += assertCircuit
        if (len(qubitList) != len(phaseDict)):
            print("qubitList length and phaseDict length does not match")
            return False
        for i in range(len(qubitList)):
            qProg += assertCircuit
            if (len(qubitList) != len(phaseDict)):
                print("qubitList length and phaseDict length does not match")
                return False
            for i in range(len(qubitList)):
                theta = phaseDict[qubitList[i]][0]
                phi = phaseDict[qubitList[i]][1]
                #print(theta, phi)
                qProg.h(qr_assert[i])
                qProg.cu3(2 * theta, phi, pi - phi, qr_assert[i], qubitList[i])
                qProg.h(qr_assert[i])
        qProg.measure(qr_assert, cr_assert)
    else:
        print("Invalid flag")
        return False
    return True


def entanglement_assertion(qProg, qubitList, flag):
    qr_assert = QuantumRegister(1, name="entanglement_assertion")
    cr_assert = ClassicalRegister(1, name="cr_entanglement_assertion")

    assertCircuit = QuantumCircuit(qr_assert, cr_assert)
    qProg += assertCircuit
    # assertion for pattern "a|00> + b|11>"
    if flag == 0:
        # even number of qubits
        if len(qubitList) % 2 == 0:
            for i in range(len(qubitList)):
                qProg.cx(qubitList[i], qr_assert[0])
        # odd number of qubits
        elif len(qubitList) % 2 == 1:
            for i in range(len(qubitList)):
                qProg.cx(qubitList[i], qr_assert[0])
            for i in range(len(qubitList)):
                if i % 2 == 1:
                    qProg.cx(qubitList[i], qr_assert[0])
    # assertion for pattern "a|01> + b|10>"
    elif flag == 1:
        qProg.x(qr_assert[0])
        # even number of qubits
        if len(qubitList) % 2 == 0:
            for i in range(len(qubitList)):
                qProg.cx(qubitList[i], qr_assert[0])
        # odd number of qubits
        elif len(qubitList) % 2 == 1:
            for i in range(len(qubitList)):
                qProg.cx(qubitList[i], qr_assert[0])
            for i in range(len(qubitList)):
                if i % 2 == 1:
                    qProg.cx(qubitList[i], qr_assert[0])
    else:
        print("Invalid flag")
        return False
    qProg.measure(qr_assert, cr_assert)
    return True


def calcSuccessrate(result, correct_output, num_assertion):
    probability = 0
    total = 0
    success = 0
    assertionString = '0' * num_assertion
    for keys in result.keys():
        if num_assertion == 0:
            total += result[keys]
        elif keys.startswith(assertionString):
            total += result[keys]
    for outputs in correct_output:
        success += result[outputs]

    probability = success / total
    print("total_count = ", total, "success_count = ", success, "success_rate = ", probability*100, "%")