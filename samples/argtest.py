import argparse
import logging

parser = argparse.ArgumentParser()
# two integers
parser.add_argument("num1", help="the first number", type=int)
parser.add_argument("num2", help="the second number", type=int)
# a string, limited to a list of options
parser.add_argument("op", help="the desired arithmetic operation", choices=['add', 'sub', 'mul', 'div'])
# an optional flag, true by default, with a short and a long name
parser.add_argument("-v", "--verbose", help="turn on verbose output", action="store_true")

opts = parser.parse_args()

if opts.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.debug("First number: %d" % opts.num1)
logging.debug("Second number: %d" % opts.num2)
logging.debug("Operation: %s" % opts.op)

if opts.op == "add":
    result = opts.num1 + opts.num2
elif opts.op == "sub":
    result = opts.num1 - opts.num2
elif opts.op == "mul":
    result = opts.num1 * opts.num2
elif opts.op == "div":
    result = opts.num1 / opts.num2

print(result)