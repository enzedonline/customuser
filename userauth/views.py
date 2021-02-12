from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .forms import CustomUserUpdateForm
from .models import CustomUser

class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm

class CustomUserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('account_signup')

def profile_view(request):
    return render(request, 'account/profile.html')
