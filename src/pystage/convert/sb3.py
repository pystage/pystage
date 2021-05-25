import argparse

from pystage.convert import CodeWriter

parser = argparse.ArgumentParser()
parser.add_argument("file", metavar="FILE", type=str)
args = parser.parse_args()
print(args.file)
