from django.urls import path
from . import views
urlpatterns=[
    path('abhi/',views.fn1,name='abhi'),
    path('xyz/',views.fn2,name='xyz'),
    path('pic/',views.fn3,name='pic'),
]