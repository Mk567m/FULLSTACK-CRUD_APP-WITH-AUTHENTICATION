from django.shortcuts import render, redirect, get_object_or_404
from CrudApp.models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# running main prouducts page. Getting submission form data and then returning that data to tables 
@login_required(login_url='/login/')
def product(request):

  if request.method == 'POST':
    data = request.POST
    product_name = data.get('product_name')
    product_description = data.get('product_description')
    product_image = request.FILES.get('product_image')

    Product.objects.create(product_name=product_name
                        ,product_description=product_description
                        ,product_image=product_image)
    


    return redirect('/') 
  

    
  all_product= Product.objects.all()
  if request.GET.get('search_input'):
    all_product = all_product.filter(product_name__icontains=request.GET.get('search_input'))
  Context={'product':all_product} 
  return render(request,'home/product.html',context=Context)


######delete product button functionality
def delete_product(request,pk):
      product = Product.objects.get(id=pk)
      product.delete()
      Context={"product":product}
      
      return redirect('/',context=Context)


######## update button functionality
def update_product(request,pk):
  pdct =get_object_or_404(Product,id=pk)
  
  Context = {'update':pdct}
  
  if request.method=='POST':
    data = request.POST

    updated_name = data.get('product_name')
    updated_description = data.get('product_description')
    updated_image = request.FILES.get('product_image')
    print('-------------------',updated_image)

    

    pdct.product_name = updated_name
    pdct.product_description = updated_description
    pdct.product_image = updated_image
    
    pdct.save()

    return redirect('/')

  
  return render(request,'home/update.html',context=Context)


###### search functionality

#def search(request,product_name):
#  if request.method=='POST':
#    data = request.POST
#    search_input = data.get('search_input')
#    if data:
#      results = Product.objects.filter(product_name__icontains=search_input)
#    Context={'results':results}  
#  return redirect('/product/',context=Context)


import time


def login_view(request):
  if request.method=='POST':
    data = request.POST

    username = data.get('username')
    user_password = data.get('password')
    user_name = User.objects.filter(username=username)
    if not user_name.exists():
      messages.error(request,'Username does not exist! 🥺')
      return redirect('/login/')

    user = authenticate(username=username,password=user_password)
    if user is None:
      messages.error(request,'Wrong Password 🥺, Try again!')
      return redirect('/login/')
    else:
      login(request,user)
      
      time.sleep(1)
      return redirect('/')
  return render(request,'home/login.html')
      
def logout_view(request):
  logout(request)
  return redirect('/login/')

def register(request):
  
  if request.method=='POST':
    data = request.POST
    username = data.get('user_name')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    user = User.objects.filter(email = email)

    if user.exists():
      messages.error(request,'User with this email already exists!')
      return redirect('/register/')
    
    if data.get('password') == data.get('passwordagain'):
      passwordagain = data.get('passwordagain')
       
    else:
      messages.error(request,'Password do not match!')
      return redirect('/register/')  
    
   

  
    user = User.objects.create(username=username,first_name=first_name,last_name=last_name,
    email=email,password=password)
    


  return render(request,'home/register.html')
