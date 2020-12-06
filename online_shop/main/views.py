from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Order, OrderItem
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

CATEGORIES = {"kitchen":7, "candy":6, "fish":5, "fruits":4, "juice":3, "souse":2, "pasta":1}

# Create your views here.
def send_mail(request):
    login = 'ourdjangoshop@mail.ru'
    password = '$python333$'
    url = 'smtp.mail.ru'
    toaddr = 'ourdjangoshop@mail.ru'
    topic = request.POST.get('subject')
    contact_message = request.POST.get('message')
    contact_email = request.POST.get('email')
    name = request.POST.get('name')
    message = 'New message from contact template:\n\nTopic: {}\n\nName: {}\n\nMessage : {}\n\nEmail: {}'.format(topic,
                                                                                                                name,
                                                                                                                contact_message,
                                                                                                                contact_email)
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())
def send_mail_name(request):
    login = 'ourdjangoshop@mail.ru'
    password = '$python333$'
    url = 'smtp.mail.ru'
    toaddr = 'ourdjangoshop@mail.ru'
    topic = 'New Subscribation!'
    contact_email = request.POST.get('email')
    message = 'User {} subscribed to our shop Now we can send messages to this mail !\nUser: {} \nMail: {}'.format(request.user.username,request.user.username,request.POST.get('email'))
    msg = MIMEMultipart()
    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def main(request):
    return redirect("/index")
def index_page(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    if request.method == "POST":
        item = Item.objects.all().filter(id=pk)[0]
        smitem = Item.objects.all().filter(category=item.category)
        content = {'item': item, 'smitem': smitem}
        return render(request, 'main/single.html', content)
    items = Item.objects.all()
    content = {"items": items}
    return render(request, "main/index.html", content)
def about(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/about.html")
def contact(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/contact.html")

def shoplocator(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/shoplocator.html")
def help(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/help.html")
def privacy(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/privacy.html")
def terms(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/terms.html")
def search(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    if request.method == 'POST':
        search = request.POST.get('search')
        items = Item.objects.all()
        content = {"items": items,"search": search}
        return render(request, "main/search.html", content)
    return render(request, "main/search.html", content)

def checkout(request):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    return render(request, "main/checkout.html")

def error_404(request, exception):
    return render(request,'main/404.html')

def error_500(request):
    return render(request,'main/404.html')

@login_required()    
def cart_view(request):
    order_ = Order.objects.all().filter(user_id = request.user.id, ordered = False)[0]
    
    return render(request, 'main/checkout.html', {'order_':order_})
    
def item_view(request, pk):
    if (request.method == 'POST') and request.POST.get('name') == "send_mail":
        send_mail_name(request)
    item = Item.objects.all().filter(id=pk)[0]
    smitem = Item.objects.all().filter(category=item.category)
    content = {'item': item, 'smitem': smitem}
    return render(request, 'main/single.html', content)

@login_required()
def add_to_cart(request, pk):
    # if (request.method == 'POST') and request.POST.get('name') == "send_mail":
    #     send_mail_name(request)
    item = get_object_or_404(Item, pk = pk)
    order_item = OrderItem.objects.get_or_create(order_item = item, user = request.user)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(order_item__pk = item.id).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.add_message(request, messages.SUCCESS, "Item added to cart")
        else:
            order.items.add(order_item[0])
            messages.add_message(request, messages.SUCCESS, "Item added to cart")
    else:
        order = Order.objects.create(user = request.user)
        order.items.add(order_item[0])
        messages.add_message(request, messages.SUCCESS, "Item added to cart")
    return redirect('index_page')


@login_required()
def minus(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_item = OrderItem.objects.get(order_item = item, user = request.user)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if  order.items.filter(order_item__pk = item.id).exists():
            if order_item.quantity == 1:
                order.items.remove(order_item)
            else:
                order_item.quantity -= 1
                order_item.save()
    return redirect('cart_view')

@login_required
def plus(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_item = OrderItem.objects.get(order_item = item, user = request.user)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(order_item__pk = item.id).exists():
            order_item.quantity += 1
            order_item.save()
      
    return redirect('cart_view')

@login_required
def remove(request, pk):
    item = get_object_or_404(Item, pk = pk)
    order_item = OrderItem.objects.get(order_item = item, user = request.user)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(order_item__pk = item.id).exists():
            
            order.items.remove(order_item)
            
            order_item.save()
    return redirect('cart_view')