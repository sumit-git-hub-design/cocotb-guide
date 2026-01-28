**print-vs-logging

This folder demonstrates the difference between using print() and logging in a cocotb-based testbench.

The example uses a simple Verilog design and a Python cocotb test to show how output messages appear during simulation.


**Folder Structure
print-vs-logging/

├── design.v        # Verilog design (Device Under Test)

├── tb-code.py    # cocotb testbench using print and logging

└── Makefile       # Makefile to run cocotb simulation


** design.v

This file contains a simple Verilog adder module

It acts as the DUT (Device Under Test)

cocotb connects to this module during simulation

The module name is used as TOPLEVEL in the Makefile


**tb-code.py

This is a Python-based cocotb testbench

It uses @cocotb.test() to define a test

dut represents the Verilog adder module

The test prints messages using:

print() → simple output

logging.info() → structured and professional output

Why this file is important:

Helps beginners see the difference in simulator output

Shows why logging is preferred in real projects


 **print vs logging (Concept)
print()

Easy to use

Good for quick learning

No log levels or formatting

Not recommended for large testbenches

logging

Supports log levels (INFO, DEBUG, ERROR)

Cleaner and timestamped output

Easy to enable/disable messages

Used in professional verification environments


**Makefile

Used to compile design.v

Starts the simulator (Icarus Verilog)

Loads the top module

Runs tb-code.py using cocotb

To run the example:

make


**How to Run
Requirements

Python 3

cocotb installed

Icarus Verilog installed

Run command
make


 **Purpose of this Folder

Teach beginners the difference between print and logging

Show best practices for cocotb testbenches

Provide a minimal, easy-to-understand example


**Key Takeaway

Use print() for learning and quick checks
Use logging for real cocotb projects
