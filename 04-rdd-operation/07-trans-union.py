from pyspark import SparkContext
import utils


def union_list(spark_context: SparkContext):
    data0 = [1, 2, 3]
    data1 = [4, 5, 6]
    rdd0 = spark_context.parallelize(data0)
    rdd1 = spark_context.parallelize(data1)
    result = rdd0.union(rdd1) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0407') as sc:
        union_list(sc)
