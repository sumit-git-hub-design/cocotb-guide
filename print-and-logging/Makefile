# ------------------------------------------------------------
# Select the HDL language used in the design
# Possible values: verilog, vhdl
TOPLEVEL_LANG ?= verilog


# ------------------------------------------------------------
# Select the simulator
# Common options:
#   icarus  -> Icarus Verilog (free, beginner-friendly)
#   verilator -> Fast, widely used
#   questa / xcelium / vcs -> Commercial simulators
SIM ?= icarus


# ------------------------------------------------------------
# List of HDL source files to be compiled
# $(shell pwd) gives the current directory path
# You can add multiple files separated by spaces
VERILOG_SOURCES = $(shell pwd)/adder.sv


# ------------------------------------------------------------
# Name of the top-level module in your Verilog/SystemVerilog code
# This must match exactly with the module name in adder.sv
TOPLEVEL := mux   # Example: module mux (...);


# ------------------------------------------------------------
# Name of the Python test file (without .py extension)
# cocotb will look for adder_tb.py
MODULE   := adder_tb


# ------------------------------------------------------------
# Include cocotb's built-in Makefile
# This line connects your Makefile with cocotb
# It handles compilation, simulation, and test execution
include $(shell cocotb-config --makefiles)/Makefile.sim
