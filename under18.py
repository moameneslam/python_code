from pyspark import SparkConf, SparkContext
import math

def format0(rec):
	Record = rec.split("|")
	return(Record)

def format1(rec):	
	Record = rec.split("\t")
	return(Record)

def ageToInt(rec):
	record = (rec[0], int(rec[1]))
	return record


con = SparkConf()
sc = SparkContext(conf = con)

movie=sc.textFile("file:///home/cloudera/imdb/Movies.item", use_unicode=True)
rating=sc.textFile("file:///home/cloudera/imdb/Movie-Ratings-Done.data")
user = sc.textFile("file:///home/cloudera/imdb/Users.txt")

userFormatted =user.map(format0)
movieFormatted= movie.map(format0)
ratingFormatted= rating.map(format1)
dataM = movieFormatted.take(movieFormatted.count())
dataR =  ratingFormatted.collect()
#golden = movieFormatted.filter(findMovie)
#match = rdd.union
#out = dataM.collect()
#get rid of headers
header = userFormatted.first()
users = userFormatted.filter(lambda row: row != header).map(ageToInt).filter(lambda n: n[1] <= 18).map(lambda n: n[0]).collect()

#movietitle = "GoldenEye (1995)"
genres =[['unknown', 5], ['Action', 6], ['Adventure', 7],  ['Animation', 8],  ['Childrens', 9], ['Comedy', 10], [ 'Crime', 11], ['Documentary', 12],  [ 'Drama', 13], ['Fantasy', 14],  ['Film-Noir', 15], ['Horror', 16], ['Musical', 17], ['Myster', 18], ['Romance', 19], ['Sci-Fi', 20], ['Thriller', 21], ['War', 22], ['Western', 23]]

for i in users:
	movieID = ratingFormatted.filter(lambda n: n[0] == i).map(lambda n: (n[0], n[1], n[2])).map(lambda n: (n[1], 1)).reduceByKey(lambda n,m: n[1]+m[1]+5).collect()

#movie = movieFormatted.filter().collect()
#for i in users:  reduceByKey(lambda n,m: n[0]+m[0])  
	#print i
	#out = ratingFormatted.filter(lambda n: n[0] == i).filter(lambda n: n[2] == "5").map(lambda n: n[1]).collect()
	#print out
#for i in movieFormatted:
#	out = movieFormatted.filter()
#or i in range (0, len(genres)):
	#print i
	#genrNum = movieFormatted.filter(lambda n: n[genres[i][1]] == "1").map(lambda n: n[1]).filter(lambda n: n == out).collect()

#	print  genrNum

print movieID
#ID = movieID[0]
#review = ratingFormatted.fitler(lambda n: n[1] == ID).filter(lambda n: n[2] == "5").count()
	#print len(list2)
#print action
		
#	movieF.append(dataM[2][0])
#print movieF

#tordd = sc.parallelize(movieF)
#join = movieID.intersection(ratingFormatted).collect()
#x = join.take(5)
#out = join.collect()
#print join
#how many 5* golden eye has