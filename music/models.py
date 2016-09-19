from django.db import models
# Create your models here.

class Singer(models.Model):
	singer_name = models.CharField(max_length=200)
	def __str__(self):
		return self.singer_name

class Songs(models.Model):
	song_name = models.CharField(max_length=200)
	added_time = models.DateTimeField('data added')
	singers = models.ManyToManyField(Singer)
	def __str__(self):
		return self.song_name

class Albums(models.Model):
	album_name = models.CharField(max_length=200)
	songs = models.ManyToManyField(Songs)
	def __str__(self):
		return self.album_name
