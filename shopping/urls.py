from django.conf.urls import patterns, url
from shopping import views
from shopping.models import *


urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    
    #/shopping/new/
    url(r'^new/', views.create_shopping_item, name='create_shopping_item'),
    
    #shopping/id/delete
    url(r'^(?P<case_id>\d+)/delete/$', views.delete_shopping_item, name='delete_shopping_item'),
    
    #shopping/id/edit
    url(r'^(?P<case_id>\d+)/edit/$', views.edit_model, name="edit_model"),
                       )

