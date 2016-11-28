from django.conf.urls import include, url
from django.contrib.auth.views import login
from registration.views import *
from groupmanagement.views import *
from reports.views import *
from message.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
         url(r'^$', login),
         url(r'^logout/$', logout_page),
         url(r'^accounts/login/$', login),
         url(r'^register/$', register),
         url(r'^register/success/$', register_success),
         url(r'^home/$', home),
         url(r'^createGroup/$', createGroup),
         url(r'^admin/', admin.site.urls),
         url(r'^allusers/(.*)', displayUsers),
         url(r'^YourGroups/', viewGroups),
         url(r'^group/(.*)', groupActionsView),
         url(r'^addmember/', addMember),
         url(r'^removeMember', removeMember),
         url(r'^createReport/$', createReport),
         url(r'^messageHome/$', messageHome),
         url(r'^allMessages/$', displayMessage),
         url(r'^checkMessage/$', checkMessage),
         url(r'^createMessage/$', createMessage),
         url(r'^changeUserRoles/', changeUserRole),
         url(r'^updatePrivilege/', updatePrivilege)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
