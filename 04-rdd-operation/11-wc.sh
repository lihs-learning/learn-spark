#!/bin/bash

cp ../data/words.txt /tmp/spark-test-words.txt
# 也支持目录 通配符*
$SPARK_HOME/bin/spark-submit --master local[2] --name 0411 ./11-wc.py file:///tmp/spark-test-words.txt
rm /tmp/spark-test-words.txt
