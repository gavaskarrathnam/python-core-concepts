def initialize_Spark():

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("simple etl job") \
        .getOrCreate()

    return spark