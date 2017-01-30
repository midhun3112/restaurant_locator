# authentication/views.py

# Create your views here.
from authentication.utils.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
 
@csrf_protect
def register(request):
    print('dudey')
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('dudey')
        if form.is_valid():
            print('dudey')
            user = User.objects.create_user(
            email =form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            firstname=form.cleaned_data['firstname'],
            lastname=form.cleaned_data['lastname']
            )
            return HttpResponseRedirect('/register/success/')
    # else:
    #     form = RegistrationForm()

    # variables = RequestContext(request, {
    # 'form': form
    # })
    context = {
        'form': form
    }
    return render(request, 'registration/registration_form.html', context)
 
    # return render_to_response(
    # 'registration/registration_form.html',
    # variables,
    # )
 
def register_success(request):
    return render_to_response(
    'registration/registration_success,html',
    )
  
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 