from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Student(request):
  data = request.POST
  print(data)
  students = [{'name':'Mustafa','roll_no':13,'age':19,'Class':11,'Address':'Shankar'},
              {'name':'Abdullah','roll_no':18,'age':18,'Class':13,'Address':'Chatto'},
              {'name':'Sara','roll_no':41,'age':15,'Class':12,'Address':'Mohib banda'},
              {'name':'Gulalai','roll_no':16,'age':13,'Class':10,'Address':'Peshawar'},
              {'name':'Amina','roll_no':36,'age':15,'Class':9,'Address':'Mardan'},
              {'name':'Jabir','roll_no':26,'age':15,'Class':13,'Address':'Charsadda'},
              {'name':'Zeenat','roll_no':20,'age':12,'Class':12,'Address':'Karachi'},
              {'name':'Saad','roll_no':10,'age':17,'Class':10,'Address':'Lahore'},
              ]
  
              
  return render(request,'home/student.html' ,context={'std':students})

