from netCDF4 import Dataset


class datasetTmin :


    def chargerDataset(annee):
        sett = Dataset(f'./DataRepertory/tmin.{annee}.nc')
        return sett

class datasetTmax:

    def chargerDataset(annee):
        sett = Dataset(f'./DataRepertory/tmax.{annee}.nc')
        return sett

class datasetPrecip:
        def chargerDataset(annee):
            sett = Dataset(f'./DataRepertory/precip.{annee}.nc')
            return sett