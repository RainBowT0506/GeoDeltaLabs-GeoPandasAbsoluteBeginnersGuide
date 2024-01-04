import geopandas as gpd
import matplotlib.pyplot as plt

# Importing an ESRI Shapefile and plotting it using GeoPandas
districts = gpd.read_file(r'.\Shapefiles\districts.shp')
districts.plot(cmap = 'hsv', edgecolor = 'black', column = 'district')
plt.title('Districts Plot')
plt.show()

area_of_interest = gpd.read_file(r'.\Shapefiles\area_of_interest.shp')
area_of_interest.plot()
plt.title('Area of Interest Plot')
plt.show()

atms = gpd.read_file(r'.\Shapefiles\atms.shp')
# Plot the figures side by side
fig, (ax1, ax2) = plt.subplots(nrows = 2, figsize = (10,8))
districts.plot(ax = ax1, cmap = 'hsv', edgecolor = 'black', column = 'district')
area_of_interest.plot(ax = ax2, color = 'green')
plt.suptitle('Districts and Area of Interest Plot')
plt.show()