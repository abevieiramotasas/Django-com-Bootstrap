from django.shortcuts import render_to_response
from django.template import RequestContext

def oi(request):
    return render_to_response('oi.html', context_instance=RequestContext(request))
