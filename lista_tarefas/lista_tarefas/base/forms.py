from django import forms

# Reordenando Formulário e Visualização


class PositionForm(forms.Form):
    position = forms.CharField()
