#!/bin/bash

# Default mode = 1 -- if 2 then readMode of prev. data for given 3 cmdline parameters.
dataLoadMode=1
numberOfAgents=$1
max_numberOfSlots=$2
slotCapacity=$3

for m in $(seq 3 "$max_numberOfSlots");
do
    total_iter=$((1*"$m"));
    for iter in $(seq 1 "$total_iter");
    do 
        echo "======= STARTING SLOT NUMBER MAX = ${m}, ITERATION NUMBER = ${iter} =======";
        python3 main.py "$dataLoadMode" "$numberOfAgents" "$m" "$slotCapacity";
        echo "";
        echo "";
    done
    # Script to update Plot
done
