from flask import Flask, render_template, request
import joblib

# initialise the app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')


@app.route('/')
def hello_word():
    return render_template('predict.html')

@app.route('/predict' , methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0]==1:
        ans = 'dibatic'
    else:
        ans = 'not dibatic'

    return render_template('predict.html' , predict = f'the person is {ans}' )


    ##return render_template('predct_obs.html', predict = f'the person is {ans}')


#@app.route('/predict' , methods = ['post'])
#def predict():
  #  first_name  = request.form.get('fname')
   # last_name  = request.form.get('lname')
   # email_name  = request.form.get('email')
    #phone_no  = request.form.get('phone')
    #print(first_name)
    #print(last_name)
    #print( email_name )
    #print(phone_no)
    #return 'Form Submitted'


#run the app
app.run(debug=True)
