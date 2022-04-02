from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {
        "form" : form
    }

    return render(request, "users/register.html", context)





def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    
    return render(request, "users/login.html")




def logout_page(request):
    logout(request)
    return redirect("users:login")



