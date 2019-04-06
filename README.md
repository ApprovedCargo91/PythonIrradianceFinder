# PythonIrradianceFinder
Uses Python to retrieve forecasted cloud cover data from the Dark Sky API and store it in a CSV file, then creates a gradient map of the cloud cover with respect to time and distance.

## Instructions
1. Put a Dark Sky API key in APIKey.txt as the only line.
2. Make sure csvMaker.py, csvGrapher.py, APIKey.txt, and your route data .txt file are in the same directory. Set the filename variable in csvMaker.py and csvGrapher.py to the name of your route data .txt file. This same name will be used when writing the CSV file.
3. Run csvMaker.py, then csvGrapher.py.

## Dependencies
You must have csv, datetime, requests, numpy, matplotlib, and scipy installed to use this code.

[![Powered by Dark Sky](https://darksky.net/dev/img/attribution/poweredby-oneline.png)](https://darksky.net/poweredby/)
