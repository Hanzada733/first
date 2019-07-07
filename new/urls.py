
from django.urls import path,include
from new import views

urlpatterns = [
path('',views.index,name='home'),
path('req',views.reg,name='reg'),
    path('brief',views.brief,name='brief'),
    path('brief_form',views.brief_form,name='brief_form'),
    path('message_form',views.message_form,name='message_form')
]
