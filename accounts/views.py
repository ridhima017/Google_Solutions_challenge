from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import QueryDict
import json
from urllib.parse import unquote
import urllib
from .models import recipe,gen_ins
# Create your views here.
def home(request):
    return render(request,'accounts/home2.html')
def about(request):
    return render(request,'accounts/about2.html')
def usermain(request):
    if request.method=='POST':
        
        height=request.POST['height']
        weight=request.POST['weight']
        age=request.POST['age']
        district=request.POST['district']
        gender=request.POST['gender']
        category=""
        print(request.POST)
        bmi = int(weight) / ((int(height)/100) ** 2)
        print(bmi)
        if gender.lower() == "male":
            if bmi < 18.5:
                category = "underweight"
            else:
                category = "healthy"
        elif gender.lower() == "female":
            if bmi < 18.5:
                category = "Underweight"
            else:
                category = "healthy"
        else:
            category = "Unknown gender"
        object_1=recipe.objects.filter(age=age)
        object_2=gen_ins.objects.filter(age=age)
        for obj in object_2:
            return render(request,'accounts/usermain.html',{'obj1':object_1,'instructions':obj.instructions,'food_items':obj.food_items,'mal_instructions':obj.mal_ins,'category':category})
def items_home(request):
    my_data = request.GET.get('data', '')
    object_1=recipe.objects.filter(recipe_name=my_data)
    for obj in object_1:
        return render(request,'accounts/item.html',{'recipe_name':my_data,'ins':obj.ins})