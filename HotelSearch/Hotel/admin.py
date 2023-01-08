from django.contrib import admin
from . models import Amenities,Hotels

# Register your models here.

# @admin.register(Amenities)

# class AmenitiesAdmin(admin.ModelAdmin):

#     list_display = ['name']
#     # pass

# @admin.register(Hotels)

# class HotelAdmin(admin.ModelAdmin):

    # list_display = ['hotel_name','hotel_desc','hotel_image','price','amenities']
    # list_display = '__all__'

admin.site.register(Amenities)
admin.site.register(Hotels)