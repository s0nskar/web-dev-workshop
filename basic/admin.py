from django.contrib import admin

from basic.models import User, Feedback, Team

admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Team)