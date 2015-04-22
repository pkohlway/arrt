from django.conf.urls import patterns, url


urlpatterns = patterns('art.views',
    url(r'^home/$', 'index', name='index'),
    url(r'^store/$', "store", name='store'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^detail/(?P<item_id>[0-9]+)/$', "detail", name='detail'),
    url(r'^checkout/(?P<item_id>[0-9]+)/$', "checkout", name='checkout'),
    url(r'^(?P<item_id>[0-9]+)/$', "order", name="order"),
)