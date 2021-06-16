from django.contrib import admin

from django.contrib import admin
from .models import Function



class FunctionAdmin(admin.ModelAdmin):
    list_display=("function","graph_preview","interval","steps","updated")
    

    #function to display picture in admin site
    def graph_preview(self,obj):
        return obj.graph_preview

    graph_preview.short_description='graph preview'
    graph_preview.allow_tags= True
admin.site.register(Function,FunctionAdmin)
# Register your models here.


