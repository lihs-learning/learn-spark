import sys

from pyspark import SparkConf, SparkContext


def run_wc(sc: SparkContext, fp: str):
    result = sc.textFile(fp) \
        .flatMap(lambda line: line.split('\t')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda m, n: m + n) \
        .collect()

    for (word, count) in result:
        print('%s: %i' % (word, count))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: 11-wc <input>", file=sys.stderr)
        sys.exit(-1)

    file_path = sys.argv[1]

    spark_conf = SparkConf()
    with SparkContext(conf=spark_conf) as spark_context:
        run_wc(spark_context, file_path)
