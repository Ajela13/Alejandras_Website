from django.urls import path
from . import views
from .views import home_view, project, logistic_regression,ada_boost,decision_trees,k_means,k_nearest_n,random_forest,ridge_lasso_r,download_logistic_data,download_kmeans_data,download_knearest_data,download_decisiontree_data,download_randomforest_data


#URLConf
urlpatterns=[
    path('', views.myWebsite,name='my_website'),
    path('plotly-example/', views.plotly_example, name='plotly_example'),
    path('', home_view, name='home_view'),
    path('project/', project, name='project'),
    path('LogisticRegression/', logistic_regression, name='logistic_regression'),
    path('AdaBoost/', ada_boost, name='ada_boost'),
    path('DecisionTrees/', decision_trees, name='decision_trees'),
    path('KMeans/', k_means, name='k_means'),
    path('KNearest/', k_nearest_n, name='k_nearest'),
    path('RandomForest/', random_forest, name='random_forest'),
    path('RidgeLassoRegression/', ridge_lasso_r, name='ridge_lasso_r'),
    path('descargar-logistic-csv/', download_logistic_data, name='download_logistic_data'),
    path('descargar-kmeans-csv/', download_kmeans_data, name='download_kmeans_data'),
    path('descargar-kmeans-csv/', download_knearest_data, name='download_knearest_data'),
    path('descargar-kmeans-csv/', download_decisiontree_data, name='download_decisiontree_data'),
    path('descargar-kmeans-csv/', download_randomforest_data, name='download_randomforest_data'),
]
