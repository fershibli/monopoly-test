import argparse
import logging as log
from run import run_analysis

def main(args):
  if args.verbose:
      log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
      log.info("Verbose output.")
  else:
      log.basicConfig(format="%(levelname)s: %(message)s")

  run_analysis()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
  args = parser.parse_args()
  main(args)