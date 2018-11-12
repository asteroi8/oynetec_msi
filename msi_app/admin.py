from django.contrib import admin
from .models import System, Supplier, Site, SitePicture, Location, Country, Node, Install, Component

# Register your models here.
admin.site.register(Site)
admin.site.register(Location)
admin.site.register(SitePicture)
admin.site.register(Country)
admin.site.register(Node)
admin.site.register(Install)
admin.site.register(Component)
admin.site.register(Supplier)
admin.site.register(System)
