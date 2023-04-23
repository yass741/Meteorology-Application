import numpy as np
import matplotlib.pyplot as plt
from math import *
from netCDF4 import Dataset
import numpy.ma as ma
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# from geopy import distance

# différentes classes correspondants aux différents types de graphes utilisés pour le frame local

class Graph:
    def __init__(self, year, type_donnees):
        self.dataset = Dataset(f'./DataRepertory/{type_donnees}.{year}.nc', 'r')
        self.lats = self.dataset.variables['lat'][:]
        self.lons = self.dataset.variables['lon'][:]
        self.times = self.dataset.variables['time'][:]
        self.vals = self.dataset.variables[type_donnees][:]
        if(len(self.vals == 366)):
            self.times = np.arange(0, len(self.vals), 1)
        else:
            self.times = np.arange(0, len(self.vals), 1)
        self.valeurs = None

    def find_closest_zone_values(self, lat, lon, vals):
           
            lats = self.lats
            lons = self.lons
            
            distances = np.empty((len(lats), len(lons)))
            distances[:] = np.nan

           
            for i in range(len(lats)):  #this was a complicated calculation and python is pretty much slow, but, with geopy library a specific method to
                                            #calculate distances is available, but I didn't use it as I didn't know whether we have the right to use it
                row_distances = []
                for j in range(len(lons)):
                    a = pow(sin((float(lat)-float(lats[i]))/2),2) + cos(float(lat))*cos(float(lats[i]))*pow(sin(float(lon) - float(lons[j])/2),2)
                    c = 2*atan2(sqrt(a),sqrt(1-a))
                    R = 6373
                    row_distances.append(R*c)

                # dist = distance.distance(point1, point2).km
                # distances[i, j] = dist
                
                distances[i,:] = row_distances

           
            min_index = np.unravel_index(np.nanargmin(distances), distances.shape)               #we append the different distances between the unmasked zones and the one in the input
                                                                                                    # we then get the indexes of the unmasked zone that got the lowest distance
            print(vals.shape)

            
            while ma.is_masked(vals[0][min_index[0]][min_index[1]]):
                distances[min_index[0]][min_index[1]] = np.nan
                min_index = np.unravel_index(np.nanargmin(distances), distances.shape)

            return vals[:, min_index[0], min_index[1]]
        

class GraphePrecip(Graph):
    def __init__(self, year):
        super().__init__(year, 'precip')
        
    def DisplayGraph(self, year, lat, lon, frame, fig, gs):                 #on the contrary of the Maps, the matplotlib graphics were easier to display with 
        plt.close()
        plt.cla()
        plt.clf()
        plt.delaxes()
        daily_values = []
        self.valeurs = self.find_closest_zone_values(lat, lon, self.vals)
        for day_values in self.vals:
            daily_values.append(day_values.mean())

        plot = fig.add_subplot(gs[1,0])
        plot.set_xlabel("jours de l'année")
        plot.set_ylabel("précipitations  ")
        plot.plot(self.times, daily_values)       
        canvas = FigureCanvasTkAgg(fig, master=frame) 


        canvas.draw()
        canvas.get_tk_widget().place(x =0, y=50)

         




class GrapheT(Graph):
    def __init__(self, year):
        super().__init__(year, 'tmin')
        self.vals_tmax = None
        self.tmin_daily_values = []
        self.tmax_daily_values = []
        
    def DisplayGraph(self, year, lat, lon, frame, fig, gs):
        plt.close()
        plt.cla()
        plt.clf()
        plt.delaxes()
        dataset = Dataset(f'./DataRepertory/tmax.{year}.nc', 'r')
        self.valeurs = self.find_closest_zone_values(lat, lon, self.vals)
        self.vals_tmax = self.find_closest_zone_values(lat, lon, dataset.variables['tmax'][:])
        for day_values in self.valeurs:
            self.tmin_daily_values.append(day_values)
        for day_values in self.vals_tmax:
            self.tmax_daily_values.append(day_values)
        
        ax1 = fig.add_subplot(gs[0,0])
        ax1.set_xlabel("jours de l'année")
        ax1.set_ylabel("températures minimales")
        ax1.plot(self.times, self.tmin_daily_values)
        
        ax2 = ax1.twinx()
        ax2.set_ylabel("températures maximales")
        ax2.plot(self.times, self.tmax_daily_values, 'r')
        ax1.legend(['températures minimales'], loc='upper left')
        ax2.legend(['températures maximales'], loc='upper right')

        canvas = FigureCanvasTkAgg(fig, master=frame) 
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=50)
         


        
