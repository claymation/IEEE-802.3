import argparse

from . import PHY, connect


parser = argparse.ArgumentParser()

parser.add_argument("TXD", type=bytes.fromhex, help="Transmit data (hex string)")

args = parser.parse_args()

p = PHY()
q = PHY()

connect(p, q)

p.transmit(args.TXD)
