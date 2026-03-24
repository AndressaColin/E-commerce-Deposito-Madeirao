from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.products import Products
from store.models.category import Category
from django.views import View
# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        #ensure cart exists and key are normalized to strings
        cart = request.session.get('cart', {})
        if product:
            product_id = str(product)
            quantity = cart.get(product_id, 0)
            if remove:
                if quantity <= 1:
                    cart.pop(product_id, None)
                else:
                    cart[product_id] = quantity - 1
            else:
                cart[product_id] = quantity + 1
            
            #save back to session
            request.session['cart'] = cart
        return redirect('homepage')
    
    def get(self, request):
        #list products and categories 
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Products.get_all_products_by_categoryid(categoryID)
        else:
            products = Products.get_all_products()

        data = {
            'products': products,
            'categories': categories
        }
        return render(request, 'index.html', data)
    
def store(request):
    return render(request, 'store.html')


