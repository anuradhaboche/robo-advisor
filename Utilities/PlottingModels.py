import pandas as pd
import numpy as np
import plotly.graph_objects as go
# from plotly.offline import init_notebook_mode, iplot

def current_price( display_parameters):
  trainset= display_parameters['trainset'][['Open','High','Low','Close','Adj Close','Volume']]
  ticker_name= display_parameters['ticker_name']
  trainset.sort_index(inplace=True, ascending=True)
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=trainset.index, y=trainset.Open,
                      mode='lines',
                      name='Open'))
  fig.add_trace(go.Scatter(x=trainset.index, y=trainset.High,
                      mode='lines',
                      name='High'))
  fig.add_trace(go.Scatter(x=trainset.index, y=trainset.Low,
                      mode='lines',
                      name='Low'))
  fig.add_trace(go.Scatter(x=trainset.index, y=trainset.Close,
                      mode='lines',
                      name='Close'))
  fig.add_trace(go.Scatter(x=trainset.index, y=trainset['Adj Close'],
                      mode='lines',
                      name='Adjusted Close'))
  fig.update_layout(
      title=ticker_name+' Stock Prices 2010-2019',
      hoverlabel=dict(
          bgcolor="white", 
          font_size=16, 
          font_family="Rockwell"
      )
  )
  fig.show()
  return

def forecast_price(display_parameters, prediction_list):
  testset= display_parameters['testset'][['Open','High','Low','Close','Adj Close','Volume']]
  testset.loc[:,'Predictions']= prediction_list
  print('Testset with predictions:\n', testset.head())
  fig = go.Figure()
  ticker_name= display_parameters['ticker_name']
  testset.sort_index(inplace=True, ascending=True)
  fig.add_trace(go.Scatter(x=testset.index, y=testset.Predictions,
                      mode='lines',
                      name='Forecasted Price'))
  fig.add_trace(go.Scatter(x=testset.index, y=testset['Adj Close'],
                      mode='lines',
                      name='Adjusted Close'))
  fig.update_layout(
      title=ticker_name+' - Forecasted Stock Prices for Year 2019 ',
      hoverlabel=dict(
          bgcolor="white", 
          font_size=16, 
          font_family="Rockwell"
      )
  )
  fig.show()
  display_parameters={'testset':testset,'ticker_name':ticker_name}
  return display_parameters

# def configure_plotly_browser_state():
#   import IPython
#   display(IPython.core.display.HTML('''
#         <script src="/static/components/requirejs/require.js"></script>
#         <script>
#           requirejs.config({
#             paths: {
#               base: '/static/base',
#               plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
#             },
#           });
#         </script>
#         '''))