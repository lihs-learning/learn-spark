import sys

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext


def word_count(scc: StreamingContext, directory: str):
    word_counts = scc.textFileStream(directory)\
        .flatMap(lambda line: line.split(' '))\
        .map(lambda word: (word, 1))\
        .reduceByKey(lambda m, n: m + n)

    word_counts.pprint()

    scc.start()
    scc.awaitTermination()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: 02-wc-local-file <directory>", file=sys.stderr)
        sys.exit(-1)

    dir_path = sys.argv[1]

    spark_conf = SparkConf()

    spark_context = SparkContext(conf=spark_conf)

    streaming_context = StreamingContext(spark_context, 5)

    word_count(streaming_context, dir_path)
