import joblib
from flask import Flask, render_template, request
import preprocess  

app = Flask(__name__)

scaler = joblib.load('model/scaler.h5')
model = joblib.load('model/RF.h5')


@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET']) 
def get_prediction() :
    if request.method == 'POST' :
        Item_Weight = request.form['weight']
        Item_Fat_Content = request.form['fat']
        Item_Type = request.form['product']
        Item_MRP = request.form['price']
        Outlet_Size = request.form['size']
        Outlet_Location_Type = request.form['population']
        Outlet_Type = request.form['market']
        
    data = {'weight' : Item_Weight, 'fat' : Item_Fat_Content, 'product' : Item_Type, 
            'price' : Item_MRP, 'size' : Outlet_Size, 'population' : Outlet_Location_Type, 'market' : Outlet_Type}
    
    final_data = preprocess.preprocess_data(data)
    scaled_data = scaler.transform([final_data])
    scaled_data = scaled_data[0][:10]
    prediction = int(model.predict(scaled_data)[0])
    
    # return str(round(prediction))
    return render_template('prediction.html', sales = str(prediction))
        
        

if __name__ == '__main__' :
    app.run(debug = True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    