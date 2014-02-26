from models import *
from django.contrib import admin

class problemAdmin(admin.ModelAdmin):
	list_display = ('problem_id','priority','description','status','related_tickets','current_owner','affected_components','currect_impact','user_experience','root_cause','workaround','workaround_status','long_term_solution','long_term_solution_status','comments')
	list_filter = ['problem_id','priority','status','related_tickets','current_owner','affected_components']
	search_fields = ['description','workaround','long_term_solution','comments']
	list_editable = ['priority','description','status','related_tickets','current_owner','affected_components','currect_impact','user_experience','root_cause','workaround','workaround_status','long_term_solution','long_term_solution_status','comments']
	ordering = ['problem_id']

	formfield_overrides = {
    	models.TextField: {'widget': Textarea(
       		attrs={'rows': 1,
                'cols': 50})},
	}

admin.site.register(problem,problemAdmin)
