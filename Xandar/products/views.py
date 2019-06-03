from operations.views import add_to_cart
from django.shortcuts import render
from django.views.generic.list import ListView
from core.models import Product, ProductImage, Attribute, CATEGORY_CHOICES, SUB_CATEGORY_CHOICES
from django.db.models import Q
from django.views.generic import DetailView
#from operations.cart import add_cart
from operations.views import add_wishlist_item
from django.http import HttpResponse
from core.models import Wishlist
from core.get_data import *


class ProductListView(ListView):

	model = Product
	template_name = "products/product_list.html"


# paginate_by = 3


	def get_queryset(self, *args, **kwargs):


		qs = Product.objects.all()
		query = self.request.GET.get("category", None)
		query2 = self.request.GET.get("sub_category", None)
		query3 = self.request.GET.get("gender", None)
		query4 = self.request.GET.get("price", None)
		query5 = self.request.GET.get("description", None)

		if query is not None:
			qs = qs.filter(
				Q(category__icontains=query)
			)

		if query2 is not None:
			qs = qs.filter(
				Q(sub_category__icontains=query2)
			)

		if query3 is not None:
			qs = qs.filter(
				Q(gender__iexact=query3)
			)

		if query4 is not None:
			qs = qs.filter(
				Q(price__lte=query4)
			)

		if query5 is not None:
			qs = qs.filter(
				Q(description__icontains=query5)
			)
		return qs


	def get_context_data(self, **kwargs):


		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['image'] = []
		context['values'] = self.request.GET
		context['categories'] = CATEGORY_CHOICES
		context['sub_categories'] = SUB_CATEGORY_CHOICES

		# Add in a QuerySet of all the books
		# for object in context['object_list']:
		# object.image = Product.objects.filter(name=object.name).main_image
		# print(context['image'])
		for object in context['object_list']:
		# print(object.main_image)
			print(object)
			object.image = ProductImage.objects.filter(product=object).first().image
		return context


class ProductDetailView(DetailView):
	model = Product
	template_name = 'products/product_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['attributes'] = []
		context['images'] = []
		attributes = get_dataset(Attribute, product=context['object'])
		for attribute in attributes:
			context['attributes'].append(attribute)
		for image in get_dataset(ProductImage, product_id=context['object']):
			context['images'].append(image)
		return context


def product_add_wishlist_cart(request, pk):
	action_perfomed = request.GET.get('button')
	quantity = int(request.GET.get('quantity'))
	if action_perfomed == 'wishlist':
		return HttpResponse(add_wishlist_item(request, pk))
	else:
		return HttpResponse(add_to_cart(request, pk, quantity))
