from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListJurnalView.as_view(), name='view'),
    url(r'^tambah/$', views.TambahJurnalView.as_view(), name='tambah'),
    url(r'^simpan/$', views.SimpanJurnalView.as_view(), name='simpan'),
    url(r'^edit/(?P<id>\d+)$', views.EditJurnalView.as_view(), name='edit'),
    url(r'^update/$', views.UpdateJurnalView.as_view(), name='update'),
    url(r'^hapus/(?P<id>\d+)$', views.HapusJurnalView.as_view(), name='hapus'),
]
