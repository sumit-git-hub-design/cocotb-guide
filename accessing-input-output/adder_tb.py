import cocotb
import logging

# The 'from ... import ...' statement is used to import
# specific items from a module instead of the whole module.
from cocotb.triggers import Timer

# This decorator tells Cocotb that this function is a test
@cocotb.test()
async def test(dut):
    """
    This test shows how to:
    1. Access DUT (Design Under Test) signals
    2. Drive values onto input signals
    3. Wait for simulation time using Timer
    """

    # 'dut' represents the top-level Verilog/VHDL module
    # dut.a and dut.b are signals declared in the RTL

    # Get handle to signal 'a'
    a_val = dut.a

    # Drive value 12 onto signal 'a'
    # Cocotb automatically converts Python int to HDL value
    a_val.value = 12

    # Get handle to signal 'b'
    b_val = dut.b

    # Drive value 15 onto signal 'b'
    b_val.value = 15

    # Wait for 10 nanoseconds of simulation time
    # This does NOT block your CPU – it advances simulator time
    await Timer(10, units='ns')

    # Optional: print values for debugging
    logging.info("Value of a = %d", a_val.value)
    logging.info("Value of b = %d", b_val.value)
