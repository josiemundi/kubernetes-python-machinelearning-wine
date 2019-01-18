from flask import Flask, request, render_template

import numpy as np
from keras.models import load_model
from sklearn.externals import joblib
scaler = joblib.load('wine_scaler.save') 

model = load_model('wine_model.h5')
model._make_predict_function()
app = Flask(__name__)
 
param_names =  [ 
    'fixedAcidity',
    'volatileAcidity',
    'citricAcid',
    'residualSugar',
    'chlorides',
    'freeSulfurDioxide',
    'totalSulfurDioxide',
    'density',
    'ph',
    'sulphates',
    'alcohol'
]

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/api/')
def api():
    data_array = []
    for param in param_names:
        data_array.append(request.args.get(param))
    # data = {}
    # for key in request.args:
    #     data[key] = request.args.get(key)
    data_array = np.array([data_array])
    return str(model.predict(scaler.transform(data_array))[0][0])
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

