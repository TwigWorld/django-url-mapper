from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import URLMap

from .settings import URLMAPPER_ALLOWED_MAPPINGS


class URLMapAdmin(admin.ModelAdmin):
    list_display = ('key', 'mapping_type', 'get_url')

    fieldsets = [(None, {'fields': ('key',)})]
    if 'url' in URLMAPPER_ALLOWED_MAPPINGS:
        fieldsets.append((_("URL mapping"), {'fields': ('url',)}))
    if 'object' in URLMAPPER_ALLOWED_MAPPINGS:
        fieldsets.append((_("Object mapping"), {'fields': ('content_type', 'object_id')}))
    if 'view_name' in URLMAPPER_ALLOWED_MAPPINGS:
        fieldsets.append((_("View mapping"), {'fields': ('view_name', 'view_keywords')}))


admin.site.register(URLMap, URLMapAdmin)
