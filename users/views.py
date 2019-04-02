from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

class Register(View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})

	def post(self, request):
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Your account has now been created! Please login to verify.', extra_tags='login')
			return redirect('login')

