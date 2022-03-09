# CATAPP

This django app returns an image or animated cat image based on the tag usser searches.

## Installation

The software requirments needed to run CATAPP include the following
+ python 3 
+ pip 
+ django

To use this app, once requirements are installed and configured, user is to start an app via django command in IDE or command line.

start a local server in your CMD next via the following code

```bash
python manage.py runserver
```

# EXPLANATION OF THE CODE 

## FUNCTIONS

+ The function that runs the Home page collects information from the CATAAS API
  -stores it in a variable as a json file which is a good way to store data information being exchanged between an API and the app.
  -renders the information to an html page that previews some cats and their tag.
  
+ The search function collects user input from the search bar and stores it in a variable.
  - The function then colledcts cats with the tag and renders it to the result url.
  
## TEMPLATES 

+ The home webpage displays cats and their tags (limited to 5 cats) 
+ The search page displays cats that have being queried via search bar and a tag (also limited to five)
