#%%
# Imports 

import pathlib 
import pandas as pd 
import geopandas as gp 
ppm_pathfile = pathlib.Path("00_raw_data", "Strato101431_261014_150508.txt")
kml_pathfile = pathlib.Path("00_raw_data", "Strato101431_261014_150508map.kml")
ppm_data = pd.read_csv(ppm_pathfile)

# %% 1) Initialize data in GeoPandas

### First attempt: load KML file in geopandas 
# Geopandas user guide:  https://geopandas.org/en/stable/getting_started/introduction.html
# Medium article: https://medium.com/@nouhailadraidar1/a-beginners-guide-to-handling-geospatial-data-using-python-79c20106167e
# Load file: 
strato_test = gp.read_file(kml_pathfile, driver = "libkml")
# Data exploration: 
# print(strato_test.head())
print("Number of rows & columns in dataframe:", strato_test.shape)
print("Column Names:", strato_test.columns)
print(strato_test.info())

#%% 2) Plot data in Geopandas 

# Plot KML points using geopandas df 
strato_test.plot()


# %% 3) View data in the PPM file 

# Check columns: what data do we have? 
ppm_data.columns

# # Output: Index(['Time Stamp', 'Inlet Number', 'P (mbars)', 'T0 (degC)', 'T5 (degC)',
#        'Tgas(degC)', 'CO2 (ppm)', 'H2O (ppm)', 'N2O (ppm)',
#        'Battery Charge (V)', 'Power Input (mV)', 'Current (mA)', 'SOC (%)',
#        'Latitude', 'Longitude'],
#       dtype='object') 

####### Notes #######
# I checked and confirmed that Lat / Long data is present, first 2 minutes are missing. 
# Maybe we should let the instrument warm up for ~5 minutes before we start collecting data 
# We can don't need the KML file and can use the Lat/Long data in the .txt file for plotting lat/long
#  > Check: does the data we collected at Larry's field site include lat/long data? 


#%% 4) Make plots 
# from ppm_data, plot lat/long and color = CO2 

# Columns of interest: 'CO2 (ppm)', 'N2O (ppm)', 'Latitude', 'Longitude'
import matplotlib.pyplot as plt 

ax1 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "CO2 (ppm)", colormap = "viridis")

ax2 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "N2O (ppm)", colormap = "viridis")
