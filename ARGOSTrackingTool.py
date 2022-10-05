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
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
obs_lc = lineData[4]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude

# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

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
    
    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    
