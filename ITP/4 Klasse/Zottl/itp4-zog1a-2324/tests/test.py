import unittest

from keras.src.preprocessing.image import ImageDataGenerator
import keras




class TestCNN(unittest.TestCase):

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

    def test_model_training(self):
        train_data = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
            class_mode='binary',
            subset='training',
            classes=['Schlapfen', 'No_Schlapfen']
        )

        validation_data = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
            class_mode='binary',
            subset='validation',
            classes=['Schlapfen', 'No_Schlapfen']
        )

        model = self.create_model()

        history = model.fit(train_data, epochs=self.epochs, validation_data=validation_data)
        self.assertTrue('accuracy' in history.history)

    #def test_model_saving(self):
        #model = self.create_model()
        # model.save('unit_test_model.h5')
        # self.assertTrue(keras.utils.get_file('test_model.h5'))


if __name__ == '__main__':
    unittest.main()

