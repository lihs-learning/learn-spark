#!/bin/bash

$SPARK_HOME/bin/spark-submit --master local[2] --name 0901 ./01-wc.py localhost 9999
