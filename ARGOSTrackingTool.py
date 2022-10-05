#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Corey Halbert (corey.halbert@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

# %%

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY)")

#Create a variable pointing to the data file
file_name = 'raw/Sara.txt'

#Create a file object from the file
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#making dictionaries
date_dict = {}
location_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list:
    
    if lineString[0] in ('#','u'):
        continue
    
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    if obs_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    

#Create an empty key list
matching_keys = []

# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
    
