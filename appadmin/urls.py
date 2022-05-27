from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/',views.dashbord, name='dashbord'),
    
    path('loginpage/',views.loginpage, name='loginpage'),
    path('signuppage/',views.signuppage, name='signuppage'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),



    path('platform1/',views.platform1, name='platform1'),
    path('platformadd/',views.platformadd, name='platformadd'),

    path('register/',views.register, name='register'),
    path('show/',views.show, name='show'),

    
    path('platformedit/<int:platformid>',views.platformedit, name='platformedit'),
    path('delete/<int:platformid>',views.delete, name='delete'),
    path('update/<int:platformid>',views.update, name='update'),


    path('cources/',views.cources, name='cources'),
    path('cshow/',views.cshow, name='cshow'),
    path('courceadd/',views.courceadd, name='courceadd'),

    path('register2/',views.register2, name='register2'),
    path('deletecource/<int:courceid>', views.deletecource, name='deletecource'),
    path('courceedit/<int:courceid>', views.courceedit, name='courceedit'),
    path('update2/<int:courceid>',views.update2, name='update2'),

    path('tutorials', views.tutorials, name='tutorials'),
    path('tutorialadd/', views.tutorialadd, name='tutorialadd'),
    path('register3', views.register3,name='register3'),

    path('qa/', views.qa,name='qa'),
    path('qashow/', views.qashow,name='qashow'),
    path('register4/', views.register4,name='register4'),
    path('deleteq/<int:questionsid>', views.deleteq, name='deleteq'),
    










]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)