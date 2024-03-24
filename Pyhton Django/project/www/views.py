from django.shortcuts import render

# Create your views here.

studenci = [
        {
            'imie': 'Jan',
            'nazwisko': 'Kowalski',
            'nr_albumu': '12345'
        },
        {
            'imie': 'Aleksandra',
            'nazwisko': 'Nowak',
            'nr_albumu': '678910'
        }
    ]

def index(request):
    return render(request, 'www/index.html', {'studenci': studenci})




def bootstrap(request):
    return render(request,'www/bootstrap.html', {'studenci': studenci})