from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
	model = Product
	template_name = 'catalog/product_list.html'


class ProductDetailView(DetailView):
	model = Product
	template_name = 'catalog/product_detail.html'


class HomeListView(ListView):
	model = Product
	template_name = 'catalog/home.html'
	context_object_name = 'products'


# def products_list(request):
# 	products = Product.objects.all()
# 	context = {'products': products}
# 	return render(request, 'products_list.html', context=context)


# def product(request, pk):
# 	product = get_object_or_404(Product, pk=pk)
# 	context = {'product': product}
# 	return render(request, 'product.html', context=context)

# def home(request):
# 	products = Product.objects.all()
# 	context = {'products': products}
# 	return render(request, 'catalog/home.html', context=context)


def contacts(request):
	if request.method == 'POST':
		name = request.POST.get['name']
		email = request.POST.get['email']
		message = request.POST.get['message']
		return render(request, 'catalog/contacts.html', {'name': name, 'email': email, 'message': message})
	return render(request, 'catalog/contacts.html')
