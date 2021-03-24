from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView


class BaseHomePage(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseHomePage.as_view(template_name='index.html'), name='home'),
]
