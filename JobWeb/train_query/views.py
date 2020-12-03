from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import generic




from .models import TrainCompany, WorkPosition
'''
# Create your views here.
def index(request):
    company_list = TrainCompany.objects.all()
    template = loader.get_template('train_query/index.html')
    context = {
        'company_list':company_list,
    }
    print(context)
    return HttpResponse(template.render(context, request))

def find_company_by_company_name(request, pk):#, input_company_name
    response = "输入的公司名称为 %s"#%s
    return HttpResponse(response % pk)#% input_company_name

def find_company_by_company_id(request, pk):#, input_company_name   
    company_info_list = TrainCompany.objects.all()
    if pk !='' and pk !=None:
        for i in company_info_list:
            if pk == i.id:
                company_info = i   
    work_position_list = WorkPosition.objects.filter(pk=company_info.id)
    response = "输入的公司信息为 %s"#%s
    company_info_text = company_info.train_company_name + company_info.train_company_address_province + company_info.train_company_address_city + company_info.train_company_address_area + company_info.train_company_address_info
    context = {
        'company_info':company_info_text,
        'work_position_list':work_position_list,
    }
    # return HttpResponse(response % context)#% input_company_name
    return render(request, 'train_query/company_info.html',context)


def find_position_by_position_id(request, pk):
    # temp_position = WorkPosition.objects.get(id=input_position_id)
    temp_position = get_object_or_404(WorkPosition, id=pk)

    return render(request, 'train_query/position_info.html', context={'temp_position':temp_position,})
'''
def commit_resume(request, temp_position_id):
    personal_info = request.POST['personal_info_name']
    return render(request, 'train_query/result.html',context={'result':personal_info,})   


class IndexView(generic.ListView):
    template_name = 'train_query/index.html'
    context_object_name = 'company_list'
    def get_queryset(self):
        return TrainCompany.objects.all()

class DetailView(generic.ListView):
    model = TrainCompany
    template_name = 'train_query/company_info.html'
    context_object_name = 'work_position_list'
    
    def get_queryset(self):
        print(self.kwargs[0])
        return WorkPosition.objects.filter(pk=self.kwargs[0])    