from django import forms
from html5.forms.widgets import EmailInput, URLInput, SearchInput, DateInput, RangeInput

class DemoForm(forms.Form):
    title = forms.CharField(
        help_text=u'This is the standard text input',
    )
    email = forms.EmailField(
        help_text=u'This is the HTML5 e-mail input',
        widget=EmailInput()
    )
    url = forms.URLField(
        help_text=u'This is the HTML5 url input',
        widget=URLInput()
    )
    search = forms.CharField(
        help_text=u'This is the HTML5 search input',
        widget=SearchInput()
    )
    date = forms.DateField(
        help_text=u'This is the HTML5 date input',
        widget=DateInput()
    )
    range = forms.IntegerField(
        help_text=u'This is the HTML5 range input',
        widget=RangeInput()
    )
