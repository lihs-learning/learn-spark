import sys

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext


def word_count(scc: StreamingContext, hostname: str, port: int):
    # lines = scc.socketTextStream('localhost', 9999)
    # words = lines.flatMap(lambda line: line.split(' '))
    # pairs = words.map(lambda word: (word, 1))
    # word_counts = pairs.reduceByKey(lambda m, n: m + n)
    word_counts = scc.socketTextStream(hostname, port)\
        .flatMap(lambda line: line.split(' '))\
        .map(lambda word: (word, 1))\
        .reduceByKey(lambda m, n: m + n)

    word_counts.pprint()

    scc.start()
    scc.awaitTermination()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: 11-wc <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    h = sys.argv[1]
    p = int(sys.argv[2])

    spark_conf = SparkConf()

    spark_context = SparkContext(conf=spark_conf)
    streaming_context = StreamingContext(spark_context, 5)
    word_count(streaming_context, h, p)
