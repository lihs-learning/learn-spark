from pyspark import SparkContext
import utils


def flatMap_split_space(spark_context: SparkContext):
    data = [
        'hello spark',
        'hello world',
        'hello world',
    ]
    rdd = spark_context.parallelize(data)

    # 如果是 map 拆分的话将会增加 1 维度，即变为 2 纬数组
    result = rdd.flatMap(lambda line: line.split(' ')) \
        .map(lambda x: (x, 1)) \
        .collect()
    print(result)


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0403') as sc:
        flatMap_split_space(sc)
