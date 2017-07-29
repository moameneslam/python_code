from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import *
from pyspark.sql.functions import udf
from pyspark.sql.types import *
con = SparkConf()
sc = SparkContext(conf = con)
sql = SQLContext(sc)

def double(A):
	return A*A

abc = udf(double, IntegerType())

rdd1 = sc.textFile("file:///home/cloudera/users.txt")
rdd2 = rdd1.map(lambda x: x.split("|"))
df = sql.createDataFrame(rdd2, ['one', 'two', 'three', 'four', 'five'])
df.show()
df.select("one", "two").show()
df.select(df.one, df.two).show()
df.select(df.one.alias("First"), df.two.alias("Second")).show()

df.select(df.one*100, df.two).show()

df.filter(df.one>2).show()
df.sort(df.one).show()
df.sort(df.one.asc()).show()





df.select("four", abc("three")).show()

#from pyspark.sql.types import *
#schema = StructType( [
#	StructField ('fieldName', LongType(), True)
#	])
#x= sql.createDataFrame(records, schema)
