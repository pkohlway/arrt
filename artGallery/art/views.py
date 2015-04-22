from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from art.models import art_item
# Create your views here.


def index(request):
	template = loader.get_template('art/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def store(request):
	latest_art = art_item.objects.order_by("item_name")
	template = loader.get_template('art/store.html')
	context = RequestContext(request, {'latest_art': latest_art, })
	#output = ', '.join([p.item_name for p in latest_art])
	return HttpResponse(template.render(context))

def contact(request):
	template = loader.get_template('art/contact.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def detail(request, item_id):
	art = get_object_or_404(art_item, pk=item_id)
	template = loader.get_template('art/detail.html')
	context = RequestContext(request, {'art' : art})
	return HttpResponse(template.render(context))

def checkout(request, item_id):
	art = get_object_or_404(art_item, pk=item_id)
	template = loader.get_template('art/checkout.html')
	context = RequestContext(request, {'art' : art})
	return HttpResponse(template.render(context))
def order(request, item_id):
	item = get_object_or_404(art_item, pk=item_id)

	item.quantity -= 1