from django.shortcuts import render, redirect
import time
from datetime import datetime
from warsztat.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.core.mail import EmailMessage  
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from warsztat.token import account_activation_token
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request=request,
                    template_name="home.html")
    
def account(request):
    return render(request=request,
                    template_name="account.html")
    
def contact(request):
    return render(request=request,
                    template_name="contact.html")
    

      
      

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get("password1"))
            login(request=request,user=user)
            return redirect("home")
    else:
        form=UserCreationForm()
    return render(request=request,
                template_name="signup.html",
                context={"form":form})
        


def hello(request):
    current_date=datetime.now()
    return render(request=request,
                    template_name="hello.html",
                    context={"current_date":current_date,
                    "snippet":"<b>grubo</b>"})


def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():  
            # save form in the memory not in database  
            new_user = form.save(commit=False)  
            new_user.is_active = False  
            new_user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
            'user': new_user,  
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),  
            'token':account_activation_token.make_token(new_user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                    mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  
    else:
        form = RegistrationForm()

    return render(request=request,
            template_name="signup.html",
            context={"form":form})    
    
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        new_user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        new_user = None  
    if new_user is not None and account_activation_token.check_token(new_user, token):  
        new_user.is_active = True  
        new_user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')      



def pchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            request.session.flush()
            logout(request)
            return redirect("home")
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form, }
    return render(request, 'pchange.html', context)  



@login_required()
def confirmemail(request):
  current_user = request.user
  recipient_list =  [current_user.email, ]
  message = render_to_string('summary_email.html', {  
            'user': current_user,  
            'last_name':current_user.last_name,
            'email':current_user.email,
            })  
  send_mail('Warsztat SerwisUS',message, from_email="warsztat.serwisus@gmail.com", recipient_list=recipient_list)
  time.sleep(3)
  return redirect("home") 