import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v","--version")
parser.add_argument("--tool")

args = parser.parse_args()
print args
