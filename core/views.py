from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm, LoginForm
from django.contrib.auth import login as auth_login
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
    'categories': categories,
    'items':items,})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            auth_login(request, form.get_user())
            return redirect('dashboard:index')  # Redirect after successful login
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {
        'form': form
    })