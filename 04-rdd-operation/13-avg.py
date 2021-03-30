import sys

from pyspark import SparkConf, SparkContext


def run_avg(sc: SparkContext, ifp: str):
    age_data = sc.textFile(ifp).map(lambda line: line.split(' ')[1]).map(lambda s: int(s))
    total = age_data.reduce(lambda m, n: m + n)
    count = age_data.count()

    avg = total / count

    print('total: %i' % total)
    print('count: %i' % count)
    print('avg: %f' % avg)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: 13-avg <input>", file=sys.stderr)
        sys.exit(-1)

    in_file_path = sys.argv[1]

    spark_conf = SparkConf()
    with SparkContext(conf=spark_conf) as spark_context:
        run_avg(spark_context, in_file_path)
