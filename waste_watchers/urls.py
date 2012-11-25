from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def mk_url(pattern, template, name):
    return url(pattern, 'django.views.generic.simple.direct_to_template',
		{'template': template}, name=name)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'waste_watchers.views.home', name='home'),
    # url(r'^waste_watchers/', include('waste_watchers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    mk_url(r'^$', 'home.html', 'home'),
    mk_url(r'^about/$', 'about.html', 'about'),
    mk_url(r'^register/$', 'register.html', 'register'),
    mk_url(r'^got-waste/$', 'got-waste.html', 'got-waste'),
    mk_url(r'^where-the-action/$', 'wheres-the-action.html', 'wheres-the-action'),
)
