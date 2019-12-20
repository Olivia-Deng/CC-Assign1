#!/bin/bash
spark-submit \
    --master local[4] \
    CTV.py \
    --input $1 \
    --output $2/