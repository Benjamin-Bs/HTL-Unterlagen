# PROGRAMM ZUM MODELL ERSTELLEN!

import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator

import cv2

# Datenverzeichnis
train_dir = './../Trainingsdaten'
batch_size = 32
img_height = 256
img_width = 256

# Normalisierung
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Trainingsdaten laden
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',  # Hier wird die Klassenzuweisung automatisch wegen der Verzeichnissstruktur vorgenommen
    subset='training',
    classes=['Schlapfen', 'No_Schlapfen']
)

validation_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation',
    classes=['Schlapfen', 'No_Schlapfen']

)

# CNN-Modell
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#  trainieren
epochs = 150
history = model.fit(
    train_data,
    epochs=epochs,
    validation_data=validation_data
)

model.save("model_from_video_trained.h5")

