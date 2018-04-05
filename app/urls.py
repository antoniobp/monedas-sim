from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^logout', views.auth_logout),
    url(r'^usuarios/$', views.usuario_lista, name='usuario_lista'),
    url(r'^usuarios/(?P<id_user>\w+)/$', views.usuario_datos, name='usuario_datos'),
    url(r'^operaciones/(?P<id_user>[0-9]+)/(?P<tipo_operacion>[0-9]+)/$', views.operacion_lista, name='operacion_lista'),
    url(r'^monedas/$', views.moneda_lista, name='moneda_lista'),
]
