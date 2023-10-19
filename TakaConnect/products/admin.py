from django.contrib import admin
from django.utils.html import format_html
from .models import Category, CategoryType, Location, MombasaProduct, KwaleProduct, LamuProduct, TanaRiverProduct, KilifiProduct
# Register your models here.

class ProductAdmin(admin.ModelAdmin): 
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:50px; height:50px"/>'.format(obj.image.url))

    list_display = ('id','image_tag','seller', 'quantity', 'contact','category','categorytype','color','location')
    search_fields =['seller', 'quantity', 'contact','category','categorytype','color','location']
    
    
admin.site.register(Category)
admin.site.register(CategoryType)
admin.site.register(Location)
admin.site.register(MombasaProduct,ProductAdmin)
admin.site.register(KilifiProduct,ProductAdmin)
admin.site.register(KwaleProduct,ProductAdmin)
admin.site.register(LamuProduct,ProductAdmin)
admin.site.register(TanaRiverProduct,ProductAdmin)