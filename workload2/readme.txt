### Python for Workload2

This folder contains two python scripts (*CTV.py*, *ml_utils.py*) implementing calculating
    the dislikes growth of each video in each country,
    and execution script (*run.sh*) of this MapReduce job to run it on EMR.

About environment: AWS EMR with emr-5.21.0 software release

CTV.py is designed to how to realize the calculation in detailed.
    The sequence of the transformations and actions are written in it.
    First, the AllVideos_short.csv is read in the format of RDD and mapped to create
    ((video_id+country), (trending_date, likes, dislikes, category))RDD pair with
    filtering out the headers. Then GroupByKey transformation is used to group the value
    to the same key. Sorting by time sequence and calculating the dislikes growth by using
    mapValues transformation. During calculating, we set the growth is 0 whose videos’
    trending date are less than two date. Change to a new RDD pair which the key is growth
    through a map transformation.Using SortByKey transformation to sort RDD pair in descending
    order by the key: growth and then get the top 10 of the dislikes growth. Finally, a
    parallelize transformation is used to convert to RDD and change the format to suitable
    for requirements of assignment and use an action named saveAsTextFile to save the result.

ml_utils.py includes a few functions used in calculating the dislikes growth of each video in each country
    They are described as follow:

    extractKey(record)
    converts entries of AllVideos_short.csv into key,value pair of the
    following format ((video_id, country), (trending_date, likes, dislikes, category))

    calGrowth(line)
    sort trending_date in sequence by time firstly, and then calculate the dislikes growth of each video in each country

    extractGrowth(line)
    change to a new key: growth, and new value: (video_id, country, category)

    extractFormat(line)
    change the format which is suitable for requirements

run.sh is to run it on EMR.
    The following command to run is:
        ./run.sh [input_path] [output_path]
        Eg. When I save the files which contains AllVideos_short.csv, CTV.py, ml_utils.py and run.sh under the
        directory of workload2, which under the directory of hadoop, the command should be:
        ./run.sh file:///home/hadoop/workload2/ file:///home/hadoop/workload2/output