from django.urls import path 
from app2.views import *
app_name='somthing2'

urlpatterns=[ 
    path('htmlfile_1/',htmlfile_1,name='htmlfile_1'),
    path('htmlfile_2/',htmlfile_2,name='htmlfile_2'),
]