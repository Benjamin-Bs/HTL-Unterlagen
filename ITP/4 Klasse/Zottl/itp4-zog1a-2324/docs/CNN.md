# TensorFlow Klassifikationsmodell mit CNN - Code-Dokumentation

In diesem Codebeispiel wird ein Klassifikationsmodell für Bilder mithilfe von TensorFlow und dem Convolutional Neural Network (CNN) erstellt, trainiert und gespeichert. Das Modell wird auf Bilddaten angewendet, die in einem bestimmten Verzeichnis gespeichert sind.
Ein **Convolutional Neural Network (CNN)** ist ein spezialisiertes neuronales Netzwerk, das hauptsächlich für die Verarbeitung von Bildern. Genaueres unter https://www.tensorflow.org/tutorials/

## Importieren der Bibliotheken

```python
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.preprocessing.image import ImageDataGenerator



```

Die Parameter für das Training, wie das Verzeichnis der Trainingsdaten, die Bildabmessungen (img_height und img_width) und die Batch-Größe (batch_size), werden festgelegt.

```python

train_dir = './../Trainingsdaten'
batch_size = 32
img_height = 256
img_width = 256

```

Der ImageDataGenerator wird wieder verwendet, um die Trainingsdaten zu normalisieren und Data Augmentation durchzuführen.

```python

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

```

Die Trainingsdaten und Validierungsdaten werden mit flow_from_directory aus den entsprechenden Verzeichnissen geladen. Die Klassenzuweisung erfolgt automatisch basierend auf der Verzeichnisstruktur.

```python
# Trainingsdaten laden
train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',  # Hier wird die Klassenzuweisung automatisch wegen der Verzeichnissstruktur vorgenommen
    subset='training',
    classes=['Schlapfen', 'No_Schlapfen']
)


```

Das CNN-Modell wird mit keras.Sequential erstellt. Es hat zwei Convolutional Layers mit Pooling Layers, gefolgt von einer Flatten-Layer und zwei Dense Layers. Das Modell wird mit dem Adam-Optimizer und der Binary Crossentropy Loss-Funktion kompiliert.


```python

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

```

Das Modell wird für eine festgelegte Anzahl von Epochen (epochs) trainiert, wobei die Trainings- und Validierungsdaten verwendet werden.


```python



```

Schließlich wird das trainierte Modell in einer Datei mit dem Namen "model_from_video_trained.h5" gespeichert.


```python



```

Dieses Programm trainiert ein CNN-Modell für die Klassifikation von Schlapfen und Nicht-Schlapfen-Bildern und speichert das trainierte Modell in einer Datei. 
