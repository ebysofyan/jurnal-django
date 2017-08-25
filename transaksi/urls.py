from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<jurnal_id>\d+)$', views.ListTransaksiView.as_view(), name='view'),
    url(r'^simpan/(?P<jurnal_id>\d+)$', views.SimpanTransaksiView.as_view(), name='simpan'),
    url(r'^ubah/(?P<jurnal_id>\d+)/(?P<trx_id>\d+)$', views.UbahTransaksiView.as_view(), name='ubah'),
    url(r'^update/(?P<jurnal_id>\d+)$', views.UpdateTransaksiView.as_view(), name='update'),
    url(r'^hapus/(?P<jurnal_id>\d+)/(?P<trx_id>\d+)$', views.HapusTransaksiView.as_view(), name='hapus'),
]
