from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Cart, ListItem 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Sum, ExpressionWrapper, F, DecimalField

def index(request):
    return render(request, 'main/index.html')

def services(request):
    cart_rows = Cart.objects.all()

    for cart in cart_rows:
        # Calculate cartamount by summing up the total of ListItem instances for this cart
        cart.cartamount = ListItem.objects.filter(cart=cart).aggregate(cartamount=Sum(F('quantity') * F('price')))['cartamount'] or 0

    return render(request, 'main/services.html', {'cart_rows': cart_rows})



def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        uemail = request.POST.get('email')
        pass1 = request.POST.get('password')
        my_user = User.objects.create_user(username,uemail,pass1)
        my_user.save()
        print(username, uemail, pass1)
        return redirect('login')
    return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Set user_id and username as sessions
            request.session['user_id'] = user.id
            request.session['username'] = user.username

            # Print or log the session variables for debugging
            print("User ID in session:", request.session.get('user_id'))
            print("Username in session:", request.session.get('username'))

            return redirect('index')
        else:
            return HttpResponse('Username or password is incorrect!')

    return render(request, 'main/login.html')

# views.py

def logout_view(request):
    # Unset session variables
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    
    print("User ID in session:", request.session.get('user_id'))
    print("Username in session:", request.session.get('username'))
    return redirect('index')


@login_required
@csrf_protect
def create_cart(request):
    if request.method == 'POST':
        cart_name = request.POST.get('txtCartName')
        store_name = request.POST.get('txtCartStore')
        notification_date = request.POST.get('txtDate')

        user = request.user

        new_cart = Cart.objects.create(
            cartname=cart_name,
            store_wheretobuy=store_name,
            date_for_notification=notification_date,
            user=user
        )

        request.session['cart_id'] = new_cart.cart_id

        messages.success(request, 'Cart created successfully!')
        return redirect('create_manage', cart_id=new_cart.cart_id)

    return render(request, 'main/index.html')


# -----------------------------------------------manage section----------------------------------------------------

def create_manage(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    formatted_date = cart.date_for_notification.strftime('%Y-%m-%d')
    
    list_items = ListItem.objects.filter(cart_id=cart_id)
    total_sum = list_items.aggregate(
        total_sum=Sum(ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField()))
    )['total_sum'] or 0

    context = {'cart': cart, 'formatted_date': formatted_date, 'list_items': list_items, 'total_sum': total_sum}
    return render(request, 'main/createManage.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart

def update_cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    
    return render(request, 'main/update_cart.html', {'cart': cart})


def update_meth_cart(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    # Extracting data from the POST request
    cart_name = request.POST.get('txtCartName')
    store_name = request.POST.get('txtCartStore')
    notification_date = request.POST.get('txtDate')

    try:
        # Retrieve the existing Cart object
        existing_cart = Cart.objects.get(cart_id=cart_id)

        # Update the Cart object with new data
        existing_cart.cartname = cart_name
        existing_cart.store_wheretobuy = store_name
        existing_cart.date_for_notification = notification_date

        # Save the changes
        existing_cart.save()

        redirect_url = reverse('create_manage', args=[cart_id])
        redirect_url += f'?cart={cart.pk}'  # Add cart as a query parameter

        # Redirect to the 'create_manage' view with the cart_id and cart parameters
        return redirect(redirect_url)

    except Cart.DoesNotExist:
        return HttpResponse("Cart not found or you don't have permission to update it.", status=404)





from django.shortcuts import render, redirect
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect



def insert_data(request, cart_id):
    if request.method == 'POST':
        product_name = request.POST.get('ProductName')
        category = request.POST.get('Category')
        quantity = request.POST.get('Quantity')
        price = request.POST.get('Price')
        description = request.POST.get('ProductDescription')
        cart = get_object_or_404(Cart, pk=cart_id)

        # Create a new object of your model and save it to the database
        ListItem.objects.create(
            productname=product_name,
            category=category,
            quantity=quantity,
            price=price,
            description=description,
            cart=cart,
        )

        return redirect('create_manage', cart_id=cart_id)
    else:
        return render(request, 'create_manage.html')

# views.py

def delete_item(request, item_id):
    item = get_object_or_404(ListItem, list_id=item_id)
    cart_id = item.cart_id  # Assuming cart_id is related to the ListItem model

    if request.method == 'POST':
        item.delete()
        return redirect('create_manage', cart_id=cart_id)



def unset_cart_session(request):
    # Get the cart_id from the query parameters
    cart_id = request.GET.get('cart_id')

    # Unset the session variable
    if 'cart_id' in request.session:
        del request.session['cart_id']

    # You might want to perform additional logic related to cart_id here

    return HttpResponse(status=200)

def delete_cart(request, cart_id):
    cart = get_object_or_404(Cart, cart_id=cart_id)
    cart.delete()
    return redirect('services')

def view_cart(request, cart_id):
    cart = get_object_or_404(Cart, cart_id=cart_id)
    list_items = ListItem.objects.filter(cart=cart)  # Fetching related ListItem instances
    # Fetch other related data or perform additional logic if needed

    return render(request, 'main/opencart.html', {'cart': cart, 'list_items': list_items})

from django.views.decorators.http import require_POST

from django.urls import reverse

@require_POST
def delete_selected(request):
    # Get the list of item IDs to delete from the form data
    delete_ids = request.POST.getlist('delete_checkbox[]')

    # Delete the selected items
    ListItem.objects.filter(list_id__in=delete_ids).delete()

    # Assuming you have access to the cart_id in your view
    cart_id = request.POST.get('cart_id')

    # Redirect to the cart details page or any other page you want
    return redirect(reverse('view_cart', args=[cart_id]))



from django.shortcuts import render, get_object_or_404, redirect
from .models import ListItem

def edit_list_item(request, list_id):
    item = get_object_or_404(ListItem, list_id=list_id)
    return render(request, 'main/edit_list_item.html', {'item': item})

def save_list_edit(request, list_id):
    item = get_object_or_404(ListItem, list_id=list_id)
    if request.method == 'POST':
        cart_id = item.cart_id
        item.productname = request.POST.get('productname', item.productname)
        item.category = request.POST.get('category', item.category)
        item.quantity = request.POST.get('quantity', item.quantity)
        item.price = request.POST.get('price', item.price)
        item.description = request.POST.get('description', item.description)
        item.save()
        return redirect('create_manage', cart_id=cart_id)




