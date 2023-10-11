from django.urls import path
from . import views

#URLConf
urlpatterns=[
    path('', views.myWebsite),
    path('plotly-example/', views.plotly_example, name='plotly_example'),

]
