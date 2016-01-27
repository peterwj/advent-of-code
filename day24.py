#!/usr/bin/python
from functools import reduce
from sys import argv as argv
from unittest import main, TestCase

class PresentConfiguration:
    def __init__(self, groups):
        # groups is a list of lists, each of which is a list of present weights
        assert(len(groups) == 3)
        self._groups = groups
        self.glove_group = groups[0]
        self._qe = reduce(lambda x,y: x*y, self.glove_group, 1)

    @property
    def qe(self):
        return self._qe

    def __lt__(self, pc):
        if len(self.glove_group) != len(pc.glove_group):
            # compare first group
            return len(self.glove_group) < len(pc.glove_group)
        else:
            return self._qe < pc._qe

    def __eq__(self, pc):
        return (
                len(self.glove_group) == len(pc.glove_group) and
                self._qe == pc._qe
        )
    def __ne__(self, pc):
        return not self.__eq__(pc)

class TestDay24(TestCase):
    def test_basic_comparison(self):
        config1 = PresentConfiguration([[11,9],[10,8,2], [7,5,4,3,1]])
        config2 = PresentConfiguration([[10,1,9],[11,7,2], [8,5,4,3]])
        assert(config1 < config2)
        assert(config1.qe == 99)
        assert(config2.qe == 90)

if __name__ == '__main__':
    main()
