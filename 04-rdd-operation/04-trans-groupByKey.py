from functools import reduce

from pyspark import SparkContext
import utils


def groupByKey_word(spark_context: SparkContext):
    data = [
        'hello spark',
        'hello world',
        'hello world',
    ]
    rdd = spark_context.parallelize(data)
    grouped_by_key_rdd = rdd.flatMap(lambda line: line.split(' ')) \
        .map(lambda x: (x, 1)) \
        .groupByKey()
    result = grouped_by_key_rdd.collect()
    print(result)
    result = grouped_by_key_rdd.map(lambda k_v: {k_v[0]: list(k_v[1])}) \
        .collect()
    print(result)
    result = grouped_by_key_rdd.map(lambda k_v: {k_v[0]: reduce(lambda n, m: n + m, k_v[1])}) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0404') as sc:
        groupByKey_word(sc)
