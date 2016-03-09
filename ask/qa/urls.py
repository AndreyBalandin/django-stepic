from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^question/(?P<id>\d+)/', 'question', name='question'),
    url(r'^$', 'test', name='home'),
    url(r'^login/', 'test', name='login'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^ask/', 'test', name='ask'),
    url(r'^popular/', 'test', name='popular'),
    url(r'^new/', 'test', name='new'),

    )
