from django.db import models


# Create your models here.
class TrainCompany(models.Model):
    train_company_name = models.CharField(max_length=200)
    train_company_address_province = models.CharField(max_length=80) #省份
    train_company_address_city = models.CharField(max_length=80) #市
    train_company_address_area = models.CharField(max_length=80) #区
    train_company_address_info = models.CharField(max_length=500) #详细地址
    train_company_signcode = models.CharField(max_length=200) #特征码，作模糊查询使用
    is_effective = models.BooleanField(default=True) #是否有效

    def __str__(self):
        return self.train_company_name
    
    def to_string(self):
        return self.train_company_name + self.train_company_address_province + train_company_address_city 


class WorkPosition(models.Model):
    train_company = models.ForeignKey(TrainCompany, on_delete=models.CASCADE)
    work_position_name = models.CharField(max_length=200)
    work_position_type = models.CharField(max_length=80)
    work_position_salary = models.IntegerField(default=0)

    def __str__(self):
        return self.work_position_name
    
    def to_string(self):
        return self.work_position_name + self.work_position_type + self.work_position_salary