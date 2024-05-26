from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
	return render(request, 'home.html')


def contacts(request):
	if request.method == 'POST':
		name = request.POST.get['name']
		email = request.POST.get['email']
		message = request.POST.get['message']
		return render(request, 'contacts.html', {'name': name, 'email': email, 'message': message})
	return render(request, 'contacts.html')


def products_list(request):
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'products_list.html', context=context)


def product(request, pk):
	product = get_object_or_404(Product, pk=pk)
	context = {'product': product}
	return render(request, 'product.html', context=context)