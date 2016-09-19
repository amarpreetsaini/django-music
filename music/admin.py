from django.contrib import admin

# Register your models here.
from .models import Singer,Songs, Albums

admin.site.register(Singer)
admin.site.register(Songs)
admin.site.register(Albums)
