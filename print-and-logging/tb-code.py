# cocotb is a Python-based verification framework. It allows writing testbenches in Python instead of SystemVerilog
import cocotb

# logging module is used for structured and configurable messages. It is preferred over print() in professional testbenches
import logging

# @cocotb.test() decorator tells cocotb that this function is a test. cocotb will automatically discover and run this test
@cocotb.test()
async def test(dut):
    """
    This is a simple cocotb test.
    
    dut:
        - 'dut' stands for Device Under Test
        - It is automatically passed by cocotb
        - It represents the top-level HDL module
    """

    # print() is the simplest way to display messages. Useful for quick debugging, but not recommended for large projects
    print('My first cocotb TB')

    # Set logging level to INFO. This ensures INFO, WARNING, ERROR messages are shown
    logging.getLogger().setLevel(logging.INFO)

    # logging.info() prints a timestamped and formatted message
    # Logging is better than print() because:
    # - You can control verbosity (INFO, DEBUG, ERROR)
    # - Output looks cleaner and professional
    # - Easy to disable or filter messages
    logging.info('My first cocotb TB')
