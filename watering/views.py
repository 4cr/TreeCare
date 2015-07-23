from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from watering.models import Suburb, WateringSession
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    suburbs_list = Suburb.objects.order_by('name')
    watering_sessions_list = WateringSession.objects.all()
    context = {
        'suburbs_list': suburbs_list,
        'first_suburb': suburbs_list[0],
        'watering_sessions_list' : watering_sessions_list,
    }
    return render(request, 'watering/dashboard.html', context)

@login_required
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


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "watering/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")