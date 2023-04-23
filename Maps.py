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
import numpy as np

mpl.rcParams['toolbar'] = 'None'


class MapTmin :
    def __init__(self, year, day, month):
        self.dataset = Dataset('./DataRepertory/tmin.{}.nc'.format(year), 'r')
        
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]
        self.times = self.dataset.variables["time"][:]
        self.vals = self.dataset.variables["tmin"][:]
        self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, self.vals[self.day_of_year], vmin=-15, vmax=30, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
      
    def displayMap(self, frame):
       
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)
            

class MapTmax:

    def __init__(self, year, day, month):
        self.dataset = Dataset('./DataRepertory/tmax.{}.nc'.format(year), 'r')
        
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]
        self.times = self.dataset.variables["time"][:]
        self.vals = self.dataset.variables["tmax"][:]
        self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, self.vals[self.day_of_year], vmin=15, vmax=50, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))

    def displayMap(self, frame):
      
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)
class MapPrecip:

    def __init__(self, year, day, month):
        self.dataset = Dataset('./DataRepertory/precip.{}.nc'.format(year), 'r')
        
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]
        self.times = self.dataset.variables["time"][:]
        self.vals = self.dataset.variables["precip"][:]
        self.day_of_year =Vue_Globale.Date.ConversionDate(year, day, month)
        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, self.vals[self.day_of_year], vmin=0, vmax=20, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
   
    def displayMap(self, frame):
        
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)
            
class MonthlyMap():
    def __init__(self, mois, year, typeDonnee):
        self.dataset = Dataset(f'./DataRepertory/{typeDonnee}.{year}.nc', 'r')
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]  

        if(typeDonnee == 'precip'):
            Vmin = 0
            Vmax = 20
        if (typeDonnee == 'tmax'):
            Vmin = -2
            Vmax = 50
        if(typeDonnee == 'tmin'):
            Vmin = -50
            Vmax = 30

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection=ccrs.PlateCarree())
        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, Vue_Globale.ChargerValues(mois,year, typeDonnee), vmin=Vmin, vmax=Vmax, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
        plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    def displayMap(self, frame):
        
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)

class MaxValueMap():
    def __init__(self,TypeDonnee, year) :
        self.dataset = Dataset(f'./DataRepertory/{TypeDonnee}.{year}.nc', 'r')
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]     
        self.times = self.dataset.variables["times"][:]
        self.vals = self.dataset.variables[TypeDonnee][:]

        if(TypeDonnee == 'precip'):
            Vmin = 0
            Vmax = 20
        if (TypeDonnee == 'tmax'):
            Vmin = -2
            Vmax = 50
        if(TypeDonnee == 'tmin'):
            Vmin = -50
            Vmax = 30

        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, self.vals[Vue_Globale.TrouverValMax(self.vals)], vmin=Vmin, vmax=Vmax, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
   
    def displayMap(self, frame):
        
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)

class MinValueMap():
    def __init__(self,TypeDonnee, year) :
        self.dataset = Dataset(f'./DataRepertory/{TypeDonnee}.{year}.nc', 'r')
        self.lats = self.dataset.variables["lat"][:]
        self.lons = self.dataset.variables["lon"][:]     
        self.times = self.dataset.variables["time"][:]
        self.vals = self.dataset.variables[TypeDonnee][:]

        if(TypeDonnee == 'precip'):
            Vmin = 0
            Vmax = 20
        if (TypeDonnee == 'tmax'):
            Vmin = -2
            Vmax = 50
        if(TypeDonnee == 'tmin'):
            Vmin = -50
            Vmax = 30

        self.fig, self.ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': ccrs.PlateCarree()})
        self.c = self.ax.pcolormesh(self.lons, self.lats, self.vals[Vue_Globale.TrouverValMin(self.vals)], vmin=Vmin, vmax=Vmax, transform=ccrs.PlateCarree(), cmap="jet")
        self.fig.colorbar(self.c, ax=self.ax, shrink=0.5)
        self.ax.coastlines(resolution='110m')
        self.ax.add_feature(cfeature.OCEAN.with_scale('50m'))
        self.ax.add_feature(cfeature.LAND.with_scale('50m'))
        self.ax.add_feature(cfeature.BORDERS.with_scale('50m'))
   
    def displayMap(self, frame):
        
        canvas = FigureCanvasTkAgg(self.fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 0, y =100)
