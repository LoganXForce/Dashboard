

#Importamos nuestras dependencias#
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output

#Leemos los registros de nuestro archivo csv#
df = pd.read_csv('Covid19VacunasAgrupadas.csv')


#Consulta de informacion de los registros#
#print(df)
#print(df.vacuna_nombre.unique())
#print(df.vacuna_nombre.nunique())

#Diseño del Dashboard#
app = dash.Dash(__name__)
app.layout = html.Div([

    html.Div([
        html.H1('Vacunados contra el SARS-CoV-2. en Argentina'),
        html.Img(src='assets/vacuna.png')
    ], className = 'banner'),

#Diseño de ventana de seleccion de dosis de vacunacion#
    html.Div([
        html.Div([
            html.P('Seleccione la dosis que desea conocer', className= "fix_label", style={'color':'black', 'margin-top': '4px'}),
            dcc.RadioItems (id = 'dosis-radioitems',
            labelStyle = {'display': 'inline-block'},
            options= [
                {'label': 'Primera Dosis','value':'primera_dosis_cantidad'},
                {'label': 'Segunda Dosis','value':'segunda_dosis_cantidad'},
            ],
                value= 'primera_dosis_cantidad',
                style = {'text-aling':'center', 'color':'black'}, className='dcc_compon'
            ),
        ],
            className= 'create_container2 five columns', style={'margin-bottom':'20px'}
            ),
    ],
        className='row flex-display'
    ),
#Diseño de graficas que se implementan#
   html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),
    ], id='mainContainer', style={'display':'flex', 'flex-direction':'column'}
)

#Vista y consulta de datos respecto a la primera dosis#
@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):

    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame = df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad')
    return fig

#Vista y consulta de datos respecto a la segunda dosis#
@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph_pie(value):

    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'primera_dosis_cantidad')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'segunda_dosis_cantidad'
        )
    return fig2

if __name__ == ('__main__'):
    app.run_server(debug=True)