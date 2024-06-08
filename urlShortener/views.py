from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ShortURL
from .forms import CreateNewShortURL
import random, string

# Function for Home Page
def home(request):
    form = CreateNewShortURL()
    return render(request, 'index.html', { 'form' : form })

# Function to redirect to URL
def redirect(request, url):
    currentObject = ShortURL.objects.filter(Short_URL = url)
    
    if len(currentObject) == 0:
        return render(request, 'error.html')

    context = { 'obj' : currentObject[0] }
    
    return render(request, 'redirect.html', context)

# Function to create shortened URL
def createShortURL(request):

    # If there is a POST request
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)

        if form.is_valid():
            originalWebsite = form.cleaned_data['Original_URL']
            randomCharsList = list(string.ascii_letters)
            randomChars = ''

            # Creating random letters for link
            for i in range(6):
                randomChars += random.choice(randomCharsList)

            # Checking and changing random letters if another created URL already has the same
            while len( ShortURL.objects.filter(Short_URL = randomChars)) != 0:
                for i in range(6):
                    randomChars += random.choice (randomCharsList)
            
            # Date Created for shortened URL
            d = timezone.now()
            s = ShortURL(Original_URL = originalWebsite, Short_URL = randomChars, Time_Created = d)
            s.save()

            return render(request, 'index.html', { 'chars' : randomChars, 'form' : form})

# Remember to run new database: python manage.py makemigrations / python manage.py migrate
# For static pages: python manage.py collectstatic --noinput --clear