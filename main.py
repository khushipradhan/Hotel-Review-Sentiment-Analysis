from flask import Flask,render_template,request
import pickle
import numpy as np
model=pickle.load(open('hotelmodel.pkl','rb'))
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    example=request.form.get('example')
    features=[np.array(example)]
    result=model.predict(features)

    return render_template("index.html",prediction_text="The sentiment is{}".format(predict))
app.run(debug=True)
if __name__== '__ main__':
    app.run(debug=True)