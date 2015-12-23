import csv
from flask import Flask, render_template, request
import os
import requests
app = Flask(__name__) 

#command line app
def run_questions():
    print "How far do you want to run?" 
    distance = raw_input(" 5K, 10K, 15K, 1mile (1M), 10miles (10M), 13.1M (1/2 marathon), 26.2M (full marathon), 20K, 30K, 50K: ")
    return distance

@app.route('/submit', methods=['POST'])
def find_race():
    #open csv file for searching for races
    races = []
    with open('2016Runs.csv', 'rb') as csvfile:
        runs2016_raw = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        #try to receive information from form on html page
        try:
            #doesn't work yet, uses requests to get info from form name="runs" 
            runs=request.form.get('runs')
            distance = str(runs)
            print "==> runs type: ",type(runs), "\nvalue:", runs, "\ndistance:",distance
            print distance, type(distance)
            print "form submit success!"
            for row in runs2016_raw:
                if distance in row['Distance']:
                    races.append((row['Name'], row['Date'], row['Location']))
            msg='Just do it!'
            return render_template('index.html', msg=msg,races=races)
            
        #if html form submit fails, race distance is collected through command line
        except:
            msg='Sorry, something went wrong.'
            return render_template('index.html', msg=msg,races=races)
            #distance = run_questions()
            
        #compares selected distance (whether from html form or command line
        #to dictionary of all races and builds list of selected races.
        
    

#posts list of filtered races to html page
@app.route('/', methods=['GET', 'POST']) 
def form():
    msg = "Let's Race!"
    return render_template('index.html', msg=msg)

#init to run app & IP is set to run on cloud9
if __name__=='__main__':
   app.run( host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug = True)
   #app.run(debug=True, port=5000) #for running locally