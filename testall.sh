#!/bin/bash

./build.sh

for tnum in ./test/*
do
    cat ${tnum}/desc.txt
    python ./compare.py ${tnum}/user_output.json -r ${tnum}/output.json
done
