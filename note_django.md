django-admin startproject myDjango1

python manage.py startapp myapp

python manage.py migrate

python manage.py runserver


Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.




python manage.py makemigrations myapp  #create model migration from models.py file
python manage.py sqlmigrate polls 0001 
python manage.py check; 



# xem
from django.db import models
html placeholder



python manage.py shell






why add myapp to settings.py?



admin.py to register DB models

models.py to place DB models

tests.py to place tests

views.py to place views or routes


create urls.py to put





>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()


# shell command 
a = Question.objects.get(pk=2)
q.choice_set.create(choice_text="Not much", votes=0)

Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()

Choice.objects.filter(question__pub_date__year=current_year)

c = q.choice_set.filter(choice_text__startswith="Just hacking")


# django Admin

python manage.py createsuperuser
pass 1111



# flow
add app, rest_framework to settings.py
create serializer.py 
create models.py  



csrfmiddlewaretoken: 3DRGhrdWH0BITXaR8jlzwU5SomStQMY1hyu1v9dLbfDw04g9j793n2mubH6HINgu
description: hello3
due_date: 2025-05-22T23:09
priority: high


    {
        "id": 5,
        "description": "task1eeee",
        "finish": false,
        "due_date": "2025-05-29T22:54:00Z",
        "priority": "high",
        "created_at": "2025-05-10T15:54:26.934660Z"
    },


    {
        "description": "task_post1",
        "finish": false,
        "due_date": "2025-05-29T22:54:00Z",
        "priority": "low"
    }