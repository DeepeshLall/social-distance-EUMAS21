#!/bin/bash

# Default mode = 1 -- if 2 then readMode of prev. data for given 3 cmdline parameters.
dataLoadMode=1
numberOfAgents=$1
max_numberOfSlots=$2
slotCapacity=$3

for m in $(seq 3 "$max_numberOfSlots");
do
    total_iter=$((20));
    for iter in $(seq 1 "$total_iter");
    do 
        echo "======= STARTING SLOT NUMBER MAX = ${m}, ITERATION NUMBER = ${iter} =======";
        python3 main.py "$dataLoadMode" "$numberOfAgents" "$m" "$slotCapacity";
        echo "";
        echo "";
    done
    # Script to update Plot
    echo "Ploting dynamically ..."
    python3 "results/time/plotter.py" "results/time/csv/N${numberOfAgents}_K${slotCapacity}.csv"
    python3 "results/val/plotter.py" "results/val/csv/N${numberOfAgents}_K${slotCapacity}.csv"
    python3 "results/time/plotter_2.py" "results/time/csv/N${numberOfAgents}_K${slotCapacity}.csv"
    python3 "results/val/plotter_2.py" "results/val/csv/N${numberOfAgents}_K${slotCapacity}.csv"
done
