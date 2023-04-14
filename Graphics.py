import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from netCDF4 import Dataset
import numpy as np
from math import *
import numpy.ma as ma

class GraphePrecip:
    def __init__(self, year):
        self.dataset = Dataset('./DataRepertory/precip.{}.nc'.format(year), 'r')
        self.lats = self.dataset.variables['lat'][:]
        self.lons = self.dataset.variables['lon'][:]
        self.times = self.dataset.variables['time'][:]
        self.vals = self.dataset.variables['precip'][:]
        self.times = self.times - 964248
        self.times = self.times / 24
        self.times = self.times - (int(year) - 2010)*350 # des calculs afin d'afficher sur l'axe des x les jours
                                                          #de manière visible et compréhensible
        self.times = self.times - 100

        
        
        self.valeurs = None



    def find_closest_zone_values(self, lat, lon, vals):
           
            lats = self.lats
            lons = self.lons
            
            distances = np.empty((len(lats), len(lons)))
            distances[:] = np.nan

           
            for i in range(len(lats)):
                row_distances = []
                for j in range(len(lons)):
                    a = pow(sin((float(lat)-float(lats[i]))/2),2) + cos(float(lat))*cos(float(lats[i]))*pow(sin(float(lon) - float(lons[j])/2),2)
                    c = 2*atan2(sqrt(a),sqrt(1-a))
                    R = 6373
                    row_distances.append(R*c)

                
                distances[i,:] = row_distances

           
            min_index = np.unravel_index(np.nanargmin(distances), distances.shape)
            print(vals.shape)

            
            while ma.is_masked(vals[0][min_index[0]][min_index[1]]):
                distances[min_index[0]][min_index[1]] = np.nan
                min_index = np.unravel_index(np.nanargmin(distances), distances.shape)

            return vals[:, min_index[0], min_index[1]]


        
    def DisplayGraph(self, year,lat, lon) :
            plt.close()
            daily_values = []
            self.valeurs = self.find_closest_zone_values(lat, lon, self.dataset.variables['precip'][:])
            for day_values in self.vals:
                daily_values.append(day_values.mean())

            plt.plot(self.times, daily_values)
            plt.xlabel("Jours de l'année")
            plt.ylabel("Précipitations (en mm)")
            plt.title("Evolution annuelle des Précipiutations dans la zone sélectionnée {}".format(year))
            plt.show()  


class GrapheTmin:
    def __init__(self, year, lon, lat):
        self.dataset = Dataset('./DataRepertory/tmin.{}.nc'.format(year), 'r')
        self.lats = self.dataset.variables['lat'][:]
        self.lons = self.dataset.variables['lon'][:]
        self.times = self.dataset.variables['time'][:]
        self.vals = self.dataset.variables['tmin'][:]
        self.times = self.times - 964248
        self.times = self.times / 24
        self.times = self.times - (int(year) - 2010)*350
        self.times = self.times - 50
        self.lat_id = np.abs(self.lats - float(lat)).argmin() 
       
        self.lon_id = np.abs(self.lons - float(lon)).argmin()
        
        self.valeurs = self.vals[:,self.lat_id, self.lon_id]
        
    def DisplayGraph(self, year) :
            plt.close()
            plt.plot(self.times, self.valeurs)
            plt.xlabel("Jours de l'année")
            plt.ylabel("Températures minimales (°C)")
            plt.title("Evolution annuelle des températures minimales dans la zone sélectionnée {}".format(year))
            plt.show()     
            self.times = self.dataset.variables['time'][:]   

class GrapheTmax:
    def __init__(self, year, lon, lat):
        self.dataset = Dataset('./DataRepertory/tmax.{}.nc'.format(year), 'r')
        self.lats = self.dataset.variables['lat'][:]
        self.lons = self.dataset.variables['lon'][:]
        self.times = self.dataset.variables['time'][:]
        self.vals = self.dataset.variables['tmax'][:]
        self.times = self.times - 964248
        self.times = self.times / 24
        self.times = self.times - (int(year) - 2010)*350
        self.times = self.times - 50


        self.lat_proche_id = np.abs(self.lats - float(lat)).argmin() 
       
        self.lon_proche_id = np.abs(self.lons - float(lon)).argmin()
        
        self.valeurs = self.vals[:,self.lat_proche_id, self.lon_proche_id]
        
    def DisplayGraph(self, year) :
            plt.close()
            plt.plot(self.times, self.valeurs)
            plt.xlabel("Jours de l'année")
            plt.ylabel("Températures maximales (°C)")
            plt.title("Evolution annuelle des températures maximales dans la zone sélectionnée {}".format(year))
            plt.show()  