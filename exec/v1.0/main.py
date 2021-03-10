#!/usr/bin/env python

from customer import *
from shop import *

market = gen_market(numberOfSlots, max_slotCapacity)
print(market[0].__dict__)

customers = gen_customers(numberOfAgents)
for person in customers:
    for shop in market:    
        person.set_shopParameter(shop)
    # print(person.__dict__)

