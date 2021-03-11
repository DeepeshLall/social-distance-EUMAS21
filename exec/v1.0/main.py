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

# Implementing Opt. Algorithm -- Brute force

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
opt_A = []
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
        opt_A = A
        opt_profile = all_valuation_profile[idx]
        opt_entry = all_entry_profile[idx]

# Final Results of OPT-allocation

# print(opt_A)
# print(opt_val)
# print(opt_profile)
# print(opt_entry)


# Implementing Aprox. Algorithm

# Constructing Valuation matrix
V = []
for person in customers:
    V.append(person.cummulativeValuation)

# Get highest valuation and the customer
max_v_i = list(map(max,V))
v_max = max(max_v_i)
b = customers[max_v_i.index(v_max)]

# Get second highest valuation
person__b = list(customers)
person__b.remove(b)
V__b = []
for person in person__b:
    V__b.append(person.cummulativeValuation)
max_v_i__b = list(map(max, V__b))
v_max__b = max(max_v_i__b)
v_sec = v_max__b

# Set parameters
r = 6*numberOfSlots*(max_slotCapacity-1) ** (1/(max_slotCapacity-2))
Q = [0]*numberOfSlots
P_0 = [v_max/(6*numberOfSlots*(max_slotCapacity-1))] * numberOfSlots

# Iterate and allocate to all customers
A = []
entry_list = []
delay_list = []
for person in customers:
    # Get N = customer - {person}
    N__person = list(customers)
    N__person.remove(person)
    if not person == b:
        v_max__person = v_max
        P = [ round(P_0[s_idx]*r**(Q[s_idx]), 5) for s_idx in range(len(P_0)) ]
        A_person, entry_idx, delay = person.demand_oracle(P)
        A.append(A_person)
        entry_list.append(entry_idx)
        delay_list.append(delay)
        Q = [ (Q[s_idx] + A_person[s_idx]) for s_idx in range(numberOfSlots) ]
    else:
        v_max__person = v_sec
        v_max_person = max(person.cummulativeValuation)
        entry_idx = person.cummulativeValuation.index(v_max_person)
        A_person = [0]*entry_idx + [1]*person.demand + [0]*((numberOfSlots - person.demand - entry_idx))
        A.append(A_person)
        entry_list.append(entry_idx)
        delay_list.append(v_max__person)
    shop.bookSlot(person, entry_idx, entry_idx+person.demand-1, delay_list[-1])

alg_val = 0
alg_profile = []
alg_entry = []
for person in customers:
    if person.allocatedSlot_start_idx == -1:
        alg_profile.append(0)
        alg_entry.append(-1)
        continue
    alg_val += person.cummulativeValuation[person.allocatedSlot_start_idx]
    alg_profile.append(person.cummulativeValuation[person.allocatedSlot_start_idx])
    alg_entry.append(person.allocatedSlot_start_idx)

# Final Results of OPT-allocation

# print(A)
# print(alg_val)
# print(alg_profile)
# print(alg_entry)
