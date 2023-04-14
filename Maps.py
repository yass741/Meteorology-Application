import matplotlib.pylab as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset
import matplotlib as mpl
import fenetre
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Vue_Globale
import tkinter as tk

mpl.rcParams['toolbar'] = 'None'


class MapTmin :
    def __init__(self, year, day, month):
        self.dataset = Dataset('./DataRepertory/tmin.{}.nc'.format(year), 'r')
        
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]
        self.times = self.dataset.variables["time"][:]
        self.vals = self.dataset.variables["tmin"][:]
        self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
        self.ax = plt.subplot(111, projection=ccrs.PlateCarree())
        self.c = self.ax.pcolormesh(self.lons,self.lats, self.vals[self.day_of_year], vmin=-25, vmax=20, transform=ccrs.PlateCarree(), cmap="jet")
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
    def displayMap(self):
        plt.colorbar(self.c,ax=self.ax,fraction=0.046,pad=0.04)
        plt.title("Températures minimales")
        plt.show()

class MapTmax:

        def __init__(self, year, day, month):
            self.dataset = Dataset('./DataRepertory/tmax.{}.nc'.format(year), 'r')
            self.lats = self.dataset.variables["lat"][:]
            self.lons = self.dataset.variables["lon"][:]
            self.times = self.dataset.variables["time"][:]
            self.vals = self.dataset.variables["tmax"][:]
            self.ax = plt.subplot(111, projection=ccrs.PlateCarree())
            self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
            self.c = self.ax.pcolormesh(self.lons,self.lats, self.vals[self.day_of_year], vmin=15, vmax=50, transform=ccrs.PlateCarree(), cmap="jet")
            self.ax.coastlines(resolution='110m')
            self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
            self.ax.add_feature(cfeature.LAND.with_scale('50m'))
            self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
        def displayMaptmax(self, day, month, year):
            plt.colorbar(self.c,ax=self.ax,fraction=0.046,pad=0.04)
            plt.title("Températures maximales {0}/{1}/{2}".format(str(day),str(month),str(year)))
            plt.show()
class MapPrecip:

        def __init__(self, year, day, month):
            self.dataset = Dataset('./DataRepertory/precip.{}.nc'.format(year), 'r')
            self.lats = self.dataset.variables["lat"][:]
            self.lons = self.dataset.variables["lon"][:]
            self.times = self.dataset.variables["time"][:]
            self.vals = self.dataset.variables["precip"][:]
            self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
            self.ax = plt.subplot(111, projection=ccrs.PlateCarree())
            self.c = self.ax.pcolormesh(self.lons,self.lats, self.vals[self.day_of_year], vmin=0, vmax=12, transform=ccrs.PlateCarree(), cmap="jet")
            self.ax.coastlines(resolution='110m')
            self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
            self.ax.add_feature(cfeature.LAND.with_scale('50m'))
            self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
        def displayMap(self):
            plt.colorbar(self.c,ax=self.ax,fraction=0.046,pad=0.04)
            plt.title("Précipitations")
            plt.show()