from django.contrib import admin
from .models import Theme, ImageMaterial, DocumentMaterial


#регистрируем в админке темы
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("t_name",)
    search_fields = ("t_name",)
    save_on_top = True
    save_as = True


#регистриуем в админке материал картинки
@admin.register(ImageMaterial)
class ImageMaterialAdmin(admin.ModelAdmin):
    list_display = ("im_name", "theme", "im_date",  )
    search_fields = ("im_name",)
    save_on_top = True
    save_as = True

#регистриуем в админке материал документ
@admin.register(DocumentMaterial)
class DocumentMaterialAdmin(admin.ModelAdmin):
    list_display = ("dm_name", "theme",  "dm_date", )
    search_fields = ("dm_name",)
    save_on_top = True
    save_as = True