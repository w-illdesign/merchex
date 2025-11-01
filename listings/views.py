from django.shortcuts import render
from .models import Band, Listing

def hello(resquest):
	bands = Band.objects.all()
	return render(resquest, 'listings/hello.html', {'bands' : bands})

def listings(resquest):
	listings = Listing.objects.all()
	return render(resquest, 'listings/listing.html', {'listings': listings})
	
def about(resquest):
	return render(resquest, 'listings/about.html')
	