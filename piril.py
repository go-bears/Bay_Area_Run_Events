import csv
from flask import Flask, render_template, request
import os
import requests
app = Flask(__name__) 

#command line app
print "How far do you want to run?" 
distance = raw_input(" 5K, 10K, 15K, 1mile (1M) 5miles (5M), 10miles (10M), 13.1M (1/2 marathon), 26.2M (full marathon), 20K, 30K, 50K: ")


        # print row['Date']
        # print row['Distance']
        # print row['Name']
        # print row['Location']

    
    

# methods={'1M','5K','10K','Half Marathon','Full Marathon', '30K', '50K's
# def index():
#     errors=[ ]
#     results= { }
#      if distance in row['5K']:
#             print row['Date'], row['Location']
# def signup():
#     '5K' = request.form['5K']
#     print("These are the upcoming 5K races")

@app.route('/', methods=['GET', 'POST']) 
def form():
    with open('2016Runs.csv', 'rb') as csvfile:
        runs2016_raw = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        #runs=request.form.get('runs')
        
        # print runs * 5
        races = []
        for row in runs2016_raw:
            
            if distance in row['Distance']:
                races.append((row['Date'], row['Location']))
        msg = "Let's Race!"
    return render_template('index.html', msg=msg, races=races)
    

if __name__=='__main__':
   
    app.run( host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug = True)