from pyspark import SparkContext
import utils


def reduceByKey_word(spark_context: SparkContext):
    data = [
        'hello spark',
        'hello world',
        'hello world',
    ]
    rdd = spark_context.parallelize(data)
    result = rdd.flatMap(lambda line: line.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0405') as sc:
        reduceByKey_word(sc)
