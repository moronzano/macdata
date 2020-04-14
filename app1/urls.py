from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', index),
    path('^swithes/$', SwithesView2.as_view(), name='SwithesView2'),
    #path('^SwithesView2/$', SwithesView2.as_view(), name='SwithesView2'),
    path('^dhcp/$', DhcpView.as_view(), name='DhcpView'),
    path('^mac-table/$', StoreMacView.as_view(), name='StoreMacView'),
    path('^mac-dhcp/$', MacDhcpView.as_view(), name='MacDhcpView'),
    path('^mac-table-search/$', StoreMacFilterView.as_view(),
         name='StoreMacFilterView'),
    path('^sw-menu/$', SwithesDetail.as_view(), name='SwithesDetail'),
    path(r'^<int:pk1>/<int:p1>', StoreMacView2.as_view(), name='StoreMacView2'),
    path(r'^sw-choice/$', SwChoiceView, name='SwChoiceView'),
    path(r'^sw-edit/<int:sw>$', SwEdit, name='SwEdit')
    #path(r'^(?P<pk1>\d+)', StoreMacView2.as_view(), name='StoreMacView2')
]
