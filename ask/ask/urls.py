from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ask.views.test', name='home'),
    url(r'^login/', 'ask.views.test', name='login'),
    url(r'^signup/', 'ask.views.test', name='signup'),
    url(r'^question/', include('qa.urls'), name='question'),
    url(r'^ask/', 'ask.views.test', name='ask'),
    url(r'^popular/', 'ask.views.test', name='popular'),
    url(r'^new/', 'ask.views.test', name='new'),

    url(r'^admin/', include(admin.site.urls)),
)
