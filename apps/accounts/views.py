from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required(login_url='/contas/login/')
def user_logout(request):
    logout(request)
    # return redirect('accounts:user_login')