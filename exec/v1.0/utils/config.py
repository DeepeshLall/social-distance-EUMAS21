#!/usr/bin/env python

# numberOfAgents = 250
# numberOfSlots = 25
# max_slotCapacity = 15

numberOfAgents = 10
numberOfSlots = 16
max_slotCapacity = 5

# Max demand -- can be equal to numberOfSlots(max) and 1(min) and is semi-inclusive set i.e. [a,a+D)
max_Demand = 4

# Urgency = 1 (Less urgent), 2 (Medium urgent), 3 (Extremly urgent)
numberOfUrgency = 3

# Rate at which valuation fall for each agent with lower preference (1--highly preferred and so on) -- default Value
shopSlotPreferenceDecayFactor = 0.10

# Factor used to scale up the valuation matrix (for precision under -- 5 decimal places)
scaleFactor = 1000

numberOfShops = 1
