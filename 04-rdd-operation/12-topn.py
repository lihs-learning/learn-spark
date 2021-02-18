import sys

from pyspark import SparkConf, SparkContext


def run_wc(sc: SparkContext, ifp: str):
    result = sc.textFile(ifp) \
        .map(lambda line: line.split('\t')) \
        .map(lambda col: (col[5], 1)) \
        .reduceByKey(lambda m, n: m + n) \
        .map(lambda k_v: (k_v[1], k_v[0])) \
        .sortByKey(ascending=False) \
        .map(lambda v_k: (v_k[1], v_k[0])) \
        .take(5)

    for (word, count) in result:
        print('%s: %i' % (word, count))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: 12-topN <input>", file=sys.stderr)
        sys.exit(-1)

    in_file_path = sys.argv[1]

    spark_conf = SparkConf()
    with SparkContext(conf=spark_conf) as spark_context:
        run_wc(spark_context, in_file_path)
