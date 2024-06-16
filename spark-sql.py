df.createOrReplaceTempView("PERSON_DATA")
val df2 = spark.sql("SELECT * from PERSON_DATA")
df2.printSchema()
df2.show()

// Import necessary libraries
import org.apache.spark.sql.SparkSession
import org.graphframes.GraphFrame

// Create a Spark session
val spark = SparkSession.builder.appName("GraphFramesExample").getOrCreate()

// Define vertices and edges as DataFrames
val vertices = spark.createDataFrame(Seq(
  (1, "Scott", 30),
  (2, "David", 40),
  (3, "Mike", 45)
)).toDF("id", "name", "age")

val edges = spark.createDataFrame(Seq(
  (1, 2, "friend"),
  (2, 3, "follow")
)).toDF("src", "dst", "relationship")