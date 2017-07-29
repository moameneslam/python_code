from pyspark import SparkConf, SparkContext
import math

def format0(rec):
	Record = rec.split("|")
	return(Record)

def format1(rec):	
	Record = rec.split("\t")
	return(Record)


con = SparkConf()
sc = SparkContext(conf = con)

movie=sc.textFile("file:///home/cloudera/imdb/Movies.item", use_unicode=True)
rating=sc.textFile("file:///home/cloudera/imdb/Movie-Ratings-Done.data")

movieFormatted= movie.map(format0)
ratingFormatted= rating.map(format1)
dataM = movieFormatted.take(movieFormatted.count())
dataR =  ratingFormatted.collect()
#golden = movieFormatted.filter(findMovie)
#match = rdd.union
#out = dataM.collect()
movietitle = "GoldenEye (1995)"

movieID = movieFormatted.filter(lambda n: n[1] == movietitle).map(lambda x: x[0]).collect()
#if (dataM[2][1] == "GoldenEye (1995)"):
#	print "found"
#	movieF= []
ID = movieID[0]
review = ratingFormatted.filter(lambda n: n[1] == ID).filter(lambda n: n[2] == "5").count()
	#print len(list2)
print "amount of 5* reviews", review		
		
#	movieF.append(dataM[2][0])
#print movieF

#tordd = sc.parallelize(movieF)
#join = movieID.intersection(ratingFormatted).collect()
#x = join.take(5)
#out = join.collect()
#print join
#how many 5* golden eye has