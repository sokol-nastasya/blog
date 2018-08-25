from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


from account.forms import EditProfileForm

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string('account/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
				})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message, to=[to_email]
				)
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = SignupForm()
	return render(request, 'account/signup.html', {'form': form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			user.save()
			login(request, user)
			# return redirect('home')
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')


def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
										password=newuser_form.cleaned_data['password2'],
										)
			auth.login(request, newuser)
			return redirect(reverse('account:prof'))
		else:
			args['form'] = newuser_form
	return render_to_response('account/register.html', args)


def prof(request, pk=None):
	storege = messages.get_messages(request)
	if pk:
		user = User.objects.get(user = request.user, pk=pk)
	else:
		user = request.user
	args = {'user':user, 'messages':messages}
	return render(request, 'account/prof.html')

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form':form}
		return render(request, 'account/edit_prof.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('account:profile')
		else:
			return redirect('account:change-password')
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form}
		return render(request, 'account/change_password.html', args)

