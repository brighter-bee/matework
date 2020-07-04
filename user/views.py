from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import RegisterForm
from profiles.models import User
from profiles.models import Person
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login


# Create your views here.
def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            user_id = get_object_or_404(User, username=username)
            person_ = Person(user=user_id, name=username)
            person_.save()
            login(response, new_user)
            return redirect("/profile/" + username)
        return redirect("/signup")
    else:
        form = RegisterForm()

    return render(response, "user/signup.html", {"form": form})
