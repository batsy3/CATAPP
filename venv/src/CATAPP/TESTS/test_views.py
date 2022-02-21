from django.test import TestCase, Client
from django.urls import reverse
from CATAPP.views import home, search
import json

#reverse returns the complete URL to that route as a String.3 Mar 
class Test_views(TestCase):
    #setup a scenario
    def setup(self):
        self.client = Client()

    def test_home_view(self):
        #setup code 
        response = self.client.get(reverse('home'))
        #assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'CATAPP/home.html')

    def test_search_view(self):
    #setup code

    #test code 

        response = self.client.get(reverse('search'))
        #assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'CATAPP/search.html')

         
