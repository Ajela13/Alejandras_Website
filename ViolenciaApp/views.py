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
    

    plotly_html = views.plotly_example(request).content.decode('utf-8')

    return render(request, 'home.html',{'plotly_html': plotly_html})

def project(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'project.html')
def linear_regression(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'linear_regression.html')
def logistic_regression(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'logistic_regression.html')
def ada_boost(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'ada_boost.html')
def decision_trees(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'decision_trees.html')
def k_means(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'k_means_clus.html')
def k_nearest_n(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'k_nearest_n.html')
def random_forest(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'random_forest.html')
def ridge_lasso_r(request):
    # Puedes personalizar esta lógica para cargar el contenido de la página nueva.
    return render(request, 'ridge_lasso_regression.html')
# En tu archivo views.py

def home_view(request):
    return render(request, 'home.html')  # Asegúrate de usar el nombre correcto aquí


from django.http import HttpResponse
from django.shortcuts import render
import os

def download_linear_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'CarPrice_Assignment_One_Var.csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)
    

def download_logistic_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'HR_Data.csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)
    

    
    
def download_kmeans_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'Mall_Customers.csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)




    
def download_knearest_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'breast_cancer_wisconsin.csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)


    
def download_decisiontree_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'prima-indians-diabetes.csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)

    
def download_randomforest_data(request):
    # Ruta al archivo CSV existente
    csv_path = os.path.join('archivos_csv', 'Sample Data for Random Forest (Heart Disease).csv')

    # Verificar si el archivo existe
    if os.path.exists(csv_path):
        # Abrir el archivo CSV y leer su contenido
        with open(csv_path, 'r') as csv_file:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(csv_path)}"'
            
            # Copiar el contenido del archivo CSV a la respuesta
            response.write(csv_file.read())

        return response
    else:
        # Manejar el caso en que el archivo no existe
        return HttpResponse("El archivo CSV no existe", status=404)




