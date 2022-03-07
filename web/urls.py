
from django.urls import path
from . import views

app_name = 'web'

urlpatterns=[
    path('',views.post_list,name="post_list"),
    path('<slug:slug>/',views.post_detail,name="post_detail"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
    path('p/<slug:slug>/',views.page,name="page"),
    path('contact',views.contact,name='contact'),
    path('query',views.search,name='search'),
    path('signup',views.handlesignup,name='signup'),
    path('login',views.loginhandle,name='login'),
    path('logout',views.logouthandle,name='logout'), 
    
]