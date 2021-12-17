from flask import Flask, render_template
import plotly
import pandas as pd, plotly.express as px, plotly.offline as pyo
import json
import altair as alt

app = Flask(__name__)

@app.route('/')
def index():     
    return render_template('index.html')

@app.route('/plot1')
def plot1():
    dataframe = pd.read_csv(r'final\processed_data\month_increase.csv')
    fig = px.treemap(dataframe, path =  [px.Constant('total'), 'year', 'month'], values = 'monthly_increase', color = 'monthly_increase')
    fig = fig.update_xaxes(rangeslider_visible=True)  
    fig.update_layout(width=1500, height=500) 
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = 'Treemap of monthly increase'
    description = 'This plot break down the newly increased case to months. We can figure out which months are the outbreak of covid each year'

    return render_template('plotly1.html', plot_json=plot_json, header=header, description=description)

@app.route('/plot2')

def plot2():
    dataframe2 = pd.read_csv(r'final\processed_data\global.csv', encoding = 'latin-1')
    fig2 = px.treemap(dataframe2, path = [px.Constant('Total'), 'WHO_region', 'Country'], values = 'Cumulative_cases')
    fig2.update_layout(width=1500, height=500) 
    plot_json = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    header = 'Treemap of global cases'
    description = 'This plot break down the cumulative cases into regions and countries. We can figure out which country has the most cumulative cases in their region'

    return render_template('plotly1.html', plot_json=plot_json, header=header, description=description)

@app.route('/plot3')

def plot3():

    header = 'Line chart of monthly increase cases'
    description ='This plot shows how monthly changed across the year. '

    return render_template('plot3.html', header=header, description=description)

@app.route('/plot4')

def plot4():

    header = 'Line chart of culmulative cases and cumulative deaths'
    description ='As you can see from the graph, the confirmed case is increasing in a rapid speed, while the deaths cases remain relatively stable'

    return render_template('plot4.html', header=header, description=description)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)