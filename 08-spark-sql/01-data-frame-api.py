import os

from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField


spark_home = os.getenv('SPARK_HOME')


def basic(spark: SparkSession):
    df = spark.read.json(f'{spark_home}/examples/src/main/resources/people.json')
    df.show()
    df.printSchema()

    df.select('name').show()
    df.select(df['name'], df['age'] + 1).show()

    df.filter(df['age'] > 21).show()

    df.groupBy('age').count().show()

    df.createOrReplaceTempView('people')
    sql_df = spark.sql('SELECT * FROM people')
    sql_df.show()


def df_rdd_interface(spark: SparkSession):
    sc = spark.sparkContext
    lines_rdd = sc.textFile(f'{spark_home}/examples/src/main/resources/people.txt')
    parts_rdd = lines_rdd.map(lambda l: l.split(','))
    people_rdd = parts_rdd.map(lambda p: Row(name=p[0], age=int(p[1])))

    people_df = spark.createDataFrame(people_rdd)
    people_df.createOrReplaceTempView('people')
    teenagers_df = spark.sql('SELECT name FROM people WHERE age >= 13 AND age <= 19')
    teenagers_df.show()

    teenagers = teenagers_df.rdd.map(lambda p: f'name: {p.name}').collect()
    for name in teenagers:
        print(name)


def custom_schema(spark: SparkSession):
    sc = spark.sparkContext

    # Load a text file and convert each line to a Row.
    lines = sc.textFile(f'{spark_home}/examples/src/main/resources/people.txt')
    parts = lines.map(lambda l: l.split(','))
    # Each line is converted to a tuple.
    people = parts.map(lambda p: (p[0], p[1].strip()))

    # The schema is encoded in a string.
    schema_string = 'name age'

    fields = [StructField(field_name, StringType(), True) for field_name in schema_string.split()]
    schema = StructType(fields)

    # Apply the schema to the RDD.
    schema_people = spark.createDataFrame(people, schema)

    # Creates a temporary view using the DataFrame
    schema_people.createOrReplaceTempView('people')

    # SQL can be run over DataFrames that have been registered as a table.
    results = spark.sql("SELECT name FROM people")

    results.show()
    # +-------+
    # |   name|
    # +-------+
    # |Michael|
    # |   Andy|
    # | Justin|


if __name__ == '__main__':
    spark_session = SparkSession.builder.appName('0801').getOrCreate()

    basic(spark_session)
    df_rdd_interface(spark_session)

    spark_session.stop()
