from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Student.models import *
import os

# Create your views here.
# running main prouducts page. Getting submission form data and then returning that data to tables 
def product(request):

  if request.method == 'POST':
    data = request.POST
    product_name = data.get('product_name')
    product_description = data.get('product_description')
    product_image = request.FILES.get('product_image')

    Product.objects.create(product_name=product_name
                        ,product_description=product_description
                        ,product_image=product_image)
    


    return redirect('/product/') 

    
  all_product= Product.objects.all()
  if request.GET.get('search_input'):
    all_product = all_product.filter(product_name__icontains=request.GET.get('search_input'))
  Context={'product':all_product} 
  return render(request,'home/product.html',context=Context)


######delete product button functionality
def delete_product(request,id):
      product_data = get_object_or_404(Product,id = id)
      product_data.delete()
              
      return redirect('/product/')


######## update button functionality
def update_product(request,id):
  pdct =Product.objects.get(id=id)
  Context = {'update':pdct}
  
  if request.method=='POST':
    data = request.POST

    updated_name = data.get('product_name')
    updated_description = data.get('product_description')
    updated_image = request.FILES.get('product_image')

    pdct.product_name = updated_name
    pdct.product_description = updated_description
    pdct.product_image = updated_image
    
    pdct.save()

    return redirect('/product/')

  
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



def student_data(request):
  if request.method == 'POST':
    # Handle the form submission
    # You can access the form data using request.POST
    data= request.POST
    student_name = data.get('name')
    student_age = data.get('age')
    student_address = data.get('address')

    ####showing data on terminal that has been sent to server or database.############
    print(student_name)
    print(student_age)
    print(student_address)
    ###############################


    ###Creates a new student record in the database from website form directly.
    Student_model.objects.create(name = student_name,
                                 address =student_address,
                                 age=student_age
                                 )
    ##################################
    
    return redirect('/')
    
    ######### Here you can save the data to the database if needed
  students = [{'name':'Mustafa','roll_no':13,'age':19,'Class':11,'Address':'Shankar'},
              {'name':'Abdullah','roll_no':18,'age':18,'Class':13,'Address':'Chatto'},
              {'name':'Sara','roll_no':41,'age':15,'Class':12,'Address':'Mohib banda'},
              {'name':'Gulalai','roll_no':16,'age':13,'Class':10,'Address':'Peshawar'},
              {'name':'Amina','roll_no':36,'age':15,'Class':9,'Address':'Mardan'},
              {'name':'Jabir','roll_no':26,'age':15,'Class':13,'Address':'Charsadda'},
              {'name':'Zeenat','roll_no':20,'age':12,'Class':12,'Address':'Karachi'},
              {'name':'Saad','roll_no':10,'age':17,'Class':10,'Address':'Lahore'},
              ]
  #################################
  


  return render(request,'home/std.html',{'students':students})
def generate_price():
    prices = {'Nvidia GTX 960 4gb':20000,
              'Nvidia GTX 1050 ti':25000,
              'Nvidia GTX 1060 6gb':30000,
              'Amd RX 580 8gb Nitro':28000,
              'Intel Arc B580 12GB':80000,
              'AMD RX 6600 XT 12GB':60000,
              'Nvidia GTX 1660 Super 6gb': 45000,
              'Nvidia RTX 2060 Super 8gb':53000
                           }
    #Generate price in placeholder
    