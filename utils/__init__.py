from pyspark import SparkConf, SparkContext


# 实际应该使用 $SPARK_HOME/bin/spark-submit 来提交作业，
# 而不应该硬编码
def get_spark_context(app_name):
    conf = SparkConf() \
        .setMaster('local[2]') \
        .setAppName(app_name)
    return SparkContext(conf=conf)
