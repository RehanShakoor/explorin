from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.p_IndexView,name="p_index"),
    path('/page4',views.Page4View,name="page4"),
    path('/page3',views.Page3View,name="page3"),
    path('/page2',views.Page2View,name="page2"),
    path('button',views.ButtonView,name="button"),
    path('jqueryhw1',views.JqueryHw1,name="jqueryhw1"),
    path('jqueryhw2',views.JqueryHw2,name="jqueryhw2"),
]