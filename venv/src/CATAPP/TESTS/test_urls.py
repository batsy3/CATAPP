from django.test import SimpleTestCase
from django.urls import reverse, resolve
from CATAPP.views import home, search

class Testurls (SimpleTestCase):
    def test_home_url(self):
        url = reverse('home') 
        print(resolve(url))
        
        #unittest to check the equality of the resolve func == home
        self.assertEquals(resolve(url).func, home)

    def test_search_url(self):
        url = reverse('search') 
        print(resolve(url))
      #unittest to check the equality of the resolve func == home

