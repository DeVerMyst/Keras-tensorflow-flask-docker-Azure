import tensorflow as tf

model = tf.keras.applications.VGG19() 
## save the weights to a HDF5 file 
model.save('app/weights/my_model.h5')
