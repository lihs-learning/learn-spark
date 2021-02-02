from pyspark import SparkContext
import utils


def sortByKey_word(spark_context: SparkContext):
    data = [
        'hello spark',
        'hello world',
        'hello world',
    ]
    rdd = spark_context.parallelize(data)
    result = rdd.flatMap(lambda line: line.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .map(lambda k_v: (k_v[1], k_v[0])) \
        .sortByKey(ascending=False) \
        .map(lambda k_v: (k_v[1], k_v[0])) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0406') as sc:
        sortByKey_word(sc)
