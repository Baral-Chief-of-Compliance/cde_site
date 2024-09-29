from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Theme, ImageMaterial, DocumentMaterial
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

BASE_PATH : str = 'cde_site'

#главная страница где все темы
def index(request) -> HttpResponse:
    themes_result : list = []
    themes = Theme.objects.order_by("t_name")

    for t in themes:
        themes_result.append({
            "t_id": t.id,
            "t_name": t.t_name
        })

    return render(
        request=request,
        template_name=f'{BASE_PATH}/index.html',
        context={
            "themes": themes_result
        }
    )

#получение информации об одной странице (картинки и документы)
def theme_info(request, t_id : int) -> HttpResponse:
    theme = get_object_or_404(Theme, pk=t_id)

    #получаем все картинки
    images_result : list = []
    imageMaterials = ImageMaterial.objects.filter(theme__id=t_id).order_by('-im_date')

    for im in imageMaterials:
        images_result.append(
            {
                "im_id": im.id,
                "im_name": im.im_name,
                "im_date": im.im_date
            }
        )

    #получаем все документы 
    documents_result : list = []
    documentMaterial = DocumentMaterial.objects.filter(theme__id=t_id).order_by('-dm_date')

    for d in documentMaterial:
        documents_result.append(
            {
                "dm_id": d.id,
                "dm_name": d.dm_name,
                "dm_date": d.dm_date,
                "dm_path": d.document_path.url
            }
        )

    return render(
        request=request,
        template_name=f"{BASE_PATH}/theme_details.html",
        context={
            "t_id": theme.id,
            "t_name": theme.t_name,
            "t_desciption": theme.t_desciption,
            "images" : images_result,
            "documents" : documents_result
        }
    )

#получить картинку
def theme_info_img(request, t_id: int, im_id: int) -> HttpResponse:
    image = get_object_or_404(ImageMaterial, pk=im_id)

    return render(
        request=request,
        template_name=f"{BASE_PATH}/img_info.html",
        context={
            "t_id": t_id,
            "im_name": image.im_name,
            "im_img": image.im_img.url,
            "im_date": image.im_date
        }
    )

#получить документ
@xframe_options_exempt
def theme_info_document(request, t_id: int, dm_id: int) -> HttpResponse:
    document = get_object_or_404(DocumentMaterial, pk=dm_id)
    print(document.document_path)

    return render(
        request=request,
        template_name=f"{BASE_PATH}/document_info.html",
        context={
            "t_id": t_id,
            "dm_name": document.dm_name,
            "dm_document_path": f"/media/{document.document_path}",
            "dm_date": document.dm_date
        }
    )



