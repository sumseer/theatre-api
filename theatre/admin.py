from django.contrib import admin

from .models import (
    Actor,
    Genre,
    Play,
    Performance,
    TheatreHall,
    Reservation,
    Ticket,
)

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Play)
admin.site.register(Performance)
admin.site.register(TheatreHall)
admin.site.register(Reservation)
admin.site.register(Ticket)
