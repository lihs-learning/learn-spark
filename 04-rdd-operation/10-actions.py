from pyspark import SparkContext
import utils


def actions_demo(spark_context: SparkContext):
    data = list(range(0, 10))
    rdd = spark_context.parallelize(data)

    print('collect')
    result = rdd.collect()
    print(result)

    print('count')
    result = rdd.count()
    print(result)

    print('take')
    result = rdd.take(3)
    print(result)

    print('max')
    result = rdd.max()
    print(result)

    print('min')
    result = rdd.min()
    print(result)

    print('sum')
    result = rdd.sum()
    print(result)

    print('reduce')
    result = rdd.reduce(lambda m, n: m + 2 * n)
    print(result)

    print('foreach')
    rdd.foreach(lambda x: print(x))


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0408') as sc:
        actions_demo(sc)
