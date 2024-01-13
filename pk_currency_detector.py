import tensorflow as tf
import numpy as np
model=tf.keras.models.load_model('currency_model.h5',compile=False)
class_names=['1000_back',
  '1000_front',
  '100_back',
  '100_front',
  '10_back',
  '10_front',
  '20_back',
  '20_front',
  '5000_back',
  '5000_front',
  '500_back',
  '500_front',
  '50_back',
  '50_front',
  'others']
# function to load currency
def currency(img):
    img = np.array(img)
    # reshape the image to 224 x 224 pixels
    image = tf.image.resize(img, [224, 224])
    # expand dimensions
    image = tf.expand_dims(image, axis=0)
    # predict currency
    prediction = model.predict(image)
    note_name = class_names[np.argmax(prediction)]
    note_name = note_name.split('_')
    note_name = ' '.join(note_name)
    # return currency
    return note_name
