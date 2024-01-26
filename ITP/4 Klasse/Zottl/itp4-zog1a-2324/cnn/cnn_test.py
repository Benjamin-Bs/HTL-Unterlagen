# PROGRAMM ZUM TESTEN DER DATEN!
# MODELL IST ERFORDERLICH

from keras.models import load_model
import numpy as np
from keras.preprocessing import image

# Pfad zur HDF5-Datei des trainierten Modells
modell_pfad = './../Models/model_from_video_trained.h5'

# Laden des Modells
geladenes_modell = load_model(modell_pfad)

bild_pfad = '/Users/suad/Schule/ITP/ZOG/ITP4-ZOG1a-2324/Trainingsdaten/Schlapfen/Schlapfen10.png'



img = image.load_img(bild_pfad, target_size=(256, 256))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalisieren der Pixelwerte auf den Bereich [0, 1]

vorhersage = geladenes_modell.predict(img_array)

if vorhersage[0][0] > 0.9:
    print(" nein Schlapfen")
else:
    print("schlapfen")