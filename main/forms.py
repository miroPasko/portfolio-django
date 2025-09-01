from django import forms

class LinearRegressionForm(forms.Form):
    submitted_x = forms.IntegerField(label="Type your X to predict Y: ")