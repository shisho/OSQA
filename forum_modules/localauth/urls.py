from django.conf.urls import *
from django.utils.translation import ugettext as _
import views as app

urlpatterns = patterns('',
    url(r'^%s%s%s$' % (_('account/'), _('local/'),  _('register/')), app.register, name='auth_local_register'),
)