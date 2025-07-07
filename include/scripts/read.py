# read.py
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("PySpark Example") \
        .getOrCreate()
    #C:\Users\bhanu\local_airflow\include\datasets\full_files\Product_Data.csv
    df = spark.read.csv("./include/datasets/full_files/Product_Data.csv", header="true")
    df.show()
    
    spark.stop()

if __name__ == "__main__":
    main()