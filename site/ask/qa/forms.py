#!/usr/bin/env python3
# coding=utf-8


from django import forms
from django.forms.widgets import HiddenInput
from django.contrib.auth.models import User
from .models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("title", "text")


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("text", "question")

        widgets = {
            "question": HiddenInput()
        }

        labels = {
            "text": u"Your Answer"
        }


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
