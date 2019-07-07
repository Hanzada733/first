from django.db import models

class Saits(models.Model):
    name=models.CharField(verbose_name='Ваше имя',max_length=255)
    def __str__(self):
        return self.name
class Brands(models.Model):
    name=models.CharField(verbose_name='Ваше имя',max_length=255)
    def __str__(self):
        return self.name
class Marketing(models.Model):
    name=models.CharField(verbose_name='Ваше имя',max_length=255)
    def __str__(self):
        return self.name
# Create your models here.
class Order(models.Model):
    name=models.CharField(verbose_name='Ваше имя',max_length=255)
    phone=models.CharField(verbose_name='Ваше телефон',max_length=255,blank=True)
    email=models.EmailField(verbose_name='Ваше email')
    subject=models.TextField(verbose_name='Собщение',blank=True)
    sait=models.ManyToManyField(Saits,blank=True)
    brand=models.ManyToManyField(Brands,blank=True)
    marketing=models.ManyToManyField(Marketing,blank=True)

    def __str__(self):
        return self.name
class Brief(models.Model):
    contact_name_company=models.CharField(max_length=255)
    contact_info_name=models.CharField(max_length=255)
    contact_adress=models.CharField(max_length=255)
    contact_data_project=models.CharField(max_length=255)
    contact_were_see_us=models.CharField(max_length=255)
    contact_bissnes=models.CharField(max_length=255)
    contact_brend=models.CharField(max_length=255)
    contact_brend_perfect=models.CharField(max_length=255)
    contact_what_do=models.CharField(max_length=255)
    contact_marketing=models.CharField(max_length=255)
    contact_problem=models.CharField(max_length=255)
    contact_people=models.CharField(max_length=255)
    contact_concurents=models.CharField(max_length=255)
    contact_money=models.CharField(max_length=255)
    contact_menu_site=models.CharField(max_length=255)
    contact_servisess_site=models.CharField(max_length=255)
    contact_update_site=models.CharField(max_length=255)
    contact_risk_site=models.CharField(max_length=255)
    contact_mean_update=models.CharField(max_length=255)
    contact_site_list=models.CharField(max_length=255)
    contact_not_site_list=models.CharField(max_length=255)
    contact_new_site=models.CharField(max_length=255)
    contact_strategy=models.CharField(max_length=255)
    contact_site_strategy=models.CharField(max_length=255)
    contact_site_reclam=models.CharField(max_length=255)
    contact_site_seo=models.CharField(max_length=255)
    contact_site_social=models.CharField(max_length=255)
    contact_more_info=models.CharField(max_length=255)
    def __str__(self):
        return '{}-Брифинг'.format(self.id)
class Message(models.Model):
    name = models.CharField(verbose_name='Ваше имя', max_length=255)
    body = models.CharField(verbose_name='Текст', max_length=255, blank=True)
    email = models.EmailField(verbose_name='Ваше email')
    subject = models.TextField(verbose_name='Тема', blank=True)
    def __str__(self):
        return '{}-письмо'.format(self.id)
