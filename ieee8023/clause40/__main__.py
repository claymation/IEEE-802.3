import argparse
import sys

from . import PHY


parser = argparse.ArgumentParser(description="1000BASE-T PHY model")

parser.add_argument("TXD", type=bytes.fromhex, nargs="?", help="Transmit data (hex string)")
parser.add_argument("--master", action="store_true", help="Master PHY")
parser.add_argument("--mdi-x", action="store_true", help="MDI-X (DCE)")

args = parser.parse_args()

phy = PHY(TXD=args.TXD, master=args.master, mdi_x=args.mdi_x)

phy.run()