from django.contrib import admin

from website.models import Slider, Service, Package, Feature, Video, Contact, Subscriber, WebsiteSettings

# Register your models here.
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Package)
admin.site.register(Feature)
admin.site.register(Video)
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(WebsiteSettings)
