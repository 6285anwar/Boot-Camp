
from django.urls import path
from . import views

urlpatterns = [
    path('userpanel/',views.userpanel, name='userpanel'),
    
    path('login2page/',views.login2page, name='login2page'),
    path('signup2page/',views.signup2page, name='signup2page'),
    path('signup2/',views.signup2, name='signup2'),
    path('login2/',views.login2, name='login2'),

    path('courcetutorial/',views.courcetutorial, name='courcetutorial'),
    path('quiz/',views.quiz, name='quiz'),
    path('certificate/',views.certificate, name='certificate'),
    path('download/',views.download, name='download'),



   
    
]