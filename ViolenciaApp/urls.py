from django.urls import path
from . import views
from .views import home_view, logisticRegression


#URLConf
urlpatterns=[
    path('', views.myWebsite,name='my_website'),
    path('plotly-example/', views.plotly_example, name='plotly_example'),
    path('Home/', home_view, name='home_view'),
    path('logisticRegression/', logisticRegression, name='logistic_regression'),

]
