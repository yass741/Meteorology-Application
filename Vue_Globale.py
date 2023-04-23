import datetime
from netCDF4 import Dataset
import numpy as np

#des méthodes facilitant le déroulement des méthodes qui régissent la frame globale

class Date :

    def ConversionDate(year, day, month):
        date_obj = datetime.datetime(year=year, month=month, day=day)
        day_of_year = date_obj.timetuple().tm_yday

        return day_of_year
    

def ChargerValues(mois, year,typeDonnee):

    dataset = Dataset(f'./DataRepertory/{typeDonnee}.{year}.nc', 'r')

    vals = dataset.variables[typeDonnee][:]

    num_days_in_year = vals.shape[0]

    if num_days_in_year == 366:
        Nbjours_des_mois = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif num_days_in_year == 365:
        Nbjours_des_mois = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

    premierjour = sum(Nbjours_des_mois[:mois])
    dernierjour = sum(Nbjours_des_mois[:mois+1])



    vals_mois = vals[premierjour:dernierjour,:,:]

    if(typeDonnee == "tmin"):
        return np.min(vals_mois, axis=0)
    elif(typeDonnee == "tmax"):
        return np.max(vals_mois, axis=0)
    elif(typeDonnee == "precip"):
        return np.average(vals_mois, axis=0)

def TrouverValMax(vals):
        moyenne_jour = np.mean(vals, axis=(1,2))
        return np.argmax(moyenne_jour)


def TrouverValMin(vals):
        moyenne_jour = np.mean(vals, axis=(1,2))
        return np.argmin(moyenne_jour)
