from django.shortcuts import render
from .models import Product, ProductImage, Banner
from django.views.generic.list import ListView


class Index(ListView):
    model = Product
    template_name = "core/index.html"
    queryset = Product.objects.filter(is_featured=True).order_by('-id')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['image']=[]
        context['banners'] = Banner.objects.filter(is_active=True)
        context['latest_products'] = Product.objects.order_by("-id")[:9]

        # Add in a QuerySet of all the books
        # for object in context['object_list']:
        # object.image = Product.objects.filter(name=object.name).main_image
        # print(context['image'])
        for object in context['object_list']:
            # print(object.main_image)
            print(object)
            object.image = ProductImage.objects.filter(product=object).first().image

        for object in context['latest_products']:
            object.image = ProductImage.objects.filter(product=object).first().image

        return context
