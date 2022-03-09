from django.shortcuts import render
import requests


def home(request):
    response = requests.get(f'https://cataas.com/api/cats?limit=5').json()
    
    return render(request, 'home.html', {'response': response})

def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        url = requests.get(f'https://cataas.com/api/cats?tags={search_tag}&limit=5').json()
        error_msg = f"9 lives exhaused for dem  '{search_tag}' cats there buddy"
        if url:
            return render(request, 'search.html', {'results_tag': url})
        else:
            return render(request, 'search.html', {'message': error_msg})
def view(request, cat_id):
	response=requests.get(f'https://cataas.com/api/{cat_id}')
	return render (request, 'view.html', {'response':response})