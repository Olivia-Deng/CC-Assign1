#!/usr/bin/python3


import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin)
        Input format:  key \t value (category \t video_id, country)
        """
    for line in file:
        temp = line.strip().split("\t", 1)
        category = temp[0]
        video_id = temp[1].strip().split(",")[0]
        country = temp[1].strip().split(",")[1]
        yield category, video_id, country

def tar_reducer():
    """ This reducer reads in (category \t video_id, country) key-value pairs which key is category,
        value is video_id and country, and returns the total average country number for videos in
        certain category by count the number of the country which the videos appear divide the
        total number of videos with different ID.
        """
    # Set a dictionary which named id_country to used to store the the correspondence between video_id and country
    current_category = ''
    id_country = {}

    for category, video_id, country in read_map_output(sys.stdin):
        # Filter out the header
        if category == "category":
            continue
        # Store a kind of category
        if current_category == '':
            current_category = category
        if current_category != category:
            # Count the number of video_id
            countID = len(id_country)
            countCountry = 0
            for i in id_country:
                countCountry += len(id_country[i])
            print(current_category,':','%.2f'%(countCountry/countID))
            # Clean the dictionary for the next category
            current_category = category
            id_country = {}
        if video_id not in id_country:
            id_country[video_id] = []
        if country not in id_country[video_id]:
            id_country[video_id].append(country)

    # Output format: current_category: countCountry/countID
    countID = len(id_country)
    countCountry = 0
    for i in id_country:
        countCountry += len(id_country[i])
    print(current_category,':','%.2f'%(countCountry/countID))

        
if __name__ == '__main__':
    tar_reducer()
