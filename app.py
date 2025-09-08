from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        years_exp = float(request.form['years_exp'])
        pred = model.predict(np.array([[years_exp]]))
        salary = round(pred[0], 2)
        return render_template('index.html', prediction=f'estimated salary: $ {salary}')
    except Exception as e:
        return render_template('index.html', prediction='error: invalid input')

if __name__ == '__main__':
    app.run(debug=True)



