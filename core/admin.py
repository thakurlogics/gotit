from django.contrib import admin
from .models import SiteSettings, Service, ContactMessage

admin.site.register(SiteSettings)
admin.site.register(Service)
admin.site.register(ContactMessage)