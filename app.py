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
        Item_Weight = request.form['Item Weight']
        Item_Fat_Content = request.form['Fat']
        Item_Type = request.form['Item Type']
        Item_MRP = request.form['price']
        Outlet_Size = request.form['Size']
        Outlet_Location_Type = request.form['Location Tier']
        Outlet_Type = request.form['Market type']
        
    data = {'Item_Weight' : Item_Weight, 'Item_Fat_Content' : Item_Fat_Content, 'Item_Type' : Item_Type, 
            'Item_MRP' : Item_MRP, 'Outlet_Size' : Outlet_Size, 'Outlet_Location_Type' : Outlet_Location_Type, 'Outlet_Type' : Outlet_Type}
    
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
    