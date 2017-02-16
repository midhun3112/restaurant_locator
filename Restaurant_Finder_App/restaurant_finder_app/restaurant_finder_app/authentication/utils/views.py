# authentication/views.py

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from authentication.models import User
from authentication.utils.forms import RegistrationForm, UserProfileForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect


@csrf_protect
def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['firstname'],
                last_name=form.cleaned_data['lastname']
            )
            return HttpResponseRedirect('/authentication/register/success/')
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
        'registration/registration_success.html',
    )


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(
            request.POST, instance=request.user.user_profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, _(
                'Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserCreationForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.user_profile)
    return render(request, 'profile/user_profile.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form
    })
