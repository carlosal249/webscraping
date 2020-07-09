import flask
from flask import Flask, send_file, escape, request, render_template
import pandas as pd
from twitterscraper import query_tweets
import datetime as dt
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import xlsxwriter

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('Scraping.html')
    
    if flask.request.method == 'POST':
        user_inputs = {
            'inicio_ano': flask.request.form['inicio_ano'],
            'inicio_mes': flask.request.form['inicio_mes'],
            'inicio_dia': flask.request.form['inicio_dia'],
            'final_ano': flask.request.form['final_ano'],
            'final_mes': flask.request.form['final_mes'],
            'final_dia': flask.request.form['final_dia'],
            'lang': flask.request.form['lang'],
            'conteudo': flask.request.form['conteudo'],
        }

        inicio_ano = user_inputs['inicio_ano']
        inicio_mes = user_inputs['inicio_mes']
        inicio_dia = user_inputs['inicio_dia']

        final_ano = user_inputs['final_ano']
        final_mes = user_inputs['final_mes']
        final_dia = user_inputs['final_dia']

        lang = user_inputs['lang']
        conteudo = user_inputs['conteudo']
        
        inicio_ano = int(inicio_ano)
        inicio_mes = int(inicio_mes)
        inicio_dia = int(inicio_dia)

        final_ano = int(final_ano)
        final_mes = int(final_mes)
        final_dia = int(final_dia)
        
        begin_date = dt.date(inicio_ano, inicio_mes,inicio_dia)
        end_date = dt.date(final_ano, final_mes, final_dia)
        conteudo= str(conteudo)

        print(begin_date)
        print(end_date)
        print(lang)
        print(conteudo)
        

        #tweets = query_tweets(conteudo, lang=lang, begindate=begin_date, enddate=end_date)

        #data = pd.DataFrame(t.__dict__ for t in tweets)
        
        #data.head()
        #writer = pd.ExcelWrither('produtos.xlsx')

        #n_registros = len(data)
        #download = data.to_csv('tweets.csv')
        # , titles=produtos.columns.values
        return flask.render_template('Scraping.html')#,download=download, tables=[data.to_html(classes='data')], n_registros=n_registros)  

if __name__ == '__main__':
    app.run(debug=True) #host='0.0.0.0' 