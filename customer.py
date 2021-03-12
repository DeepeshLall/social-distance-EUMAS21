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
    
    def demand_oracle(self, Price_vector):
        max_util = -1
        cummulative_price = windowSum(Price_vector, self.demand)
        utility = [(self.cummulativeValuation[entry_idx] - cummulative_price[entry_idx]) for entry_idx in range(len(self.cummulativeValuation))]
        max_util = max(utility)
        entry_idx = utility.index(max_util)
        if max_util < 0:
            return [0]*numberOfSlots, -1, 0
        allocation = [0]*entry_idx + [1]*self.demand + [0]*(numberOfSlots - self.demand - entry_idx)
        return allocation, entry_idx, cummulative_price[entry_idx]

def gen_customers(numberOfAgents):
    customers = [ Person() for _ in range(numberOfAgents)]
    return customers
