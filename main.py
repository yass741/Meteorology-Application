import fenetre 
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == "__main__":
   plt.close()
   mpl.rcParams['toolbar'] = 'None'   # just to make sure that the plots are being well initialized
   window = fenetre.lafenetre()   #window's initialization
   

   window.chargerlafenetre()   #window's refreshing
