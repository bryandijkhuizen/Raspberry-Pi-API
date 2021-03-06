# import the header file
from header import *

# create a new Dash app
app = dash.Dash(__name__)

# perform an http get request to the server
# and get the data
df = pd.read_json('http://127.0.0.1:5000/data/get')

# get the amounts and the substance name out of the dataframe
amounts = df['amount'].tolist()
substances = df['substance'].tolist()
danger_levels = df['danger_level'].tolist()
timestamps = df['time_stamp'].tolist()

# create a new dataframe with the amounts and the substance name
df_amounts = pd.DataFrame({'time': timestamps, 'danger': danger_levels,})

# create a new figure
fig = px.bar(df_amounts, x='time', y='danger',  
   barmode='group')

# display the figure in an html div
app.layout = html.Div(children=[
   html.H1(children='Rookbot Dashboard'),
   html.Div(children='''
   Gedane metingen van de luchtkwaliteit in de buurt van de Rookbot.
   '''),
   html.Button('Export Graph', id='export_graph_button', n_clicks=0),
   dcc.Graph(
      id='example-graph',
      figure=fig
   ),
   
]) 

export_graph(fig, 'example_graph', 'png')

# run the app
if __name__ == '__main__':
   app.run_server(debug=True)
 


