from django.shortcuts import render,get_object_or_404
from new.models import *
from new.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.
def index(request):
    form=OrderForm()
    saits=Saits.objects.all()
    brands=Brands.objects.all()
    marketings=Marketing.objects.all()
    if request=='POST':
        print(request)
    return render(request,'index.html',locals())
def reg(request):
    brands=request.POST.getlist('brand')
    sites=request.POST.getlist('site')
    marketing=request.POST.getlist('marketing')
    if request.method=='POST':
        Order.objects.create(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),subject=request.POST.get('message'))
        order=Order.objects.last()

        for i in brands:
            Brand = get_object_or_404(Brands, id=i)
            order.brand.add(Brand)
        for i in sites:
            Site = get_object_or_404(Saits, id=i)
            order.sait.add(Site)
        for i in marketing:
            Market = get_object_or_404(Marketing, id=i)
            order.marketing.add(Market)
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))
def brief(request):
    return render(request,'brief.html')
from django.http import HttpResponse
def brief_form(request):

    if request.method=='POST':
        Brief.objects.create(
            contact_name_company=request.POST.get('contact_name_company'),
        contact_info_name = request.POST.get('contact_info_name'),
        contact_adress = request.POST.get('contact_adress'),
        contact_data_project = request.POST.get('contact_data_project'),
        contact_were_see_us = request.POST.get('contact_were_see_us'),
        contact_bissnes = request.POST.get('contact_bissnes'),
        contact_brend = request.POST.get('contact_brend'),
        contact_brend_perfect = request.POST.get('contact_brend_perfect'),
        contact_what_do = request.POST.get('contact_what_do'),
        contact_marketing = request.POST.get('contact_marketing'),
        contact_problem = request.POST.get('contact_problem'),
        contact_people = request.POST.get('contact_people'),
        contact_concurents = request.POST.get('contact_concurents'),
        contact_money = request.POST.get('contact_money'),
        contact_menu_site = request.POST.get('contact_menu_site'),
        contact_servisess_site = request.POST.get('contact_servisess_site'),
        contact_update_site = request.POST.get('contact_update_site'),
        contact_risk_site = request.POST.get('contact_risk_site'),
        contact_mean_update = request.POST.get('contact_mean_update'),
        contact_site_list = request.POST.get('contact_site_list'),
        contact_not_site_list = request.POST.get('contact_not_site_list'),
        contact_new_site = request.POST.get('contact_new_site'),
        contact_strategy = request.POST.get('contact_strategy'),
        contact_site_strategy = request.POST.get('contact_site_strategy'),
        contact_site_reclam = request.POST.get('contact_site_reclam'),
        contact_site_seo = request.POST.get('contact_site_seo'),
        contact_site_social = request.POST.get('contact_site_social'),
        contact_more_info = request.POST.get('contact_more_info'),


        )
        return HttpResponseRedirect(reverse('brief'))
    return HttpResponse(request)
from django.conf import settings
def message_form(request):
    if request.method == 'POST':
        Message.objects.create(
            name=request.POST.get('name'),
        body = request.POST.get('message'),
        email =request.POST.get('email'),
        subject = request.POST.get('subject'),
        )
        send_mail('Тема', request.POST.get('name'), settings.EMAIL_HOST_USER, [request.POST.get('email')])

    return HttpResponseRedirect(reverse('home'))
