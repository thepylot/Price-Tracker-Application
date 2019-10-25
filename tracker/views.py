from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from .models import Item
from .forms import AddNewItemForm

def tracker_view(request):
    items = Item.objects.order_by('-id')
    form = AddNewItemForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            url = form.cleaned_data.get('url')
            requested_price = form.cleaned_data.get('requested_price')
            crawled_data = crawl_data(url)
            Item.objects.create(
            url = url,
            title = crawled_data['title'],
            requested_price=requested_price,
            last_price=crawled_data['last_price'],
            discount_price='No Discount Yet',
            )
            return HttpResponseRedirect('')
        else:
            form = AddNewItemForm()
    context = {
        'items':items,
        'form':form,
    }
    return render(request, 'tracker.html', context)

def crawl_data(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, 'html.parser')
    
    title = bs.find('h1', id="itemTitle").get_text().replace("Details about", "").strip()
    price = bs.find('span', id="prcIsum").get_text()
    clean_price = float(price.strip().replace("US", "").replace("$", ""))
    return {'title': title, 'last_price':clean_price }