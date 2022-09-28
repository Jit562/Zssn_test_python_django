from django.contrib import admin



from .models import Location,Survivor 

# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','created_at', 'updated_at','lat','long','survivor']

@admin.register(Survivor)
class SurvivorAdmin(admin.ModelAdmin):
    list_display = ['id','created_at', 'updated_at','name','age','gender']