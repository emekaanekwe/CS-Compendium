#TODO: NEEDS FIXING
# TODO: how extends works?
# TODO: make a regular expression command to read the words containing "ing" and return those as strings
from typing import List
import numpy 


class Bot:

    def __init__(self, model, energy, version):
        # string
        self.model = model
        # int
        self.energy = energy
        # float
        self.version = version
        # complex
        # self.energy_value = None
        # list, tuple, range
        # self.part_list = None
        # set
        # self.attribute_set = None
        # dictionary
        #self.action_sequence = action_sequence
        # bool
        # self.has_energy = None
        # byte/bytearrays?

    def walk(self):
        print(self.model + " is walking")

    def stop(self):
        print(self.model + " has stopped")


class BotList:

    def __init__(self, name, part_list, attribute_set, action_sequence, has_energy):
        # string
        self.name = name
        # list, tuple, range
        self.part_list = part_list
        # set
        self.attribute_set = attribute_set
        # dictionary
        self.action_sequence = action_sequence
        # bool
        self.has_energy = has_energy


class Lists:
    def __init__(self, li):
        self.li = li
    def appending(self, li, a):
        li.append(a)
    def removing(self, li, rem):
        li.remove(rem)
    def inserting(self, li, i, x):
        li.insert(i, x)
    def extending(self, li):
        li.extend()
    def popping(self, li, po):
        li.pop(po)
    def clearing(self, li):
        li.clear()
    # find the next ind start at position x
    def indexing(self, li, start, end):
        li.index(start, end)
    def counting(self, li, cou):
        li.count(cou)
    def sorting(self, li):
        li.sort()

class Dictionaries:

    def __init__(self, dict):
        self.dict = dict

        def show_dict(sho):
            sho = dict
            print(show_dict(**sho))
            
bot = Bot(1, 2, 3)

l = Lists([1])
l.appending(1, 1)

print(bot.walk)
print(l)