# Import system modules
import arcpy

# Create gdb
geo_patch = "C:\Work\geotest"
geo_name = "MyGeo.gdb"

geo_gdb = arcpy.CreateFileGDB_management(geo_patch,geo_name)

# Set environment settings
arcpy.env.workspace = geo_patch

# Create Feature Class
arcpy.CreateFeatureclass_management(geo_name,"TestPoints","POINT","","DISABLED","DISABLED",arcpy.SpatialReference(4326))

# Create Name field
arcpy.AddField_management("TestPoints","Number","TEXT","","",30)

# Create dbf from excel
xls_name = "data.xls"
arcpy.ExcelToTable_conversion(xls_name, geo_name, "Sheet1")

# Copy dbf table to temp table
search_cursor = arcpy.da.SearchCursor("MyGeo.dbf", ["Num", "X", "Y"])

temp_list = []
for row in search_cursor:
    temp_list.append(row)

del search_cursor
# Copy point to Feature class
insert_cursor = arcpy.da.InsertCursor("C:\Work\geotest\MyGeo.gdb\TestPoints", ["Number", "SHAPE@X", "SHAPE@Y"])

for row in temp_list:
    insert_cursor.insertRow(row)

del temp_list
del insert_cursor
