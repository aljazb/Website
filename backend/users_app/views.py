from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from forms import RegisterForm, LoginForm
import re
import logging

logger = logging.getLogger(__name__)


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'users_app/register.html'

    def get(self, request):
        form = self.form_class(None)
        context = {
            'form': form,
            'warning': ''
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            name_pattern = re.compile('^[A-Z][-a-zA-Z]+$')
            username_pattern = re.compile('^(?=.{5,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')
            email_pattern = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
            password_pattern = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
            name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not name_pattern.match(name):
                context = {
                    'form': form,
                    'warning': 'Wrong first name (valid name example: John)'
                }
                return render(request, self.template_name, context)

            if not name_pattern.match(last_name):
                context = {
                    'form': form,
                    'warning': 'Wrong last name (valid name example: Doe)'
                }
                return render(request, self.template_name, context)

            if not username_pattern.match(username):
                context = {
                    'form': form,
                    'warning': 'Wrong username (valid username example: john_doe)'
                }
                return render(request, self.template_name, context)

            if not email_pattern.match(email):
                context = {
                    'form': form,
                    'warning': 'Wrong email (valid email example: john.doe@email.com)'
                }
                return render(request, self.template_name, context)

            if not password_pattern.match(password):
                context = {
                    'form': form,
                    'warning': 'Wrong password (Minimum 8 characters, at least 1 Alphabet and 1 Number)'
                }
                return render(request, self.template_name, context)

            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            logger.debug('[New user] username: ' + username)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')

        return render(request, self.template_name, {'form': form})


def login_form(request, redirect_link='home'):
    form_class = LoginForm
    template_name = 'users_app/login.html'
    redirect_link = clean_redirect_link(redirect_link)

    if request.method == 'GET':
        form = form_class(None)
        return render(request, template_name, {'form': form})
    elif request.method == 'POST':
        form = form_class(None)
        username = request.POST['username']
        password = request.POST['password']

        username_pattern = re.compile('^(?=.{5,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')
        password_pattern = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

        if not username_pattern.match(username):
            context = {
                'form': form,
                'warning': 'Wrong username (valid username example: john_doe)'
            }
            return render(request, template_name, context)

        if not password_pattern.match(password):
            context = {
                'form': form,
                'warning': 'Wrong password (Minimum 8 characters, at least 1 Alphabet and 1 Number)'
            }
            return render(request, template_name, context)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/' + redirect_link)

        context = {
            'form': form,
            'warning': 'Wrong username or password'
        }
        return render(request, template_name, context)


def logout_user(request, redirect_link='home'):
    logout(request)
    redirect_link = clean_redirect_link(redirect_link)
    return redirect('/' + redirect_link)


def clean_redirect_link(link):
    if link.count('redirect') > 0:
        link = 'home'
    return link
