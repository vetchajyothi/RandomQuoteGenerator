			SAMPLE PROJECT	USING DJANGO
								-Random Quote Generator
STEP-1: Create project and app
		>django-admin startproject quote_project
		>cd quote_project
		>python manage.py startapp quotes
STEP-2:Now defining  model:
	In quotes, open the models.py file and add the following code-
from django.db import models
# Create your models here.
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.text} - {self.author}"
        STEP-3:Adding quotes to Admin
	In quotes open admins.py add the following code:-
from django.contrib import admin
# Register your models here.
from .models import Quote
admin.site.register(Quote)

STEP-4:Now create views:
		In quotes(app) views.py add the following code:-
import random
from django.shortcuts import render
from .models import Quote
# Create your views here.
def random_quote(request):
	quotes = Quote.objects.all()
quote = random.choice(quotes) if quotes else None
return render(request, 'quotes/index.html', {'quote': quote})

STEP-5:Configuring urls:
		-In quotes(app’s) urls.py add the following code:
from django.urls import path
from .views import random_quote
urlpatterns = [
    path('', random_quote, name='random_quote'),
]

		 -In quote_project(project’s) urls.py add the following code:
from django.contrib import admin
from django.urls import path ,include
urlpatterns = [
path('admin/', admin.site.urls),
			    path('', include('quotes.urls')), 
]
STEP-6:Creating a Template:
	In quotes create a folder called “templates” and in that again create a folder called “quotes” and in that create a html file called as “index.html”.
And in that add the following code:

<!DOCTYPE html>
<html>
<head>
 <title>Random Quote Generator</title>
</head>
<body>
   <h1>Random Quote Generator </h1>
    {% if quote %}
        <blockquote>
        <p>"{{ quote.text }}"</p>
            <footer>— {{ quote.author }}</footer>
        </blockquote>
        <a href="/">Get Another Quote</a>
    {% else %}
        <p>No quotes found.</p>
    {% endif %}
</body>
</html>
STEP-7:In your quote_project(project’s) "settings.py", add ‘quotes’(app name) in installed apps.
STEP-8:After defining the model, run the following command to create the necessary database tables: 
				>python manage.py makemigrations 
    				>python manage.py migrate
STEP-9:Now give some quotes in using powershell:
		-Open powershell and enter command:
			>python manage.py shell
			>>>                                         (indicates we entered into powershell)
The indication that we entered in to power shell is in that we get ‘>>>’ in place of ‘>’
			-And enter the following :
		       from quotes.models import Quote
		       Quote.objects.create(text="The only limit to our realization of tomorrow is
         		      our doubts of today.", author="Franklin D. Roosevelt")
Quote.objects.create(text="In the middle of every difficulty lies opportunity.", author="Albert Einstein")
Quote.objects.create(text="It does not matter how slowly you go as long as you do not stop.", author="Confucius")
-Exit from the powershell by the command exit
>>>exit()
(indicates we are exited from power shell)
STEP:10:Create superuser by using the following command:
			>python manage.py createsuperuser
It asks for username,gmail,password after that the superuser will be created
STEP-11:Run the server by using below command:
			>python manage.py runserver
Now visit  http://127.0.0.1:8000/
Now open the browser and enter the URL:
		http://127.0.0.1:8000/admin/
Login using above admin user credentials. After logging in we are directed to the site administration.
