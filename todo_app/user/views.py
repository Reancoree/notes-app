from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from user.forms import RegisterForm
from user.service import send


@login_required
def profile_view(request):
    return render(request, 'user/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
