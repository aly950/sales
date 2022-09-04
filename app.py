import joblib
from flask import Flask, render_template, request
import preprocess  
import numpy as np

app = Flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model = joblib.load('Models/RF.h5')


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST' :
        weight = request.form['weight']
        fat = request.form['fat']
        product = request.form['product']
        price = request.form['price']
        size = request.form['size']
        population = request.form['population']
        market = request.form['market']
        
    data = {'weight' : weight, 'fat' : fat, 'product' : product, 
            'price' : price, 'size' : size, 'population' : population, 'market' : market}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    #scaled_data = scaled_data[0][:8]
    prediction = int(model.predict(scaled_data)[0])
    
    # return str(round(prediction))
    return render_template('prediction.html', sales = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
   
    