from tkinter import *
import tkinter
from tkinter import ttk
from numpy import *
from DatasetManip import *
import Maps
import Graphics

class lafenetre () :

    def __init__(self):
        self.fenetre = Tk()

        
        self.fenetre.geometry("1000x900")

        self.frame = Frame(self.fenetre)

        self.frame.grid(row = 0, column = 0)

        
        self.annee_selectionnee = 2010
        self.jour = 0
        self.mois = 0
        self.lat = 89.75
        self.lon = 0.25

         

        self.rep_annees = Entry(self.fenetre)
        
        self.rep_annees.grid(row=0, column=0,padx = 3, pady =3)

        self.annees = Label(self.fenetre, text= "Annnée")
        self.annees.grid(row=0, column=10,padx =4, pady = 4)

        self.Charger = Button(self.frame, text = "Charger", command = lambda : [self.maj_annee_selectionnee(),self.chargerlafenetre()])
        self.Charger.grid(row = 0, column = 20,padx= 7, pady =7)

        self.longitude = Entry(self.frame)

        self.notebook = ttk.Notebook(self.fenetre)
        self.notebook.grid(row = 140, column = 0)

        self.frame_globale = ttk.Frame(self.notebook, height = 500, width = 1000 )
        self.frame_globale.pack( fill = "both", expand = True)
        

        self.frame_locale = ttk.Frame(self.notebook, height = 500, width = 1000 )
        self.frame_locale.pack( fill = "both", expand = True)

        self.Latitude = ttk.Entry(self.frame_locale)
        self.Latitude.pack(pady = 5, padx = 5)
        self.Lat = ttk.Label(self.frame_locale, text= "Latitude")
        self.Lat.pack(pady = 5, padx = 5)

        self.Longitude = ttk.Entry(self.frame_locale)
        self.Longitude.pack(pady=5,padx=5)
        self.Longit = ttk.Label(self.frame_locale, text= "Longitude")
        self.Longit.pack(pady = 5, padx = 5)

        

        self.AfficherGrapheTemperaturesMaximales = ttk.Button(self.frame_locale, text= "Afficher Températures maximales", command = lambda : [self.maj_lat_selectionnee(), self.maj_lon_selectionnee(), Graphics.GrapheTmax(self.annee_selectionnee, self.lon, self.lat).DisplayGraph(self.annee_selectionnee)] )
        self.AfficherGrapheTemperaturesMaximales.pack(pady = 5, padx = 5)

        self.AfficherGrapheTemperaturesMinimales = ttk.Button(self.frame_locale, text= "Afficher Températures minimales", command = lambda : [self.maj_lat_selectionnee(), self.maj_lon_selectionnee(), Graphics.GrapheTmin(self.annee_selectionnee, self.lon, self.lat).DisplayGraph(self.annee_selectionnee)] )
        self.AfficherGrapheTemperaturesMinimales.pack(pady = 5, padx = 5)

        self.AfficherGraphePrecip = ttk.Button(self.frame_locale, text= "Afficher les precipitations", command = lambda : [self.maj_lat_selectionnee(), self.maj_lon_selectionnee(), Graphics.GraphePrecip(self.annee_selectionnee).DisplayGraph(self.annee_selectionnee, self.lon, self.lat)] )
        self.AfficherGraphePrecip.pack(pady = 5, padx = 5)

        self.locale_notebook = ttk.Notebook(self.frame_globale)
        self.locale_notebook.pack(side = "top", expand= True)


        self.par_jour = ttk.Frame(self.locale_notebook, height = 200 , width = 400)
        self.par_jour.pack(fill = "both", expand = True, anchor = "center")

        self.Day = ttk.Entry(self.par_jour)
        self.Day.pack(pady=5,padx=5)
        self.day = ttk.Label(self.par_jour, text= "Jour")
        self.day.pack(pady=5,padx=5)

        self.Month = ttk.Entry(self.par_jour)
        self.Month.pack(pady=5,padx=5)
        self.month = ttk.Label(self.par_jour, text= "Mois")
        self.month.pack(pady=5,padx=5)       


        

        # self.donnees_text = Label(self.par_jour,text = "Données")
        # self.donnees_text.pack(side = "left", padx = 5, pady = 5)


        # self.donnees_jour = ttk.Combobox(self.par_jour, values = ["Températures minimales", "Températures maximales", "Précipitations"])
        # self.donnees_jour.pack(side = "left", padx = 5, pady = 5)
        
        self.afficherTmin = ttk.Button(self.par_jour, text= "afficher les temperatures minimales", command = lambda : [self.maj_jour(), self.maj_mois(),Maps.MapTmin(self.annee_selectionnee, self.jour, self.mois).displayMap()] )
        self.afficherTmin.pack()

        self.afficherTmax = ttk.Button(self.par_jour, text= "afficher les températures maximales", command = lambda :[self.maj_jour(), self.maj_mois(),Maps.MapTmax(self.annee_selectionnee,self.jour, self.mois).displayMaptmax(self.jour, self.mois, self.annee_selectionnee)] )
        self.afficherTmax.pack()

        self.afficherPrecip = ttk.Button(self.par_jour, text= "afficher les precipitations", command = lambda :[self.maj_jour(), self.maj_mois(),Maps.MapPrecip(self.annee_selectionnee,self.jour, self.mois).displayMap()] )
        self.afficherPrecip.pack()        
        self.par_mois = ttk.Frame(self.locale_notebook, height = 200, width = 400)
        self.par_mois.pack(fill = "both", expand = True, anchor = "center")
    

        

        self.locale_notebook.add(self.par_jour, text = "Par jour")
        self.locale_notebook.add(self.par_mois, text = "Par mois")


        self.notebook.add(self.frame_globale, text="Vue globale")
        self.notebook.add(self.frame_locale, text="Courbe locale")

        
    def anneeChoisi(self):
        self.annee_selectionnee = self.rep_annees.get() 
        return int(self.annee_selectionnee)
             

    def chargerlafenetre(self):
        self.fenetre.mainloop() 
        
                        
    def donnesChoisisJour(self):
        donneeJour = self.Day.get()
        return int(donneeJour)
    
    def maj_jour(self):
        self.jour = self.donnesChoisisJour()
        print(self.jour)

    def donnesChoisismois(self):
        donneeMois = self.Month.get()
        return int(donneeMois)

    def maj_mois(self):
        self.mois = self.donnesChoisismois()
        print(self.mois)


    def maj_annee_selectionnee(self):
        self.annee_selectionnee = self.anneeChoisi()
        print(self.annee_selectionnee)

    def lonChoisi(self) :
        self.lon = self.Longitude.get()
        return self.lon
    
    def maj_lon_selectionnee(self):
        self.lon = self.lonChoisi()
        print(self.lon)
    
    def latChoisi(self):
        self.lat = self.Latitude.get()
        return self.lat

    def maj_lat_selectionnee(self):
        self.lat = self.latChoisi()
        print(self.lat)

    
    
    
    
         
    

