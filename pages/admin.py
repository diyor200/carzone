from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            f'<img src="{object.photo.url}" width=50 style="border-radius: 50px;" />'
        )

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'first_name', 'thumbnail',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
