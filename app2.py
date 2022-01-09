import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly
import plotly.graph_objs as go

import pandas as pd
import pathlib
import dash_bootstrap_components as dbc


import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pathlib


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import os 







# get relative data folder




df_monthly = pd.read_csv("data/monthly_table.csv",sep = ';').replace(0.0,"-")
df_prices = pd.read_csv("data/res1.csv")
df_trades = pd.read_csv("data/trades.csv")
df_drawdowns = pd.read_csv("data/drawdowns.csv")
df_kpi1 = pd.read_csv("data/main_kpi.csv")
df_kpi2 = pd.read_csv("data/kpi2.csv")
df_kpi3 = pd.read_csv("data/kpi3.csv")
df_kpi4 = pd.read_csv("data/kpi4.csv")
df_kpi5 = pd.read_csv("data/kpi5.csv")


red = 'rgb(151,21,28)'
grey = '#3c4743'

def rebase_series(self,series):
    return (series/series.iloc[0]) * 100  

df_temp = df_prices
df_temp = df_temp.set_index('date')
#plotly combined equity chart
trace_equity = go.Scatter(
                    x=df_temp['equity_curve'].index.tolist(),
                    y=df_temp['equity_curve'].values.tolist(),
                    name='Strategy Backtest',
                    yaxis='y2',
                    line = dict(color = (red)))

trace_benchmark = go.Scatter(
                    x=df_temp['benchmark'].index.tolist(),
                    y=df_prices['benchmark'].values.tolist(),
                    name='S&P 500 Index',
                    yaxis='y2',
                    line = dict(color = (grey)))


####
trace0 = go.Histogram(x=df_prices['equity_curve'].pct_change().values,
                        name="Strategy Backtest",
                        opacity=0.75,
                        marker=dict(
                        color=(red)),
                        xbins=dict(
                        size=0.0025
                                ))

trace1 = go.Histogram(x=df_prices['benchmark'].pct_change().values,
                        name="S&P 500 Index",
                        opacity=0.75,
                        marker=dict(
                        color=(grey)),
                        xbins=dict(
                        size=0.0025
                                ))


def get_ffn_stats(equity_series):
    equity_stats = equity_series.calc_stats()
    d = dict(equity_stats.stats)
    return d


trace_equity_drawdown = go.Scatter(
                    x=list(df_drawdowns['date']),
                    y=list(df_drawdowns['equity_curve']),
                    name='Strategy Backtest',
                    yaxis='y2',
                    line = dict(color = (red)))

trace_benchmark_drawdown = go.Scatter(
                    x=list(df_drawdowns['date']),
                    y=list(df_drawdowns['benchmark']),
                    name='S&P 500 Index',
                    yaxis='y2',
                    line = dict(color = (grey)))



trace_box1 = go.Box(y=df_prices['equity_curve'].pct_change().values,
                name="Strategy Backtest",
                marker=dict(
                                color=(red)))

trace_box2 = go.Box(y=df_prices['benchmark'].pct_change().values,
                name="S&P 500 Index",
                marker=dict(
                        color=(grey)))

data = [trace0,trace1]


data = [trace0,trace1]
###

app = dash.Dash(
    __name__,prevent_initial_callbacks=True, meta_tags=[{"name": "viewport", "content": "width=device-width"}],external_stylesheets=["https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" ,
    "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"],external_scripts=["https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"])

app.title = "Sofaer Technologies"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(

        [

            html.Div(
	html.Div([
            dbc.Row([
                    html.Div(
                        html.H6(
                            "Sofaer Technologies",className="seven columns main-title",style = {"padding-left":"20px","padding-top":"20px"}
                        ),
                    ),
                    html.Div(
                        html.H5("Combined Strategy Backtest Report"),
                        className="seven columns main-title",
                    ),

                ], style = {"padding-bottom":"135px!important","padding-left": "0px","padding-top":"40px"})
        	],className = "header-space",style = {"padding-bottom":"135px!important","padding-left": "0px","padding-top":"40px"})
),
            # page 1
            html.Div(
                [
                    # Row 3
                    dbc.Row(
                        [
                          dbc.Col(
                                [
                                    html.H5("Summary"),
                                    html.Br([]),
                                    html.P(                                   

                                        "\
     This report summarizes the backtest results of the fund's strategy over the last 27 years. The results are benchmarked against the S&P 500 Index by comparison with the ETF SPY. This strategy applies systematic trading using quantitative models derived from mathematical and statistical analysis. The algorithms are continuously improved with machine learning. The underlying security for this backtest is the ETF SPY with 3X leverage in 26% of the total trades.",
                                        style={"color": "#ffffff",'width': '100%'},
                                    ),
                                ],
                                className="product",
                            )
                        ],style = {"padding-top":"40px!important"}
                    ),
                    # Row 4
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H6(
                                        "Overview", className="subtitle"
                                    ),

                                    dbc.Table.from_dataframe(df_kpi1,hover = True,striped = False, responsive = True,bordered = True),
                                ],
                            ),


                            dbc.Col(
                                [
                                    html.H6(
                                        "Average performance",
                                        className="subtitle",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "27 Year",
                                                    ],
                                                    y=[
                                                        "38.07",
                                                        "39.96",
                                                        "36.11",
                                                        "31.59",
                                                        "30.17",
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Strategy Backtest",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "27 Year",
                                                    ],
                                                    y=[
                                                        "30.43",
                                                        "25.65",
                                                        "18.03",
                                                        "16.26",
                                                        "10.63",

            
                                                    ],
                                                    marker={
                                                        "color": grey,
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="S&P 500 Index",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 20,
                                                },
                                                showlegend=True,
                                                title="",
                                                #width=450,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": True , 'displaylogo': False},
                                    ),
                                ],style = {"padding-left":"50px!important"},
                            ),
                        ], justify="evenly"
                    ),




        dbc.Row([

           
dbc.Col([
    html.Div([
    html.H6(
                         "Monthly Table and Yearly Returns  (%)",className="subtitle"
                                        ), 



             dbc.Table.from_dataframe(df_monthly,hover = True,striped = False, responsive = True,bordered = True,color ="light"),
             ]), 
]), #,style = {"overflow-x:auto"}),

        ],            justify="center",
),





dbc.Row([
                      
                            dbc.Col(
                                
                                [
                                    html.Div([html.H6(
                                        "Performance Chart",className="subtitle",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                trace_equity,trace_benchmark
                                                    ],
                                            "layout" : go.Layout(                                               
                                                 font={"family": "Raleway", "size": 10},
                                                 showlegend = True,
                                                 #height = 450,
                                                #  width = 550,
                                                 autosize=True,
                                                xaxis={
                                                    #"range": [1994,2021],
                                    "nticks": 8,

                                                    "showgrid": False,
                           
                                                },
                                            )
                                    
                                        },
                                        config={"displayModeBar": True,'displaylogo': False},

                                    ),
                                    ]),  
                                
                                ],
                            )
                            ,

                            dbc.Col(
                                
                                [
                                                                         html.H6(
                                        "Trade Statistics",
                                        className="subtitle",
                                    ),
                           
                                    dbc.Table.from_dataframe(df_trades,hover = True,striped = False, responsive = True,bordered = True),
                                ],
                            ),

                        ],             

                    ),



        ]),




            #        ],   className="page",
            # ),

                
    dbc.Row([dbc.Col([     html.H6(
                    "KPI Tables",className="subtitle"
                    ), ])]),
     dbc.Row([
 
                       dbc.Col([
                           
    #  html.H6(
    #                 "KPI Tables",className="subtitle"
    #                 ),  
                                    dbc.Table.from_dataframe(df_kpi2,hover = True,striped = False, responsive = True,bordered = True),
                                        ]),


                                           dbc.Col([
                                    dbc.Table.from_dataframe(df_kpi3,hover = True,striped = False, responsive = True,bordered = True),
                                        ]),
        ],justify = "evenly"),

    dbc.Row([
                dbc.Col([
                       html.H6(
                    
                    ),  
                                    dbc.Table.from_dataframe(df_kpi4,hover = True,striped = False, responsive = True,bordered = True),
                                        ] ),
                

                dbc.Col([
                                    dbc.Table.from_dataframe(df_kpi5,hover = True,striped = False, responsive = True,bordered = True),
                                        ]),
        ],justify = "evenly"),



   



                         
#drawdowns
dbc.Row([

         dbc.Col([ 

                     html.H6(
                        "Drawdown Chart",className="subtitle"
                    ),
         
        dcc.Graph(id = "idk", 
                figure = { "data": 
                                [
                                        trace_equity_drawdown
                                        ,trace_benchmark_drawdown],
                        "layout":
                                go.Layout(
                                # title='Histogram of Strategy and Benchmark Weekly Returns',
                                autosize=True,
				#Margin = 0,	

				#pad = 0,
                                #height=600,
				width =1000,
                                font={"family": "Raleway", "size": 10},

                                # hovermode = 'closest',
                                # barmode='overlay',
                                                                                 
                                showlegend=True,
                                xaxis={
                                    # "autorange": True,
                                    "linecolor": "rgba(127, 127, 127, 0.2)",
                                    # "linewidth": 1,
                                    "showgrid": False,
                                    # "showline": True,
                                    # "title": "",
                                    # "type": "linear",
                                },
                                yaxis={
                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                  
                                    "showgrid": True,
                           
                                    "zeroline": False,
                                    "zerolinewidth": 4,
                                },
                                )
                        },
                                
                 config={"displayModeBar": True ,'displaylogo': False}                                  
                    ),
         ]), 
        ]),

    




#BOX PLOTS
dbc.Row([


dbc.Col([

           
            html.H6(
                        "Boxplot of Strategy and Benchmark Weekly Returns",className="subtitle"
                    ),
                             
        dcc.Graph(id = "idk2", 
                figure = { "data": 
                                [
                                        trace_box1
                                        ,trace_box2],
                        "layout":
                                go.Layout(
                                # title='Histogram of Strategy and Benchmark Weekly Returns',
                                autosize=True,
                                #height=600,
                                font={"family": "Raleway", "size": 10},

                                hovermode = 'closest',
                                barmode='overlay',
                                                                                 
                                showlegend=True,
                                xaxis={
                                    "autorange": True,
                                    "linecolor": "rgba(127, 127, 127, 0.2)",
                                    # "linewidth": 1,
                                    "showgrid": False,
                                    "showline": False,
                                    "title": "",
                                    "type": "linear",
                                },
                                yaxis={
                                    "autorange": True,
                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                    "mirror": False,
                                    "nticks": 5,
                                    "showgrid": True,
                                    # "showline": True,
                                    "zeroline": False,

                                    "ticklen": 10,
                                    "ticks": "outside",
                                    # "title": "%",
                                    "type": "linear",
                                    "zeroline": False,
                                    "zerolinewidth": 4,
                                },
                                )
                        },
                                
                 config={"displayModeBar": True, 'displaylogo': False}                                  
                    ),
            
        ]),]),

    











       
dbc.Row([

 

dbc.Col([

                    html.H6(
                        "Histogram of Strategy and Benchmark Weekly Returns",className="subtitle"
                        
                    ),                            
        dcc.Graph(id = "idk3", 
                figure = { "data": 
                                [
                                        go.Histogram(x=df_prices['equity_curve'].pct_change().values,
                                        name="Strategy",
                                        opacity=0.75,
                                        marker=dict(
                                        color=('rgb(151,21,28)')),
                                        xbins=dict(
                                        size=0.0025))
                                        ,trace1],
                        "layout":
                                go.Layout(
                                # title='Histogram of Strategy and Benchmark Weekly Returns',
                                autosize=True,
                                #height=600,
                                font={"family": "Raleway", "size": 10},

                                hovermode = 'closest',
                                barmode='overlay',
                                                                                 
                                showlegend=True,
                                xaxis={
                                    "autorange": True,
                                    "linecolor": "rgba(127, 127, 127, 0.2)",
                                    # "linewidth": 1,
                                    "showgrid": False,
                                    # "showline": True,
                                    "title": "",
                                    "type": "linear",
                                },
                                yaxis={
                                    "autorange": True,
                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                    "mirror": False,
                                    "nticks": 5,
                                    "showgrid": True,
                                    # "showline": True,
                                    "ticklen": 10,
                                    "ticks": "outside",
                                    # "title": "%",
                                    "type": "linear",
                                    "zeroline": False,
                                    "zerolinewidth": 4,
                                },
                                )
                        },
                                
                 config={"displayModeBar": True, 'displaylogo': False}                                  
                    ),
            
        ]),]),




	dbc.Row([dbc.Col([html.P("info@sofaertechnologies.com",className="foot")])],justify="center"),




   

        ], className = "page")

    

        





if __name__ == "__main__":
    # app.run_server(debug=True,port=5000)
    app.run_server(host = '0.0.0.0')
