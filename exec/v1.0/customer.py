#!/usr/bin/env python

from utils.header import *

class Person():
    def __init__(self):
        self.pid = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 5))
        self.allocatedSlot_start_idx = -1
        self.delay = -1
        
    def set_shopParameter(self, shop):
        self.urgency = random.sample(range(1, numberOfUrgency+1), 1)[0]
        self.shopSlotPreferenceDecayFactor = shopSlotPreferenceDecayFactor
        self.demand = random.randint(1, max_Demand)
        self.preference = random.sample(range(1, shop.numberOfSlots+1), shop.numberOfSlots)
        self.valuation = [round(scaleFactor * self.urgency * self.shopSlotPreferenceDecayFactor ** self.preference[slot_idx], 5) for slot_idx in range(shop.numberOfSlots)]
        self.cummulativeValuation = windowSum(self.valuation, self.demand)

def gen_customers(numberOfAgents):
    customers = [ Person() for _ in range(numberOfAgents)]
    return customers
