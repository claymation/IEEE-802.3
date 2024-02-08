import json
import sys

from ..types import SYMB_4D


class MDI:
    def output(self, tx_symb_vector):
        print(tx_symb_vector, file=sys.stderr)
        print(json.dumps(tx_symb_vector))        

    def sample(self):
        try:
            return SYMB_4D(*json.loads(input()))
        except EOFError:
            return None
