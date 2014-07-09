
from django.conf.urls import patterns, include, url
from todoapp import views
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^page1$', views.page1,name="good"),
    url(r'^toDoApp$', views.index,name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/create/(?P<task_name>[A-za-z]+)$', views.savetask,name="createtasks"),
    url(r'^tasks$', views.movies,name="movies"),
    url(r'^users/create/(?P<user_name>[A-za-z]+)$', views.createuser,name="createtasks"),
    url(r'^authenticate$', views.authenticate_user,name="authenticateusers"),
)
