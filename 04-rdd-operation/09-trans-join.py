from pyspark import SparkContext
import utils


def join_score(spark_context: SparkContext):
    math_score = [
        ('lihs', 118),
        ('sunyl', 100),
        ('zhengsy', 119),
    ]
    meow_score = [
        ('lihs', 120),
        ('zhengsy', 130),
        ('zhengsy', 140),
        ('hudi', 140),
        ('jojo', 80),
    ]
    rdd0 = spark_context.parallelize(math_score)
    rdd1 = spark_context.parallelize(meow_score)

    # inner join
    print('join (inner)')
    result = rdd0.join(rdd1) \
        .collect()
    print(result)
    print('\n - - - \n')

    print('leftOuterJoin')
    result = rdd0.leftOuterJoin(rdd1) \
        .collect()
    print(result)
    print('\n - - - \n')

    print('rightOuterJoin')
    result = rdd0.rightOuterJoin(rdd1) \
        .collect()
    print(result)
    print('\n - - - \n')

    print('fullOuterJoin')
    result = rdd0.fullOuterJoin(rdd1) \
        .collect()
    print(result)
    print('\n - - - \n')


if __name__ == '__main__':
    with utils.get_spark_context(app_name='0409') as sc:
        join_score(sc)
