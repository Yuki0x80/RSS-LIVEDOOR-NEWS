from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xmlprj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/','display.views.index',name='index'),
    url(r'^top/','display.views.top',name='top'),
    url(r'^dom/','display.views.dom', name='dom'),
    url(r'^inter/','display.views.inter', name='inter'),
    url(r'^eco/','display.views.eco', name='eco'),
    url(r'^ent/','display.views.ent', name='ent'),
    url(r'^spo/','display.views.spo', name='spo'),
    url(r'^movie/','display.views.movie', name='movie'),
    url(r'^gourmet/','display.views.gourmet', name='gourmet'),
    url(r'^trend/','display.views.trend', name='trend'),
    url(r'^love/','display.views.love', name='love'),
)
