import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("gs://{SEU_BUCKET}/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    for i in range(10):    
      wd2 = wordCounts[i]
      wd2.saveAsTextFile("gs://{SEU_BUCKET}/resultado")
