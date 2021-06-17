from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home, expenses, about, contact, get_name, get_amount, planowanie, przychody, enter_the_cost, enter_the_income, statement
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('home', home, name='home'),
                  path('expenses', expenses, name='Wydatki'),
                  path('about', about, name='O-nas'),
                  path('contact', contact, name='Kontakt'),
                  path('name', get_name, name='Name'),
                  path('kwota', get_amount, name='Formularz Wydatków'),
                  path('planowanie', planowanie, name="Planowanie wydatków"),
                  path('przychody', enter_the_income, name="Przychody w domowym budżecie"),
                  path('categories', enter_the_cost, name="Kategorie budżetu domowego"),
                  path('wydatki', enter_the_cost, name="Kategorie budżetu domowego"),
                  path('statement', views.display, name="Zestawienie"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
