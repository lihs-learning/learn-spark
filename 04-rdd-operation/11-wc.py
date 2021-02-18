import sys

from pyspark import SparkConf, SparkContext


def run_wc(sc: SparkContext, ifp: str, ofp: str):
    sc.textFile(ifp) \
        .flatMap(lambda line: line.split('\t')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda m, n: m + n) \
        .saveAsTextFile(ofp)


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: 11-wc <input> <output>", file=sys.stderr)
        sys.exit(-1)

    in_file_path = sys.argv[1]
    out_file_path = sys.argv[2]

    spark_conf = SparkConf()
    with SparkContext(conf=spark_conf) as spark_context:
        run_wc(spark_context, in_file_path, out_file_path)
