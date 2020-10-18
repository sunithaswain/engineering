from django.conf.urls import url

from . import views
from django.conf import settings

urlpatterns = [
    
    url(r'^regi/', views.regisin, name='registering'),
    url(r'^log/',views.login, name='logging'),
    # url(r'^$',views.indexing, name='indexing1'),
    url(r'^userprofile/(?P<user_id>[\d]+)',views.profile, name='userprofiles'),
    #url(r'^pass_chnge/',views.changingpassword, name='change_pwd'),
 
    # url(r'^out/',views.logoutin, name='logout')
    #url(r'^prof/', views.profile, name='profiling'),
    #url(r'^out/',views.logout, name='logouting'),
    #url(r'^alldata/',views.getalldetails, name='alldetails'),
    #url(r'^searchtext/',views.searchbutton,name='alldetails'),


    ]
