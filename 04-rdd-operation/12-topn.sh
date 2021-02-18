#!/bin/bash

cp ../data/page_views.txt /tmp/spark-test-topn.txt
# 也支持目录 通配符*
$SPARK_HOME/bin/spark-submit --master local[2] --name 0412 ./12-topn.py file:///tmp/spark-test-topn.txt
rm /tmp/spark-test-topn.txt
