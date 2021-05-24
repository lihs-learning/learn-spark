#!/bin/bash

$SPARK_HOME/bin/spark-submit --master local[2] --name 0902 ./02-wc-local-file.py ./tmp-wc-local
