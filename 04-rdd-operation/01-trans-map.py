from pyspark import SparkContext

import utils


def map_double(spark_context: SparkContext):
    data = list(range(1, 6))
    rdd = spark_context.parallelize(data)
    result = rdd.map(lambda x: x * 2).collect()
    print(result)


def map_tuple(spark_context: SparkContext):
    data = ['dog', 'cat', 'rat']
    rdd = spark_context.parallelize(data)
    result = rdd.map(lambda x: (x, 1)).collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0401') as sc:
        map_double(sc)
        map_tuple(sc)
