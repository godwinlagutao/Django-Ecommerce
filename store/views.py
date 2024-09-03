from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, CustomPasswordChangeForm
from .models import Product, Category
from django.contrib.auth import authenticate, login,logout # for login and authenticating users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Create your views here.    
def category(request, foo):
    # Replace Hyphens with spaces
    foo = foo.replace('-', ' ')
    # Grab the category from the url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
        
    except:
        messages.success(request, ("Category doesn't exist"))
        return redirect('home')
    

def product(request, pk):
    product = Product.objects.get(id=pk) #gets a specific product with a unique primary key
    return render(request, 'product.html', {'product':product})


def home(request):
    products = Product.objects.all() #gets everything in the Products model and puts it in the variable 'products'
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST": # if they filled out the form, do the following
        
        username = request.POST['username'] #username because that's the name we gave our html input tag in login.html
        password = request.POST['password'] #same thing
        user = authenticate(request,username=username,password=password) #authenticates the username and password into the db
        
        if user is not None:
            login(request,user) #if the user is not none, then login the user
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        
        else:
            messages.success(request, ("There was an error, pls try again"))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})        

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out, Thanks for stopping by"))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
        
    return render(request, 'home.html', {'products': products})
    

@login_required
def update_user(request):
    user_form = UserUpdateForm(instance = request.user)
    password_form = CustomPasswordChangeForm(request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile and password were successfully changed')
            return redirect('update_user')
        else:
            messages.error(request, 'Please correct the errors below.')
        
    return render(request, 'update_user.html', {
        'form': user_form,
        'password_form': password_form
    })
   
