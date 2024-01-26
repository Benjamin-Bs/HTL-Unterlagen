# Unitests für CNN

Um in Python Unittest zu machen ist es vonnöten von **unittest.TestCase** zu erben, dies wird in Python in der
Klassendefinition in runden Klammern durchgeführt.

Vor allem sind diese Imports essenziell

```python

import unittest

from keras.src.preprocessing.image import ImageDataGenerator
import keras

```

Zunächst wird eine setUp Methode erzeugt diese setUp-Methode initialisiert verschiedene Parameter, die für das Training
des CNN verwendet werden, wie den Pfad zum Trainingsdatensatz, die Batch-Größe, die Bildgröße, die Anzahl der Epochen
und einen Bildgenerator, der Datenaugmentation durchführt.

```python

def setUp(self):
    self.train_dir = '../Trainingsdaten'
    self.batch_size = 32
    self.img_height = 256
    self.img_width = 256
    self.epochs = 3  # Je weniger desto schneller

    self.train_datagen = ImageDataGenerator(
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




Die create_model-Methode definiert das CNN-Modell. Es enthält zwei Convolutional Layers, zwei Max-Pooling Layers, eine Flatten-Layer und zwei Dense Layers. Das Modell wird mit dem Adam-Optimizer und der Binary Crossentropy Loss-Funktion kompiliert.


```python

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(self.img_height, self.img_width, 3)),
            keras.layers.MaxPooling2D(2, 2),
            keras.layers.Conv2D(64, (3, 3), activation='relu'),
            keras.layers.MaxPooling2D(2, 2),
            keras.layers.Flatten(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model
```


Die test_model_training-Methode überprüft das Training des Modells. Sie verwendet den ImageDataGenerator, um Trainings- und Validierungsdaten zu erstellen und das Modell darauf zu trainieren. Dann wird überprüft, ob die Genauigkeit ('accuracy') im Trainingsverlauf enthalten ist.

```python

     def test_model_training(self):
        train_data = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
            class_mode='binary',
            subset='training',
            classes=['Schlapfen', 'No_Schlapfen']
        )
```

Schließlich wird die unittest.main()-Funktion verwendet, um die Testfälle auszuführen, wenn das Skript direkt ausgeführt wird.
