from collections import namedtuple


WIRE_PAIR_NAMES = ("BI_DA", "BI_DB", "BI_DC", "BI_DD")
"""The four wire pairs in the 1000BASE-T medium"""

SYMB_4D = namedtuple("SYMB_4D", WIRE_PAIR_NAMES, defaults=(0, 0, 0, 0))
"""A vector of four quinary symbols (§40.2.5.1, §40.2.6.1)"""


class Signal:
    """
    Models a signal produced by one block and consumed by one or more blocks.
    """
    def __init__(self, initial_value):
        self.value = initial_value

    def set(self, value):
        self.value = value

    def get(self):
        return value