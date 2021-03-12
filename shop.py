#!/usr/bin/env python

from utils.header import *

class Shop():
    def __init__(self, numberOfSlots, max_slotCapacity):
        self.sid = ''.join(random.choices(string.ascii_uppercase + string.ascii_uppercase + string.digits, k=2))
        self.numberOfSlots = numberOfSlots
        self.max_slotCapacity = max_slotCapacity
        self.slotCapacity = [self.max_slotCapacity] * self.numberOfSlots
        self.perSlotPeople = []
        self.set_perSlotPeople()

    def set_perSlotPeople(self):
        for _ in range(numberOfSlots):
            self.perSlotPeople.append([])
    
    def bookSlot(self, customer, Slot_entry, Slot_exit, Price):
        customer.allocatedSlot_start_idx = Slot_entry
        customer.delay = Price
        for slot_idx in range(Slot_entry, Slot_exit+1):
            self.slotCapacity[slot_idx] -= 1
            self.perSlotPeople[slot_idx].append(customer)
        return

    def isFree(self, slotEntry_idx, slotExit_idx):
        for slot_idx in range(slotEntry_idx, slotExit_idx+1):
            if self.slotCapacity[slot_idx] == 0:
                return False
        return True

def gen_market(numberOfSlots, max_slotCapacity, numberOfShops=1):
    market = [ Shop(numberOfSlots, max_slotCapacity) for _ in range(numberOfShops) ]
    return market
