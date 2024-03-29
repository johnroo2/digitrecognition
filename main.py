import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def train():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape = (28, 28)))
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.selu))
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.selu))
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=3)

    accuracy, loss = model.evaluate(x_test, y_test)
    print(accuracy)
    print(loss)

    model.save('digits.model')
    return model

m = train()
m = tf.keras.models.load_model('digits.model')

def predict(path):
    img = cv.imread(path)[:, :, 0]
    img = np.invert(np.array([img]))
    prediction = m.predict(img)
    print('The result should be: ' + str(np.argmax(prediction)))
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()

for x in range(0, 10):
    predict(str(x) + '.png')
predict('7zesty.png')

