# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 23:15:48 2022

@author: Rafael
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm

class FormUser(UserCreationForm):
    username=forms.CharField(label='Utilizador', min_length=5, max_length=150)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)
    

    