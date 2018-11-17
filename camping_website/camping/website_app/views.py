from django.shortcuts import render
from website_app.models import Emplacement, HomePage, Media
from django.views import generic

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ContactForm


class MediaListView(generic.ListView):
    model = Media

# def media(request):
#
#     all_media = Media.objects.all()
#
#     return render(request, 'media.html', {'all_media': all_media} )


# Create your views here.
def index(request):
    data =str(HomePage.objects.filter().only().first())
    splited = data.split('__sep_char__')

    context = {
        'header_title1': splited[0],
        'header_title2': splited[1],
        'header_summary': splited[2],
        'header_button1' : splited[3],
        'header_button2' : splited[4],
        'features1_1_title': splited[5],
        'features1_1_text': splited[6],
        'features1_2_title': splited[7],
        'features1_2_text': splited[8],
        'features1_3_title': splited[9],
        'features1_3_text': splited[10],
        'features1_4_title': splited[11],
        'features1_4_text': splited[12],
        'features2_1_title': splited[13],
        'features2_1_text': splited[14],
        'features2_2_title': splited[15],
        'features2_2_text': splited[16],
        'features2_3_title': splited[17],
        'features2_3_text': splited[18],
        'features2_4_title': splited[19],
        'features2_4_text': splited[20],
        'features2_5_title': splited[21],
        'features2_5_text': splited[22],
        'citation_title': splited[23],
        'citation_auteur': splited[24],
        'contact_title': splited[25],
        'contact_text': splited[26],
        'adress': splited[27],
        'email': splited[28],
        'phone': splited[29],
        # 'email_receptrice': splited[30],
    }


    return render(request, 'index.html', context=context)



# Create your views here.
def tarif(request):
    """View function for home page of site."""
    emplacement_number = Emplacement.objects.all().count()

    context = {
        'emplacement_number': emplacement_number,
    }
# Render the HTML template index.html with the data in the context variable
    return render(request, 'tarif.html', context=context)

def media(request):
    context = {
        'emplacement_number': "emplacement_number",
    }
    return render(request, 'media.html', context=context)

def contact(request):
    if(request.method == 'GET'):
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['kissmyskunkpossible@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "contact.html", {'form': form})
