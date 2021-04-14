"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
We are right now using function views here.
1. Empty url is never finished by '/'

2. Always a good habit to end the urlpattern(except empty url) with '/'
   It will make it to --> http://127.0.0.1:8000/polls/3/
   
   when user gives --> http://127.0.0.1:8000/polls/3 or http://127.0.0.1:8000/polls/3/

3. If you do not do then url will only run when user uses --> http://127.0.0.1:8000/polls/3
   It will fail if user writes --> http://127.0.0.1:8000/polls/3/
   
4. Another UrlConfigration means url of other app as it url change
  Ex: if you are in mysite app then your current location is http://127.0.0.1:8000/mysite.urls
  but you want to access urls of polls app then its address is http://127.0.0.1:8000/polls.urls
  thus you will need to use 'include' so that the address changes from 
  http://127.0.0.1:8000/mysite.urls --> http://127.0.0.1:8000/polls.urls
"""

from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
