from django.db import models


# Create your models here.
# `watched`untuk mendeskripsikan film tersebut sudah ditonton atau belum
# `title`ntuk mendeskripsikan judul film
# `rating`untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5
# `release_date`untuk mendeskripsikan kapan film dirilis
# `review`untuk mendeskripsikan review untuk film tersebut

class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField(max_length=1)
    release_date = models.DateField()
    review = models.TextField()
