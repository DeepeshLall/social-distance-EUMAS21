#!/bin/bash

numberOfAgents=$1
max_numberOfSlots=$2
slotCapacity=$3

Cdump="data/customers/dump/N${numberOfAgents}_M"
Cpickle="data/customers/pickle/N${numberOfAgents}_M"

Mdump="data/market/dump/N${numberOfAgents}_M"
Mpickle="data/market/pickle/N${numberOfAgents}_M"

rm -vf "$Cdump"*.dat "$Cpickle"*.pk
rm -vf "$Mdump"*.dat "$Mpickle"*.pk

timeResult="results/time/csv/N${numberOfAgents}_K${slotCapacity}.csv"
valResult="results/val/csv/N${numberOfAgents}_K${slotCapacity}.csv"

rm -vf "$timeResult"
rm -vf "$valResult"
