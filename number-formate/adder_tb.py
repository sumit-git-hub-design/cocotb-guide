import cocotb
import logging

# This decorator tells Cocotb that this function is a test
@cocotb.test()
async def test(dut):
    """
    Simple Cocotb test to demonstrate logging
    and number format conversions (decimal, hex, binary).
    
    'dut' stands for Device Under Test.
    Cocotb automatically passes it when the test runs.
    """

    # Set logging level to INFO so info messages are printed
    logging.getLogger().setLevel(logging.INFO)

    # Define an integer variable
    a = 10

    # Print value in decimal format
    # %0d is used for decimal integers
    logging.info("Value of a in decimal format: %0d", a)

    # Print value in hexadecimal format
    # %0x converts integer to hexadecimal
    logging.info("Value of a in hexadecimal format: %0x", a)

    # Print value in binary format
    # Python does not have a direct %b formatter in logging,
    # so we use f-string formatting instead.
    # {a:08b} means:
    #   - convert 'a' to binary
    #   - pad with zeros
    #   - total width = 8 bits
    # 8'b is a Verilog-style prefix for readability
    logging.info("Value of a in binary format: %s", f"8'b{a:08b}")
