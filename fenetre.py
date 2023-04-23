from tkinter import *
import matplotlib.pyplot as plt
from tkinter import ttk
from numpy import *
import Maps
import Graphics
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class lafenetre () :
    
    def __init__(self):                             #initialisation de la fenêtre principale
                                                    #les différentes variables que j'ai déclaré comme attributs de cette fenêtre
        self.fenetre = Tk()                        # nous permettront de gérer le code
        self.fenetre.geometry("1000x900")

        self.frame = Frame(self.fenetre)
        self.frame.place(x=0, y=0, width=1000, height=900)
        
        self.annee_selectionnee = 2010
        self.jour = 0
        self.mois = 0
        self.mois1 = 0
        self.lat = 89.75
        self.lon = 0.25
        self.Choice = IntVar()
        self.Choice.set(1)
       

        self.fig = Figure(frameon= True)
        self.gs = self.fig.add_gridspec(2,1)

        self.DonneesChoisisJour = None
        self.DonneesChoisirMois = None
        self.ChoiceMaxMin = None
        

        self.annees = ttk.Label(self.frame, text="Annnée")   #Implémentation des différentes widgets et frames de la fenetre
        self.annees.place(x=0, y=0)

        array = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

        self.rep_annees = ttk.Combobox(values=array)
        self.rep_annees.place(x=80, y=0)

        self.Charger = ttk.Button(self.frame, text="Charger", command=lambda: [self.maj_annee_selectionnee(), self.chargerlafenetre()])
        self.Charger.place(x=300, y=0)


        self.notebook = ttk.Notebook(self.frame, height =870, width = 1000)
        self.notebook.place(x=0,y=130)

        self.frame_globale = ttk.Frame(self.notebook, height = 870, width =1000)
        self.frame_globale.place(x=0,y=0)

        self.frame_locale = ttk.Frame(self.notebook, height = 870, width = 1000)
        self.frame_locale.place(x=0,y=0)
        self.latitudetext = ttk.Label(self.frame_locale, text ="Latitude:")
        self.latitudetext.place(x=0,y=0)
        self.Latitude = ttk.Entry(self.frame_locale)
        self.Latitude.place(x=50,y=0)
        self.longitudetext = ttk.Label(self.frame_locale, text = "Longitude:")
        self.longitudetext.place(x=240, y=0)
        self.Longitude = ttk.Entry(self.frame_locale)
        self.Longitude.place(x=310, y = 0)
        self.calculateButton = ttk.Button(self.frame_locale,text = "Effectuer les calculs", command = lambda :[self.display_temperature_graph(), self.display_precip_graph()])
        self.calculateButton.place(x= 500, y=0)
   

        self.notebook.add(self.frame_globale, text = "Vue Globale")
        self.notebook.add(self.frame_locale, text = "Courbe locale")
        
        self.notebook_global = ttk.Notebook(self.frame_globale, height = 870, width=1000 )
        self.notebook_global.place(x=0,y=0)

        self.frame_par_jour = ttk.Frame(self.notebook_global, height=870, width=1000)
        self.frame_par_jour.place(x=0,y=0)

        self.frame_par_mois = ttk.Frame(self.notebook_global, height =870, width = 1000)
        self.frame_par_mois.place(x=0, y=0)

        self.notebook_global.add(self.frame_par_jour, text = "par jour")
        self.notebook_global.add(self.frame_par_mois, text = "par mois" )

        # Par jour en globale
        self.date = ttk.Radiobutton(self.frame_par_jour, text= "date", variable= self.Choice, value = 1)
        self.date.place(x = 0,y =0)
        self.SaisiJour = ttk.Entry(self.frame_par_jour)
        self.SaisiJour.place(x=150, y=0)
        self.labelrandom = ttk.Label(self.frame_par_jour,text= "/")
        self.labelrandom.place(x=400, y= 0)
        self.SaisiMois = ttk.Entry(self.frame_par_jour)
        self.SaisiMois.place(x=550, y = 0)
        self.Charger_mapJour = ttk.Button(self.frame_par_jour, text="Afficher la carte", command = lambda: [self.displayMap(), self.displayMinMap()] )
        self.Charger_mapJour.place(x=700, y=0)
        self.TypeDonnees =ttk.Combobox(self.frame_par_jour, values = ["Températures maximales","Températures minimales","Précipitations"])
        self.TypeDonnees.place(x=850, y=25)
        self.Autre = ttk.Radiobutton(self.frame_par_jour, text = "autre", variable = self.Choice, value = 2)
        self.Autre.place(x=0,y=50)
        self.ChoiceMinMax = ttk.Combobox(self.frame_par_jour, values = ["Valeurs maximales", "Valeurs minimales"])
        self.ChoiceMinMax.place(x=50, y=50)

        #Par mois en Globale
        self.SaisiMois1 = ttk.Entry(self.frame_par_mois)
        self.SaisiMois1.place(x=40, y = 50)
        self.Charger_mapMois = ttk.Button(self.frame_par_mois, text="Afficher la carte", command = lambda: [ self.displayMonthMap()] )
        self.Charger_mapMois.place(x=190, y=50)
        self.TypeDonnees1 =ttk.Combobox(self.frame_par_mois, values = ["Températures maximales","Températures minimales","Précipitations"])
        self.TypeDonnees1.place(x=300, y=50)

# les fonctions ci-dessous servent à mettre à jour les atributs de la fenêtre selon l'input, recharger la fenêtre et afficher les représentations graphiques
    def chargerlafenetre(self):
        self.fenetre.mainloop() 

    def anneeChoisi(self):
        self.annee_selectionnee = self.rep_annees.get() 
        return int(self.annee_selectionnee)
    
    def maj_annee_selectionnee(self):
        self.annee_selectionnee = self.anneeChoisi()
        print(self.annee_selectionnee)      
                        
    def donnesChoisisJour(self):
        donneeJour = self.TypeDonnees.get()
        return donneeJour
    
    def majDonneesChoisisJour(self):
        self.DonneesChoisisJour = self.donnesChoisisJour()
        print(self.DonneesChoisisJour)

    def getterJour(self):
        jour = self.SaisiJour.get()
        return int(jour)
    
    def maj_jour(self):
        self.jour = self.getterJour()
        print(self.jour)

    def Choisismois(self):
        Mois = self.SaisiMois.get()
        # month = int(Mois)
        # if(month < 1):
        #     month = 1
        # elif(month> 12):
        #     month = 12
        return int(Mois)

    def maj_mois(self):
        self.mois = self.Choisismois()
        print(int(self.mois))




    def lonChoisi(self) :
        lon = self.Longitude.get()
       
        # if(lon > 90):
        #     while lon>90:
        #         lon = lon -90
        # elif(lon<-90):
        #     while lon <-90:
        #         lon = lon + 90
        return float(lon)
    
    def maj_lon_selectionnee(self):
        self.lon = self.lonChoisi()
        print(self.lon)
    
    def latChoisi(self):
        lat = self.Latitude.get()
        # lat = float(lat)
        # if(lat>180):
        #     while(lat > 180):
        #         lat = lat - 180
        # if(lat < -180):
        #     lat = lat + 180

        return lat

    def maj_lat_selectionnee(self):
        self.lat = self.latChoisi()
        print(self.lat)



    def display_precip_graph(self):
        
        self.maj_lat_selectionnee()
        self.maj_lon_selectionnee()
        graphe = Graphics.GraphePrecip(self.annee_selectionnee)
        graphe.DisplayGraph(self.annee_selectionnee, self.lat, self.lon, self.frame_locale, self.fig, self.gs)

    def display_temperature_graph(self):
       self.maj_lat_selectionnee()
       self.maj_lon_selectionnee()
       graphe = Graphics.GrapheT(self.annee_selectionnee)
    
       graphe.DisplayGraph(self.annee_selectionnee, self.lat, self.lon, self.frame_locale, self.fig, self.gs)


    def display_tmin_map(self):
      
         self.maj_jour()
         self.maj_mois()
         map = Maps.MapTmin(self.annee_selectionnee, self.jour, self.mois)
         map.displayMap(self.frame_par_jour)

    def display_tmax_map(self):
         
         self.maj_jour()
         self.maj_mois()
         map = Maps.MapTmax( self.annee_selectionnee, self.jour, self.mois)
         map.displayMap(self.frame_par_jour)

    def display_precip_map(self): 
           
         self.maj_jour()
         self.maj_mois()
         map = Maps.MapPrecip(self.annee_selectionnee, self.jour, self.mois)
         map.displayMap(self.frame_par_jour)


    def displayMap(self):
     
     choice_value = self.Choice.get()

     if(choice_value == 1):
        self.majDonneesChoisisJour()
        if(self.DonneesChoisisJour == "Températures minimales"):
            self.display_tmin_map()
        if(self.DonneesChoisisJour == "Températures maximales"):
            self.display_tmax_map()
        if(self.DonneesChoisisJour == "Précicipitations"):
            self.display_precip_map()

    def majMinMax(self):
       choix = self.ChoiceMinMax.get()
       return choix
    def updateChoiceMinMax(self):
        self.ChoiceMaxMin = self.majMinMax()
        print(self.ChoiceMaxMin)

    def displayMinMap(self):

        self.majDonneesChoisisJour()
        choix = None
        if(self.DonneesChoisisJour == "Températures minimales"):
            choix = 'tmin'
        if(self.DonneesChoisisJour == "Températures maximales"):
            choix = 'tmax'
        if(self.DonneesChoisisJour == "Précipitations"):
            choix = 'precip'

        map = Maps.MinValueMap(choix,self.annee_selectionnee)
        map.displayMap(self.frame_par_jour)
    def displayMaxMap(self):
        self.majDonneesChoisisJour()
        choix = None
        if(self.DonneesChoisisJour == "Températures minimales"):
            choix = 'tmin'
        if(self.DonneesChoisisJour == "Températures maximales"):
            choix = 'tmax'
        if(self.DonneesChoisisJour == "Précipitations"):
            choix = 'precip'
        map = Maps.MaxValueMap(choix,self.annee_selectionnee)
        map.displayMap(self.frame_par_jour)
    
    def displayMaxMinMap(self):
      self.updateChoiceMinMax()
      if(self.Choice == 2):
            if(self.ChoiceMaxMin == "Valeurs maximales"):
                self.displayMaxMap()
            if(self.ChoiceMaxMin == "Valeurs minimales") :
                self.displayMinMap() 

    def DonneesChoisiMoisGet(self):
        
        donnee = self.TypeDonnees1.get()
        if(donnee == "Températures minimales"):
            donnee = "tmin"
        elif(donnee == "Températures maximales"):
            donnee = "tmax"
        elif(donnee == "Précipitations"):
            donnee = "precip"
        return donnee
    

    def majDonneeChoisisMois(self):
        self.DonneesChoisirMois = self.DonneesChoisiMoisGet()
        print(self.DonneesChoisirMois)

    def MoisParMoisGet(self):
        Mois = self.SaisiMois1.get()
        
        return int(Mois)
    def majMoisParMoisGet(self):
        self.mois1 = self.MoisParMoisGet()
        print(self.mois1)

    def displayMonthMap(self):
        
        self.majDonneeChoisisMois()
        self.majMoisParMoisGet()
        Maps.MonthlyMap(self.mois1,self.annee_selectionnee,self.DonneesChoisirMois).displayMap(self.frame_par_mois)

    

    







