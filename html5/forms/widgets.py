from django.forms import widgets as django_widgets

class DateInput(django_widgets.DateInput):
    input_type = 'date'

class TimeInput(django_widgets.TimeInput):
    input_type = 'time'

class DateTimeInput(django_widgets.DateTimeInput):
    input_type = 'datetime'

class NumberInput(django_widgets.TextInput):
    input_type = 'number'

class RangeInput(django_widgets.TextInput):
    input_type = 'range'

class EmailInput(django_widgets.TextInput):
    input_type = 'email'

class URLInput(django_widgets.TextInput):
    input_type = 'url'

class SearchInput(django_widgets.TextInput):
    input_type = 'search'