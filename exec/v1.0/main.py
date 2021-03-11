#!/usr/bin/env python

from customer import *
from shop import *

# Get the market
market = gen_market(numberOfSlots, max_slotCapacity)

# Get customer with each market's shop view
customers = gen_customers(numberOfAgents)
for person in customers:
    for shop in market:    
        person.set_shopParameter(shop)

if not len(market) == 1:
    print("Excess number of shop in market.")
    exit(0)

# Below code is modelled only for single shop case
shop = market[0]

# Get all the valuation profile permutation and respectively ordered entry slot for each agent -- if entry_idx == -1 => customer isn't allocated
all_valuation_list = []
all_entry_list = []
for person in customers:
    v_profile = [0]
    entry_idx = [-1]
    v_profile.extend(person.cummulativeValuation)
    entry_idx.extend(range(numberOfSlots-person.demand))
    all_valuation_list.append(v_profile)
    all_entry_list.append(entry_idx)

# It will he of exponential order length
all_entry_profile = list(itertools.product(*all_entry_list))
all_valuation_profile = list(itertools.product(*all_valuation_list))

opt_val = 0
opt_profile = []
opt_entry = []
for idx in range(len(all_valuation_profile)):
    # Construct corresponding A matrix -- allocation matrix
    A = []
    for p_idx in range(len(customers)):
        entry_idx = all_entry_profile[idx][p_idx]
        if entry_idx == -1:
            A.append([0]*numberOfSlots)
            continue
        A_p_idx = [0]*entry_idx + [1]*customers[p_idx].demand + [0]*(numberOfSlots-customers[p_idx].demand-entry_idx)
        A.append(A_p_idx)
    
    # Check if valid entry profile -- accordance to slot-capacity
    isValid = True
    for col in range(numberOfSlots):
        slotOccupancy=0
        for row in range(numberOfAgents):
            if A[row][col] == 1:
                slotOccupancy += 1
        if slotOccupancy > shop.max_slotCapacity:
            isValid = False
            break
    if not isValid:
        continue
    
    # Check and update optimal
    curr_val = sum(all_valuation_profile[idx])
    if curr_val > opt_val:
        opt_val = curr_val
        opt_profile = all_valuation_profile[idx]
        opt_entry = all_entry_profile[idx]

# Final Results of OPT-allocation

# print(opt_val)
# print(opt_profile)
# print(opt_entry)


