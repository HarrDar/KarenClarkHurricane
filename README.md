# Harrison Darbin - Karen Clark & Co. Home Coding Project
Thank you for the opportunity to show my coding to the team! I had a lot of fun being able to work with even just a little bit of the data, and it left me wanting to do much more with it, so I fleshed out every part of it that I could! But for simplicity I still just kept it to the landfall statistics as requested.\
The simple breakdown is, after reading and organizing the HURDAT2 data, I also load in a GeoJSON file with a 'polygon' of Florida. Then converting that geography data to a polygon shape object, we can easily check if any point is contained with in, so we step through each hurricane's readings until we find one. This should run in O(n) where n is the number of readings, since in the worst case where nothing hits, we check every reading. I am not qualified enough to program judgement calls as to whether a hurricane will ever reach Florida, so checking every step of their paths felt like the only safe option.\
The GeoJSON polygons were also constructed somewhat crudely in the interest of time (coastlines are generally within ~1 mile for Florida, ~10 miles for Mass, Yucatan & Bermuda, and they are wildly inaccurate for North America. That one was just for fun.), and I assumed landfall did not include islands, though I did include barrier islands.
### Required Packages
geojson\
shapely
## File Breakdown
generateReport.py - What to run for the actual given assignment. Script that links everything together to generate the report file. Arguments given below. \
storm.py - Contains functions & classes for reading in HURDAT data sets.\
geo.py - Contains functions & classes for reading in and comparing location data.\
report.py - Opens stream for reports and formats strings to fit in reports.\
data/ - Input data to be used\
&emsp;[data].txt - Expected text files to be read in as storm data.\
&emsp;[location].geojson - Expected 'GeoJSON' files to be read in as location data.\
reports/ - Where output will be generated.\
&emsp;[locationReport].txt - Report generated for given location.
## generateReport
Running generateReport will create a report of what hurricanes made landfall in the given location, defaulting to Florida. The input data, location data, and report location can be customized with flags. The hurricane and location data must be placed in the data folder, and the report will always generate in the reports folder. All the flags are as follows:\
&emsp;-def - Use all "default" values (those asked for in the assignment). The script does this automatically, but this can be set to be shown explicitly.\
&emsp;-h - Set the hurricane data file, 'hurdat2.txt' by default. Text files are expected.\
&emsp;-l - Set the location data file, 'florida.geojson' by default. GeoJSON files are expected.\
&emsp;-r - Set the report file, 'FloridaReport.txt' by default. This will overwrite an existing file.\
&emsp;-d - Set the starting year, 1900 by default. A hurricane is included in a given year if it has any activity in that year, even if the landfall was in a previous year.\
&emsp;-p - Set report output to print to console instead, useful for debugging.\
I.E.\
```python3 generateReport.py -h hurdat2.txt -l bermuda.geojson -r BermudaReport.txt -d 1999```\
```python3 generateReport.py -def -p```\
or even just ```python3 generateReport.py``` for the default (requested) report!\
