from django.urls import path
from . import views
app_name='phapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('sup/',views.signup,name='sup'),
    path('log/',views.login,name='log'),
    path('gal/',views.gallery,name='gal'),
    path('detail/<int:id>',views.detail,name='detail'),
]