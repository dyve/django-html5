from django.shortcuts import render_to_response
from django.template.context import RequestContext
from html5_demo.forms import DemoForm

def index(request):
    if request.method == 'POST':
        form = DemoForm(request.POST)
        form.is_valid()
    else:
        form = DemoForm()
    return render_to_response('index.html', RequestContext(request, {
        'form': form,
    }))
