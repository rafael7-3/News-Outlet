# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:12:54 2022

@author: Rafael
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registo', views.registo, name='registo'),
    path('<int:Noticia_id>/', views.detalhe, name='detalhe'),
    path('comentario/<int:Noticia_id>', views.comentario, name='comentario'), 
    path('fim', views.fim, name='fim'), 
    ]