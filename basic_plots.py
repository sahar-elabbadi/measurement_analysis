#%%
import pathlib 
import pandas as pd # package for working with dataframes
import matplotlib.pyplot as plt # package for plotting 


# Path to the TXT file with Strato data
ppm_pathfile = pathlib.Path("00_raw_data", "Strato101431_261014_150508.txt")

# Load Strato data 
ppm_data = pd.read_csv(ppm_pathfile)

# Make scatter plot of CO2 data 
ax1 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "CO2 (ppm)", colormap = "viridis")

# Make scatter plot of N2O data 
ax2 = ppm_data.plot.scatter(
    x = "Longitude", y = "Latitude", c = "N2O (ppm)", colormap = "viridis")
