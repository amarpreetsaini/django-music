=====
Music
=====

Music is a simple Django app to create music website. We can add 
singers, songs and albums. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "music" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'music',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^music/', include('music.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to start adding singer,songs and albums  (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/music/ to start using music app.
