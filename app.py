from flask import Flask, render_template, request
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
 
        time = request.form['time']
 
        data = int(time)
 
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(start = 2616 + data, end = 2616 + data)
        output = round(prediction[0],2)

 
    return render_template('index.html', prediction=output)
if __name__ == '__main__':
    app.run(debug=True)