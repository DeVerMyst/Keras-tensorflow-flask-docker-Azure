import tensorflow as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg19 import preprocess_input
from keras.applications.vgg19 import decode_predictions

# model = tf.keras.applications.VGG19() 
## save the weights to a HDF5 file 
# model.save('my_model.h5')

model = tf.keras.models.load_model('app/weights/my_model.h5', compile=False)
def process_image(image):
    '''
    Pre processing de l'image pour la rendre utilisable par le modèle VGG19
    '''
    print('process image')
    # Image vers array
    image = img_to_array(image)
    # On donne la bonne taille de l'array
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare l'image pour le modèle VGG19
    image = preprocess_input(image)

    return image

def predict_class(image):
    '''
    Prédire la classe et le score de précision de l'image, on garde que le premier résultat
    '''
    print('predict image')
    # Prédire la probabilité de chaque classe
    yhat = model.predict(image)
    # On décode les labels
    label = decode_predictions(yhat)
    # On prend le premier résultat
    label = label[0][0]
    # On retourne la classe et le score
    prediction = label[1]
    percentage = '%.2f%%' % (label[2]*100)

    return prediction, percentage

## Pour tester les fonctions (DEV)
# if __name__ == '__main__':
#     '''Pour tester si le code fonctionne correctement'''
#     print('main')
#     # load an image from file
#     image = load_img('static/test/image.jpg', target_size=(224, 224))
#     image = process_image(image)
#     prediction, percentage = predict_class(image)
#     print(prediction, percentage)
