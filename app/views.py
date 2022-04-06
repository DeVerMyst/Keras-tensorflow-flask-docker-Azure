from app import app
from os.path import dirname, join, abspath 
from flask import render_template, request
from keras.preprocessing.image import load_img
from app.model import process_image, predict_class
APP_ROOT = dirname(abspath(__file__))
# print('\n***** ',APP_ROOT,'\n')

UPLOAD_FOLDER = join(APP_ROOT,'static','img')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():       
    return render_template("index.html")
# def hello():
#     return "Hello simplonien voila une petite application utilisant flask et tournant sur Azure Container Instance!"

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        # Pris sur le site de flask, a part les flash
        if 'file' not in request.files:
            return render_template("index.html")
        file = request.files['file']
        if file.filename == '':
            return render_template("index.html")
        if file and allowed_file(file.filename):
            filename = "test.jpg"
            # urlimg = join('static','img', filename)            
            urlimg = join(app.config['UPLOAD_FOLDER'], filename)
            file.save(urlimg)    

            # Charge l'image
            image = load_img(urlimg, target_size=(224, 224))
            # Traitement de l'image
            image = process_image(image)
            # Prediction
            prediction, percentage = predict_class(image) 
            
            urlimg = join('static','img', filename)     
            return render_template("results.html",urlimg=urlimg, prediction=prediction, percentage=percentage)

    else: 
        return render_template("index.html")            