#%%
# Imports 

import pathlib 
import pandas as pd 
import geopandas as gp 
ppm_pathfile = pathlib.Path("00_raw_data", "Strato101431_261014_150508.txt")
kml_pathfile = pathlib.Path("00_raw_data", "Strato101431_261014_150508map.kml")
ppm_data = pd.read_csv(ppm_pathfile)

# %%
# Geopandas user guide:  https://geopandas.org/en/stable/getting_started/introduction.html
# Medium article: https://medium.com/@nouhailadraidar1/a-beginners-guide-to-handling-geospatial-data-using-python-79c20106167e
# Load file: 
strato_test = gp.read_file(kml_pathfile, driver = "libkml")
# Data exploration: 
print(strato_test.head())
print("Number of rows & columns in dataframe:", strato_test.shape)
print("Column Names:", strato_test.columns)
print(strato_test.info())

#%% 
# Plot points 
strato_test.plot()


# %% View data 
# view data: 

ppm_data.columns

# # Output: Index(['Time Stamp', 'Inlet Number', 'P (mbars)', 'T0 (degC)', 'T5 (degC)',
#        'Tgas(degC)', 'CO2 (ppm)', 'H2O (ppm)', 'N2O (ppm)',
#        'Battery Charge (V)', 'Power Input (mV)', 'Current (mA)', 'SOC (%)',
#        'Latitude', 'Longitude'],
#       dtype='object') 
#%%
# from ppm_data, plot lat/long and color = CO2 

# Column sof interest: 'CO2 (ppm)', 'N2O (ppm)', 'Latitude', 'Longitude'
import matplotlib.pyplot as plt 

ax1 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "CO2 (ppm)", colormap = "viridis")

ax2 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "N2O (ppm)", colormap = "viridis")
