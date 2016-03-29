# FormatTime.py - works with ArcGIS for Desktop 10.3.1 and 10.4

# This tool reformats a single datetime field from  M/DD/YYYY HH:MM:SS AM format to YYYY/MM/DD HH:MM:SS AM for a featureclass

# Reads a string from a field called "StartTime" (text) in a M/DD/YYYY HH:MM:SS AM format and
# writes to an different existing field called "StartTimeNew" (text) in a YYYY/MM/DD HH:MM:SS AM format
# The time slider tool needs the date in this format, thus this script



# To use
# - make sure your date field is in the format M/DD/YYYY in one field and your time field is in a separate field in HH:MM:SS AM
# - you want these to be in one field together
# - Add a new field called StartTime (text) to your featureclass
# - If not in one field, using the field calculator in ArcGIS, append your date and time using [date field] & " " & {time field}
# - Add a new field called StartTimeNew (text) to your featureclass to hold the new calculation that this script will perform
# - edit the path below to the feature class (not table) that contains the above fields
# - run in the python program that is installed standalone with ArcGIS
# - Line 39 and 41 control the input and output formatting, you could change this any time format

import arcpy, os

from datetime import datetime

# Input variables
# featureclass
pFeatureClass = arcpy.GetParameterAsText(0) 

#parameters for field names
pStartTimeField = arcpy.GetParameterAsText(1)
pStartTimeFieldNew = arcpy.GetParameterAsText(2)

rows = arcpy.UpdateCursor(pFeatureClass)
print("start")

for row in rows:
   
    #print(row.getValue("StartTime"))
    StartDateObject = datetime.strptime(row.getValue(pStartTimeField), "%m/%d/%Y %I:%M:%S %p") # ie M/DD/YYYY HH:MM:SS AM
    
    newStartDateStr = StartDateObject.strftime("%Y/%m/%d %I:%M:%S %p") # ie YYYY/MM/DD HH:MM:SS AM
    row.setValue(pStartTimeFieldNew, newStartDateStr)
    #print(newdateStr)
                                                       
    rows.updateRow(row)
    
# Delete cursor and row objects to remove locks on the data
del row
del rows

print("done")


 
