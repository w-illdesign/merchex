from django.shortcuts import render
from .models import Band, Listing
from django.utils.timezone import now

def band_list(resquest):
	bands = Band.objects.all()
	return render(
		resquest, 'listings/band_list.html',
			{
				'bands' : bands,
				'timestamp':int(now().timestamp())
				
			}
		)

def band_detail(resquest, id):
	band = Band.objects.get(id=id)
	return render(
		resquest, 'listings/band_detail.html',
			{
				'band':band,
				'timestamp':int(now().timestamp())
			}
		)
		
def listings(resquest):
	listings = Listing.objects.all()
	return render(
		resquest, 'listings/listing.html', 
			{
				'listings': listings, 
				'timestamp':int(now().timestamp())
			}
		)
	
def listing_detail(resquest, id):
	listing = Listing.objects.get(id=id)
	return render(
		resquest, 'listings/listing_detail.html', 
			{
				'listing': listing, 
				'timestamp':int(now().timestamp())
			}
		)
		
from django.shortcuts import get_object_or_404
from .models import Band, Listing

def listings_band(request, id):
    band = get_object_or_404(Band, id=id)  # ← on récupère le groupe
    listings = Listing.objects.filter(band=band)  # ← on filtre ses annonces
    return render(request, 'listings/listings_band.html', {
        'band': band,
        'listings': listings,
        'timestamp':int(now().timestamp())
    })
		
def about(resquest):
	return render(
		
		resquest, 'listings/about.html', 
		{
			 'timestamp':int(now().timestamp())
		}
		)
	