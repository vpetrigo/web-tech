#!/usr/bin/env python3
# coding=utf-8


from django import forms
from .models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("title", "text", "author")


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("text", "question", "author")
