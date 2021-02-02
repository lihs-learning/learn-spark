from pyspark import SparkContext
import utils


def filter_gt(spark_context: SparkContext):
    data = list(range(1, 6))
    rdd = spark_context.parallelize(data)
    result = rdd.map(lambda x: x * 2) \
        .filter(lambda x: x > 5) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0402') as sc:
        filter_gt(sc)
