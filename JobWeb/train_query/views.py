from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def find_company_by_company_name(request, input_company_name):#, input_company_name
    response = "输入的公司名称为 %s"#%s
    return HttpResponse(response % input_company_name)#% input_company_name