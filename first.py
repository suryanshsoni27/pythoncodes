import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
import keras.models
import keras.layers
from keras import backend as K
import pandas as pd
data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()
#img_w , img_h = 813,414
#train_foot_images = "C:\Users\hsoni\Desktop\Research work\Participant Pictures\P 23"
#train_foot_validation_img = "C:\Users\hsoni\Desktop\Research work\Participant Pictures\P 23"
#nb_train_samples = 5
#nb_validation_samples = 5




class_name = ['T-shirt/top','Trouser','Pullover', 'Dress', 'Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

plt.imshow(train_images[8], cmap=plt.cm.binary)
plt.show()
print(train_labels[0])
print(train_images[7])
train_images = train_images/255.0
print(train_images[4])


#creating a model
#testing a model
#setting up the whole model
#architecture of neural networks
#images come 28*28 value
#[[0,0.2,0.3]]
#we go down 28
#we have to figure out a way to pass the informatio to the nerauvlnt
#flattening the data
#remove the interiro arrrays
#one element in each array
#flatten the data so that we have lst of 784 elemet pixel and we feed that to neeuralv net
#784 neuron
#output layer number between 0 and 9
#0-9 10 neurons
#each neuron has a value
#we classify image for eg pants
#we gonna hve 784*10 bias and weights.
#hidden layer has 1028 neuron
#hidden layer will be connected to ouput neuron
#may


model = keras.Sequential([
   keras.layers.Flatten(input_shape=(28,28)),
   keras.layers.Dense(128,activation="relu"),
   keras.layers.Dense(10,activation="softmax")
])

model.compile(optimizer = "adam",loss = "sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_images, train_labels, epochs = 5)
test_loss ,test_acc = model.evaluate(test_images,test_labels)



prediction = model.predict(test_images)

for i in range(5):
   plt.grid(False)
   plt.imshow(test_images[i],cmap = plt.cm.binary)
   #plt.xlabel("Actual: "+ test_labels[i])
   plt.title("prediction " + class_name[np.argmax(prediction[0])])

plt.show()


model = keras.Sequential([
   keras.layers.Flatten(input_shape = (28,28)),
   keras.layers.Dense(128,activation='relu'),
   keras.layers.Dense(10,activation='softmax')

])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(train_images,train_labels,epochs=5)
test_loss,test_acc = model.evaluate(test_images,test_labels)

print("tested acc:", test_acc)

