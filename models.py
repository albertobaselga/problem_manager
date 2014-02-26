from django.db import models
from django.utils.encoding import *

PROB_PRIORITY = (('low','Low'),('medium','Medium'),('high','High'))
PROB_STATUS = (('low','Low'),('medium','Medium'),('high','High'))
PROB_WORK_STATUS = (('low','Low'),('medium','Medium'),('high','High'))
PROB_LTS_STATUS = (('low','Low'),('medium','Medium'),('high','High'))


class problem (models.Model):
	problem_id = models.CharField('Prob ID',max_length=8, unique=True)
	priority = models.CharField('Priority',max_length=50, choices=PROB_PRIORITY)
	description =  models.TextField('Description')
	status  = models.CharField('Priority',max_length=50, choices=PROB_STATUS)
	related_tickets =  models.TextField('TICKETS-UNDERCONS')
	current_owner = models.CharField('Current Owner',max_length=50)
	affected_components = models.CharField('Affected Components',max_length=50)
	currect_impact = models.CharField('Current Impact',max_length=50)
	user_experience = models.CharField('User Experience',max_length=50)
	root_cause = models.TextField('Root Cause')
	workaround = models.TextField('Workaround')
	workaround_status = models.CharField('Priority',max_length=50, choices=PROB_WORK_STATUS)
	long_term_solution = models.TextField('Long Term Solution')
	long_term_solution_status = models.CharField('Priority',max_length=50, choices=PROB_LTS_STATUS)
	comments = models.TextField('Comments')

	def __str__(self):
		return self.problem_id

	class Meta:
		verbose_name = 'Problem'
		verbose_name_plural = 'Problems'
		
