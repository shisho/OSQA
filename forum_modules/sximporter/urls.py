from django.conf.urls import *
from django.utils.translation import ugettext as _

from views import sximporter

urlpatterns = patterns('',
    url(r'^%s%s$' % (_('admin/'), _('sximporter/')),  sximporter, name='sximporter'),
)