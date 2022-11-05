Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "288d7667",
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.preprocessing.image import ImageDataGenerator\n",
    "train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)\n",
    "test_datagen=ImageDataGenerator(rescale=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d139959f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Found 5384 images belonging to 6 classes.\n",
      "Found 1686 images belonging to 6 classes.\n"
     ]
    }
   ],
   "source": [
    "x_train=train_datagen.flow_from_directory(r'C:\\Users\\uma25\\project\\Dataset Plant Disease\\fruit-dataset\\fruit-dataset\\train',target_size=(128,128),batch_size=2,class_mode='categorical')\n",
    "x_test=test_datagen.flow_from_directory(r'C:\\Users\\uma25\\project\\Dataset Plant Disease\\fruit-dataset\\fruit-dataset\\test',target_size=(128,128),batch_size=2,class_mode='categorical')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2383c259",
   "metadata": {},
   "outputs": [
    {
...      "name": "stdout",
...      "output_type": "stream",
...      "text": [
...       "Found 11386 images belonging to 9 classes.\n",
...       "Found 3416 images belonging to 9 classes.\n"
...      ]
...     }
...    ],
...    "source": [
...     "x_train=train_datagen.flow_from_directory(r'C:\\Users\\uma25\\project\\Dataset Plant Disease\\Veg-dataset\\Veg-dataset\\train_set',target_size=(128,128),batch_size=2,class_mode='categorical')\n",
...     "x_test=test_datagen.flow_from_directory(r'C:\\Users\\uma25\\project\\Dataset Plant Disease\\Veg-dataset\\Veg-dataset\\test_set',target_size=(128,128),batch_size=2,class_mode='categorical')"
...    ]
...   }
...  ],
...  "metadata": {
...   "kernelspec": {
...    "display_name": "Python 3 (ipykernel)",
...    "language": "python",
...    "name": "python3"
...   },
...   "language_info": {
...    "codemirror_mode": {
...     "name": "ipython",
...     "version": 3
...    },
...    "file_extension": ".py",
...    "mimetype": "text/x-python",
...    "name": "python",
...    "nbconvert_exporter": "python",
...    "pygments_lexer": "ipython3",
...    "version": "3.9.12"
...   }
...  },
...  "nbformat": 4,
...  "nbformat_minor": 5
