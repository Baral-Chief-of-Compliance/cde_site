from django.db import models
from datetime import date

#класс темы, в темах будут хранится различные материлы
class Theme(models.Model):
    t_name = models.CharField(verbose_name="Название темы по ГО и ЧС", max_length=512)
    t_desciption = models.TextField(verbose_name="Краткое описание темы", blank=True)

    def __str__(self) -> str:
        return self.t_name
    
    class Meta:
        verbose_name = "Тема ГО и ЧС"
        verbose_name_plural = "Темы ГО и ЧС"


#класс материлов картинок, там хранятся картинки
class ImageMaterial(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name="тема ГО и ЧС")
    im_name = models.CharField(verbose_name="название материала картинки", max_length=512)
    im_img = models.ImageField(verbose_name="файл кратинки",  upload_to='images_materials/')
    im_date = models.DateField(verbose_name="Дата публикации", default=date.today)

    def __str__(self) -> str:
        return self.im_name
    
    class Meta:
        verbose_name = "Материал (Картинка) к теме по ГО и ЧС"
        verbose_name_plural = "Материалы (Картинки) к теме по ГО и ЧС"


#класс метериалы pdf файлики
class DocumentMaterial(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name="тема ГО и ЧС")
    dm_name = models.CharField(verbose_name="название материала документа", max_length=512)
    document_path = models.FileField(verbose_name="файл документа", upload_to="documents_materials/")
    dm_date = models.DateField(verbose_name="Дата публикации", default=date.today)

    def __str__(self) -> str:
        return self.dm_name
    
    class Meta:
        verbose_name = "Материал (Документы) к теме по ГО и ЧС"
        verbose_name_plural = "Материалы (Документы) к теме по ГО и ЧС"
    
