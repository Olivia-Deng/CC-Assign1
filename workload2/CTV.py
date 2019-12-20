from pyspark import SparkContext
from ml_utils import *
import argparse


if __name__ == "__main__":
    sc = SparkContext(appName="Controversial Trending Videos Identification")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='')
    parser.add_argument("--output", help="the output path",
                        default='CTV_out_script')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output


    allVideos = sc.textFile(input_path + "AllVideos_short.csv")
    # The filter is to filter out the headers
    trendingVideos = allVideos.map(extractKey).filter(lambda x:len(x)>1).groupByKey()
    growthOfVideos = trendingVideos.mapValues(calGrowth).map(extractGrowth)
    result = growthOfVideos.sortByKey(ascending=False)
    # Because the return of take(10) is a list, parallelize will be used to convert list to RDD
    result = result.take(10)
    resultRDD = sc.parallelize(result)
    resultFormat = resultRDD.map(extractFormat)
    resultFormat.saveAsTextFile(output_path)
