import csv
from operator import itemgetter


"""
This module includes a few functions used in calculating 
the dislikes growth of each video in each country
"""

def extractKey(record):
    """ This function converts entries of AllVideos_short.csv into key,value pair of the following format
        ((video_id+country), (trending_date, likes, dislikes, category))
        Args:
            record (str): A row of CSV file, with 12 columns separated by comma
        Returns:
            The return value is a tuple ((video_id+country), (trending_date, likes, dislikes, category))
        """
    try:
        temp = record.strip().split(",")

        video_id = str(temp[0].strip())
        category = str(temp[3].strip())
        t1 = '20' + temp[1].strip()
        t1 = t1.split('.')
        trending_date = int(t1[0] + t1[2] + t1[1])
        likes = int(temp[6].strip())
        dislikes = int(temp[7].strip())
        country = str(temp[11].strip())
        return ((video_id + country), (trending_date, likes, dislikes, category))

    except:
        return ()


def calGrowth(line):
    """ This function sort trending_date in sequence by time firstly,
        and then calculate the dislikes growth of each video in each country
        Args:
            line: Values in an iterable ({trending_date1, likes1, dislikes1, category1},
            {trending_date2, likes2, dislikes2, category2}, ...)
        Returns:
            The return value is a tuple (current_growth, current_category)
        """

    date = list(line)
    date = sorted(date, key=lambda x:x[0])

    if len(date) == 1:
        return (0, date[0][3])
    growth = (date[1][2] - date[0][2]) - (date[1][1] - date[0][1])
    return (growth, date[0][3])


def extractGrowth(line):
    """ This function is to change to a new key: growth, and new value: (video_id, country, category)
        Args:
            line (str): A tuple of (video_id+country), (current_growth, current_category)
        Returns:
            The return value is a tuple ((growth), (video_id, country, category))
        """
    id_country = line[0]
    growth = line[1][0]
    category = line[1][1]
    country = id_country[-2:]
    video_id = id_country[:-2]

    return (growth, (video_id, country, category))

def extractFormat(line):
    """ This function is to change the format which is suitable for requirements
        Args:
            line (str): A tuple of ((growth), (video_id, country, category))
        Returns:
            The return value is (video_id, growth, category, country)
        """
    growth = line[0]
    video_id = line[1][0]
    country = line[1][1]
    category = line[1][2]

    return video_id, growth, category, country
