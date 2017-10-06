# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                           "placeholder": "Имя *"}), label='Имя', max_length=150,
                           required=True)
    email = forms.EmailField(label="email", required=True, max_length=150,
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "placeholder": "Введите email *"}))
    phone = forms.CharField(max_length=100, label="Телефон",
                            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите телефон"}))
    message = forms.CharField(label="Сообщение", required=True,
                              widget=forms.Textarea(attrs={"class": "form-control",
                                                           "placeholder": "Введите вопрос *"}) )


