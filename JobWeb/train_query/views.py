from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TrainCompany, WorkPosition


# Create your views here.
def index(request):
    company_list = TrainCompany.objects.all()
    template = loader.get_template('train_query/index.html')
    context = {
        'company_list':company_list,
    }
    print(context)
    return HttpResponse(template.render(context, request))

def find_company_by_company_name(request, input_company_name):#, input_company_name
    response = "输入的公司名称为 %s"#%s
    return HttpResponse(response % input_company_name)#% input_company_name

def find_company_by_company_id(request, input_company_id):#, input_company_name   
    company_info_list = TrainCompany.objects.all()
    if input_company_id !='' and input_company_id !=None:
        for i in company_info_list:
            if input_company_id == i.id:
                company_info = i   
    work_position_list = WorkPosition.objects.filter(train_company__id=company_info.id)
    response = "输入的公司信息为 %s"#%s
    company_info_text = company_info.train_company_name + company_info.train_company_address_province + company_info.train_company_address_city + company_info.train_company_address_area + company_info.train_company_address_info
    context = {
        'company_info':company_info_text,
        'work_position_list':work_position_list,
    }
    # return HttpResponse(response % context)#% input_company_name
    return render(request, 'train_query/company_info.html',context)


def find_position_by_position_id(request, input_position_id):
    return render(request, 'train_query/position_info.html', context='pass')