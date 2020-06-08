import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# initialize the Flask app
app = Flask(__name__)
ml_model = pickle.load(open('ml_model.pkl','rb'))

# root api
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    for rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = ml_model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Compressive Strength of Concrete {} MPa'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    for direct API calls
    '''
    data = request.get_json(force=True)
    prediction = ml_model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)