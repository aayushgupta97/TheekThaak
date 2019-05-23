from django.shortcuts import render
from django.views.generic.list import ListView
from core.models import Product, ProductImage
from django.db.models import Q






class ProductListView(ListView):
	model = Product
	template_name = "products/product_list.html"
	paginate_by = 3


	def get_queryset(self, *args, **kwargs):
		qs = Product.objects.all()
		query = self.request.GET.get("category", None)
		if query is not None:
			qs = qs.filter(Q(category__icontains=query) |
    			Q(sub_category__icontains=query)
    			)

		return qs


	def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['image']=[]

        # Add in a QuerySet of all the books
		# for object in context['object_list']:
		# 	object.image = Product.objects.filter(name=object.name).main_image
		# print(context['image'])
		for object in context['object_list']:
			#print(object.main_image)
			object.image = object.main_image
			print(object.image)
		
		return context



		# [{a,b,c,d},{a,b,c},{a,b,c}]