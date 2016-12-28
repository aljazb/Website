from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from forms import UserForm


class UserFormView(View):
    form_class = UserForm
    template_name = 'users_app/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            print('ndsdsd')
            user = form.save(commit=False)
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home')

        return render(request, self.template_name, {'form': form})
