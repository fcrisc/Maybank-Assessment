from django import forms

# creating a form
class DateTimeForm(forms.Form):
	dateTime_input = forms.DateTimeField( required=True, input_formats=["%Y-%m-%d %H:%M", ] )

