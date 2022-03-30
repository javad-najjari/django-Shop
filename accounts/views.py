from django.shortcuts import redirect, render
from django.contrib.auth.views import LogoutView
from .forms import UserLoginForm, UserRegistrationForm
from django.views import View
from django.contrib.auth import authenticate, login, views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User



class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'باید ابتدا از حساب کاربری خود خارج شوید', 'warning')
            return redirect('store:home')
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            return redirect('store:home')
        
        messages.error(request, 'خطایی رخ داد : یا نام کاربری از قبل وجود دارد ، یا ایمیل از قبل وجود دارد ، یا رمز عبورها مشابه نیستند', 'warning')
        return render(request, self.template_name, {'form': form})




class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html', {'form': form})
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user != None:
                login(request, user)
                return redirect('store:home')
                
            return redirect('accounts:login')
        

class UserLogoutView(LogoutView):
    pass



# Reset Password
class UserResetPasswordView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

