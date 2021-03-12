#!/bin/bash

# Default mode = 1 
dataLoadMode=1
numberOfAgents=$1
max_numberOfSlots=$2
slotCapacity=$3

for m in $(seq 2 "$max_numberOfSlots");
do
    total_iter=$((10*"$m"));
    for iter in $(seq 1 "$total_iter");
    do 
        echo "SLOT NUMBER MAX =${m}, ITERATION NO.=${iter}";
        python3 main.py "$dataLoadMode" "$numberOfAgents" "$m" "$slotCapacity";
    done
done
