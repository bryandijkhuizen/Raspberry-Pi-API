from header import *

app = dash.Dash(__name__)

# perform an http get request to the server
# and get the data
df = pd.read_json('http://127.0.0.1:5000/data/get')

# get the amounts and the substance name out of the dataframe
amounts = df['amount'].tolist()
substances = df['substance'].tolist()

# create a new dataframe with the amounts and the substance name
df_amounts = pd.DataFrame({'substance': substances, 'amount': amounts,})



fig = px.bar(df_amounts, x='substance', y='amount',  
   barmode='group')
app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='''
   Dash: A web application framework for Python.
   '''),
   html.Button('Export Graph', id='export_graph_button', n_clicks=0),
   dcc.Graph(
      id='example-graph',
      figure=fig
   ),
   
]) 

if __name__ == '__main__':
   app.run_server(debug=True)
 


