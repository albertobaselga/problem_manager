from problem_manager import *
from django.contrib import admin

class problemAdmin((admin.ModelAdmin):
	list_display = ('problem_id','priority','description','status','related_tickets')
	list_filter = ['problem_id','priority','description','status','related_tickets']
	search_fields = ['description']
	list_editable = ['description','status']
	ordering = ['problem_id']

admin.site.register(problem,problemAdmin)
