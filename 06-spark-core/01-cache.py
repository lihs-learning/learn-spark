# 请使用 $SPARK_HOME/bin/pyspark 逐行运行以观察结果

lines = sc.textFile('file:///path/to/project/data/page_views.txt')
lines.count()
# 观察 http://spark-master:4040/jobs/job 对应 Application 的 input
lines.cache()
lines.count()
# 观察 http://spark-master:4040/jobs/job 对应 Application 的 input
lines.count()
# 观察 http://spark-master:4040/jobs/job 对应 Application 的 input
