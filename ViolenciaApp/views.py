from django.shortcuts import render
from django.http import HttpResponse

from urllib.request import urlopen
import json 
from django.http import JsonResponse

from unidecode import unidecode
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from . import views
from ViolenciaApp.models import Dane
from ViolenciaApp.models import Geojason




# Create your views here.


def plotly_example(request):
    # Datos para el gráfico
    data = [go.Bar(
        x=['Manzanas', 'Plátanos', 'Peras', 'Uvas'],
        y=[15, 12, 10, 8]
    )]

    # Configuración del diseño del gráfico
    layout = go.Layout(
        title='Ejemplo de Gráfico de Barras con Plotly ',
        xaxis=dict(title='Frutas'),
        yaxis=dict(title='Cantidad')
    )

    # Crear la figura del gráfico
    fig = go.Figure(data=[
        go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 4, 8, 16], mode='lines')
    ],
    layout=go.Layout(
        height=300,  # Set the height here
        title='Plotly Graph Example'
    ))

    # Generar el gráfico en formato HTML
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    
    return render(request, 'plotly_example.html', {'plot_div': plot_div})

# def map(request):
#     #geojeason to plot country
#     with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
#         colombia = json.load(response)

#     df=pd.read_csv(r"C:\Users\aleja\Downloads\Violence\Reporte_Delito_Violencia_Intrafamiliar_Polic_a_Nacional.csv")
#     df=df.replace('GUAJIRA','LA GUAJIRA')
#     df=df.replace('VALLE','VALLE DEL CAUCA')
#     df=df. drop(df.index[df['DEPARTAMENTO'] == 'NO REPORTA'])

#     colombia_dep_map={}
#     for feature in colombia['features']:
#         feature['id']=feature['properties']['DPTO']
#         colombia_dep_map[unidecode(feature['properties']['NOMBRE_DPT'])]=feature['id']


#     #changing name in order to have the same name in dic and jason file
#     colombia_dep_map['SAN ANDRES'] = colombia_dep_map['ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA']
#     del colombia_dep_map['ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA']
#     #print(colombia_dep_map)


#     # Creating pivot_table of quantity
#     pivot_df = pd.pivot_table(df, index='DEPARTAMENTO', values='CANTIDAD', aggfunc=np.sum).reset_index()
#     #print(pivot_df)
#     #creating new column in pivot table to identify departments by id

#     pivot_df['ID']=pivot_df['DEPARTAMENTO'].apply(lambda x:colombia_dep_map[unidecode(x)])
#     #print(pivot_df)
#     pivot_df['CANTIDADSCALE']=np.log10(pivot_df['CANTIDAD'])

#     #plotting map 
#     fig=px.choropleth_mapbox(pivot_df,locations='ID',geojson=colombia,color='CANTIDADSCALE',hover_name='DEPARTAMENTO',hover_data=['CANTIDAD'],mapbox_style='carto-positron',center={'lat':4,'lon':-74},zoom=4)
#     fig.update_geos(fitbounds='locations',visible=False)
#     plot_divmap = plot(fig, output_type='div', include_plotlyjs=False)

#     return HttpResponse(fig.to_html(), content_type='text/html')
    

def map2(request):

    registros = Dane.objects.all()
    df = pd.DataFrame(list(registros.values()))
    df=df.replace('GUAJIRA','LA GUAJIRA')
    df=df.replace('VALLE','VALLE DEL CAUCA')
    df=df. drop(df.index[df['DEPARTAMENTO'] == 'NO REPORTA'])
    
    col_data = Geojason.objects.all()[0]
    colombia=col_data = {
            'type': col_data.type,
            'crs': col_data.crs,
            'features': col_data.features,
        }
    colombia_dep_map={}
    for feature in colombia['features']:
        feature['id']=feature['properties']['DPTO']
        colombia_dep_map[unidecode(feature['properties']['NOMBRE_DPT'])]=feature['id']


    #changing name in order to have the same name in dic and jason file
    colombia_dep_map['SAN ANDRES'] = colombia_dep_map['ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA']
    del colombia_dep_map['ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA']
    #print(colombia_dep_map)


    # Creating pivot_table of quantity
    pivot_df = pd.pivot_table(df, index='DEPARTAMENTO', values='CANTIDAD', aggfunc=np.sum).reset_index()
    #print(pivot_df)
    #creating new column in pivot table to identify departments by id

    pivot_df['ID']=pivot_df['DEPARTAMENTO'].apply(lambda x:colombia_dep_map[unidecode(x)])
    #print(pivot_df)
    pivot_df['CANTIDADSCALE']=np.log10(pivot_df['CANTIDAD'])

    #plotting map 
    fig=px.choropleth_mapbox(pivot_df,locations='ID',geojson=colombia,color='CANTIDADSCALE',hover_name='DEPARTAMENTO',hover_data=['CANTIDAD'],mapbox_style='carto-positron',center={'lat':4,'lon':-74},zoom=4)
    fig.update_geos(fitbounds='locations',visible=False)
    plot_divmap = plot(fig, output_type='div', include_plotlyjs=False)

    return HttpResponse(fig.to_html(), content_type='text/html')





def myWebsite(request):
    # fig = map(request)

    # # Convert the Plotly figure to HTML
    # fig_html = fig.to_html()

    plotly_html = views.plotly_example(request).content.decode('utf-8')

    return render(request, 'home.html',{'plotly_html': plotly_html})

def logisticRegression(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'logistic_regression.html')