
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
    url(r'^todoapp$', views.index,name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/newtask/(?P<user_id>[0-9]+)$', views.new_task,name="newtask"),
    url(r'^tasks/create/(?P<user_id>[0-9]+)$', views.save_task,name="createtasks"),
    url(r'^tasks/(?P<user_id>[0-9]+)$', views.tasks,name="tasks"),
    url(r'^users/create/(?P<user_name>[A-za-z]+)$', views.create_user,name="createtasks"),
    url(r'^authenticate$', views.authenticate_user,name="authenticateusers"),
)
