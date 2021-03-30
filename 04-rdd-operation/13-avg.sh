#!/bin/bash

cp ../data/sample_age.txt /tmp/spark-test-avg.txt
# 也支持目录 通配符*
$SPARK_HOME/bin/spark-submit --master local[2] --name 0413 ./13-avg.py file:///tmp/spark-test-avg.txt
rm /tmp/spark-test-avg.txt
