#!/bin/bash

./build.sh

for tnum in ./test/*
do
    ./run.sh ${tnum}/input.json ${tnum}/user_output.json
done
