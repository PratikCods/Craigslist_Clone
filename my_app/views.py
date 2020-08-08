import requests
from requests.compat import quote_plus
from django.shortcuts import render,reverse
from bs4 import BeautifulSoup

def home(request):
    return render(request,'my_app/base.html')

def new_search(request):
    BASE_URL = "https://losangeles.craigslist.org/search/bbb?query={}"
    BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
    search = request.POST.get('search')
    new_search_string = quote_plus(search.lower())

    response = requests.get(BASE_URL.format(new_search_string))

    soup = BeautifulSoup(response.text,features = 'html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://www.kindpng.com/picc/m/380-3809024_5-stars-png-cartoon-five-star-general-symbol.png'

        final_postings.append((post_title, post_url, post_price, post_image_url))

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
