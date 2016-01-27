#!/usr/bin/python

import numpy as np
from sys import argv as argv
from unittest import main, TestCase

class Instruction:
    def __init__(self, s):
        self._op = s.split(' ')[0]
        s = s.replace('+', '')
        s = s.replace(',', '')
        self._i = OPCODE_MAP[self._op](s)
        self._register = self._i.register
        self._offset = self._i.offset
    @property
    def register(self):
        return self._register
    @property
    def offset(self):
        return self._offset
    def execute(self, ps):
        # ps should be ProgramState
        self._i.execute(ps)

class ProgramState:
    def __init__(self, instruction_strings):
        self.registers = {
                'a': 0,
                'b': 0,
        }
        self.pc = 0 # index into the array of instructions
        self.instructions = [Instruction(s) for s in instruction_strings]

    def run(self):
        while self.pc >= 0 and self.pc < len(self.instructions):
            self.instructions[self.pc].execute(self)

class Half(Instruction):
    def __init__(self, s):
        self._register = s.split(' ')[1]
        self._offset = None
    def execute(self, ps):
        ps.registers[self.register] /= 2
        ps.pc += 1
class Triple(Instruction):
    def __init__(self, s):
        self._register = s.split(' ')[1]
        self._offset = None
    def execute(self, ps):
        ps.registers[self.register] *= 3
        ps.pc += 1
class Increment(Instruction):
    def __init__(self, s):
        self._register = s.split(' ')[1]
        self._offset = None
    def execute(self, ps):
        ps.registers[self.register] += 1
        ps.pc += 1
class Jump(Instruction):
    def __init__(self, s):
        self._offset = int(s.split(' ')[1])
        self._register = None
    def execute(self, ps):
        ps.pc += self._offset
class JumpEven(Instruction):
    def __init__(self, s):
        self._offset = int(s.split(' ')[2])
        self._register = s.split(' ')[1]
    def execute(self, ps):
        if ps.registers[self._register] %2 == 0:
            ps.pc += self._offset
        else:
            ps.pc += 1
class JumpOne(Instruction):
    def __init__(self, s):
        self._offset = int(s.split(' ')[2])
        self._register = s.split(' ')[1]
    def execute(self, ps):
        if ps.registers[self._register] == 1:
            ps.pc += self._offset
        else:
            ps.pc += 1

OPCODE_MAP = {
        'hlf': Half,
        'tpl': Triple,
        'inc': Increment,
        'jmp': Jump,
        'jie': JumpEven,
        'jio': JumpOne,
}

class TestDay23(TestCase):
    def test_increment(self):
        ps = ProgramState(['inc a', 'inc a'])
        ps.run()
        assert(ps.registers['a'] == 2)
    def test_easy_case(self):
        ps = ProgramState([ 'inc a', 'jio a, +2', 'tpl a', 'inc a',])
        ps.run()
        assert(ps.registers['a'] == 2)

if __name__ == '__main__':
    main()

