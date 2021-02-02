import utils

if __name__ == '__main__':
    # SparkContext 实现了 __exit__ 因此使用 with 语句更优雅
    with utils.get_spark_context(app_name='0301') as sc:
        data = list(range(1, 6))
        distData = sc.parallelize(data)
        result = distData.collect()
        print(result)
