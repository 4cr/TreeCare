from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from watering.models import Suburb, WateringSession


def index(request):
    suburbs_list = Suburb.objects.order_by('name')
    watering_sessions_list = WateringSession.objects.all()
    context = {
        'suburbs_list': suburbs_list,
        'first_suburb': suburbs_list[0],
        'watering_sessions_list' : watering_sessions_list,
    }
    return render(request, 'watering/dashboard.html', context)

def addcomment(request):
    try:
        sub = Suburb.objects.get(pk=request.POST['suburb-number'])
        comment = request.POST['suburb-comment']
    except (KeyError, Suburb.DoesNotExist):
        return render(request, 'watering/dashboard.html', {
            'error_message': "You didn't entered a comment.",
        })
    else:
        sub.comment = comment
        sub.save()
        return HttpResponseRedirect(reverse('watering:index'))