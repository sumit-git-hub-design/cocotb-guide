import cocotb
import logging
from cocotb.triggers import Timer

@cocotb.test()
async def test(dut):
    """
    This test demonstrates how to drive DUT signals in Cocotb
    and explains the difference between '.value =' and '<='.
    """
      #dut.a.value = 12
      #dut.b.value = 15
  
    # Drive values to DUT input signals
    # In Cocotb, '<=' is overloaded to mean signal assignment,
    # similar to non-blocking assignment in Verilog.
    dut.a <= 12
    dut.b <= 15

    # Wait for 10 nanoseconds of simulation time
    await Timer(10, units='ns')
