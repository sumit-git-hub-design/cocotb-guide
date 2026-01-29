import cocotb
import logging
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge, FallingEdge, Edge

# This is a cocotb test.
# cocotb.test() tells the simulator that this is a test coroutine.
@cocotb.test()
async def test(dut):
    # 'dut' stands for Device Under Test.
    # It gives access to the signals in your HDL design.

    rst = dut.rst      # Get handle to reset signal

    # -------------------------
    # Reset sequence – part 1
    # -------------------------

    rst.value = 1      # Assert reset (assuming active-high reset)

    # Wait for 2 rising edges of the clock
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    rst.value = 0      # Deassert reset

    # -------------------------
    # Reset sequence – part 2
    # -------------------------

    # Wait for 2 falling edges of the clock
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)

    rst.value = 1      # Assert reset again

    # -------------------------
    # Reset sequence – part 3
    # -------------------------

    # Edge() triggers on *either* rising or falling edge
    await Edge(dut.clk)
    await Edge(dut.clk)

    rst.value = 0      # Deassert reset

    # -------------------------
    # Hold reset low for 5 falling edges
    # -------------------------

    for i in range(5):
        await FallingEdge(dut.clk)

    rst.value = 1      # Assert reset again

    # -------------------------
    # Hold reset high for 5 rising edges
    # -------------------------

    for i in range(5):
        await RisingEdge(dut.clk)
