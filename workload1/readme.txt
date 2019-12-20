### Python for Workload1

This folder contains two python scripts (*mapper.py*, *reducer.py*) implementing the map and the reduce function respectively,
    and execution script (*run.sh*) of this MapReduce job to run it on EMR.

About environment: AWS EMR with emr-5.21.0 software release

mapper.py is designed to extracting category, video_id, and country information from input line using string manipulation methods,
    and convert to key/value pair:(category, {video_id, country}) to output

reducer.py received the key/value output from mapper which sorted by key: category. A dictionary is created to store the
    correspondence between video_id and country, and count the number of the video and the country they appeared each to
    get the total average country number for videos in certain category. The output is current_category: countCountry/countID.

run.sh is to run it on EMR.
    The following command to run is:
        ./run.sh [input_path] [output_path]
        Eg. When I save the files which contains AllVideos_short.csv, mapper.py, reducer.py and run.sh under the directory of workload1,
        which under the directory of hadoop, the command should be:
        ./run.sh file:///home/hadoop/workload1/AllVideos_short.csv file:///home/hadoop/workload1/output