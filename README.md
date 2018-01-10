Create a virtual environment and from it, run

    pip install requirements.txt
    python manage.py migrate
    python manage.py loaddata parking/fixtures.json
    # For admin purposes
    python manage.py createsuperuser

Example query:

    from django.contrib.gis.geos import fromstr
    from django.contrib.gis.measure import D
    from parking.models import ParkingSpot
    pnt=fromstr('POINT(-122.413768 37.782781)', srid=4326)
    ParkingSpot.objects.filter(location__distance_lte=(pnt, D(km=1))).count()

