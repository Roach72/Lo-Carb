from django.shortcuts import render
from .models import SocialMediaLink, whatsappchat, mobile, lociation, app, description, description2, addlocarb

def social(request):
    addlocarbs     = addlocarb.objects.all()
    apps           = app.objects.all()
    locations      = lociation.objects.all() 
    mobiles        = mobile.objects.all()
    social_links   = SocialMediaLink.objects.all()
    whatsapp_chats = whatsappchat.objects.all()
    return render(request, 'app/social.html', {'social_links': social_links, 'whatsapp_chats': whatsapp_chats, 'mobiles': mobiles, 'locations': locations, 'apps': apps, 'addlocarbs':addlocarbs})

def page(request):
	descriptions   = description.objects.all()
	descriptions2   = description2.objects.all()
	return render(request, 'app/page.html', {'descriptions': descriptions, 'descriptions2': descriptions2})

