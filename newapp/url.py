from django.conf.urls import url
from . import views

app_name='newapp'
urlpatterns = [
    url(r'^$',views.all_notes,name='all_notes'),
    url(r'^add$',views.add_note,name='add_note'),
    url(r'^(?P<slug>[-\w]+)$',views.details,name='details'),
    url(r'^(?P<slug>[-\w]+)/edit$',views.edit_note,name='edit_note'),

]
