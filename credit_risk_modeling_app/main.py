from flask import Flask, render_template, request
import pickle
import joblib
import pandas as pd

app = Flask(__name__)
#load the model
model = joblib.load('risk_modeling_pipeline.pkl')

@app.route('/')
def home():
	result = ''
	dd = {}
	return render_template('index.html', **locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
	d = {}
	d['person_age'] = float(request.form['person_age'])
	d['person_income'] = float(request.form['person_income'])
	d['person_emp_length'] = float(request.form['person_emp_length'])
	d['loan_amnt'] = float(request.form['loan_amnt'])
	d['loan_int_rate'] = float(request.form['loan_int_rate'])
	d['loan_percent_income'] = float(request.form['loan_percent_income'])
	d['cb_person_cred_hist_length'] = float(request.form['cb_person_cred_hist_length'])


	#quantitative variables
	d['person_home_ownership'] = request.form['person_home_ownership']
	d['loan_intent'] = request.form['loan_intent']
	d['loan_grade'] = request.form['loan_grade']
	d['cb_person_default_on_file'] = request.form['cb_person_default_on_file']
	result = model.predict(pd.DataFrame(d,index=[0]))[0]
	output = "The customer will default."
	if result == 0:
		output = "The customer will not default."

	return render_template('index.html', **locals(), dd=d)
 		

if __name__ == '__main__':
	app.run(debug=True)