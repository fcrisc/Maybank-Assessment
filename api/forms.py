from django import forms

# creating a form
class DateTimeForm(forms.Form):
	dateTime_input = forms.DateTimeField( )

