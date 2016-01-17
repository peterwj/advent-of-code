#!/usr/bin/python

class Sue():
    def __init__(self, line):
        line = line.split(' ')
        self._name = line[1].replace(':', '')
        line = line[2:]
        self._items = {}
        for i in range(0,6,2):
            item = line[i].replace(':', '')
            count = int(line[i+1].replace(',', ''))
            self._items[item] = count

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    def __getitem__(self, name):
        return self._items.get(name, None)

class MFCSAM():
    def __init__(self, filename):
        self._items = {}
        with open(filename) as f:
            for line in f:
                line = line.split(': ')
                self._items[line[0]] = int(line[1])

    def __getitem__(self,name):
        return self._items[name]

def is_match(sue, mfcsam, item, part_two=False):
    if part_two:
        if item in ['cats', 'trees']:
            return sue[item] > mfcsam[item]
        elif item in ['pomeranians', 'goldfish']:
            return sue[item] < mfcsam[item]
    return sue[item] == mfcsam[item]

def do_problem(sues_file, mfcsam_file):
    sues = {}
    with open(sues_file) as f:
        for line in f:
            sue = Sue(line)
            sues[sue.name] = sue
    mfcsam = MFCSAM(mfcsam_file)

    for i,sue in sues.items():
        sue_score = 0
        for item,count in sue.items.items():
            if is_match(sue, mfcsam, item, part_two=True):
                sue_score += 1
        if sue_score == 3:
            print(i)
            return

if __name__ == '__main__':
    do_problem('inputs/day16-sues.txt', 'inputs/day16-mfcsam.txt')
