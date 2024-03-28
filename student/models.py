from django.db.models import Model, IntegerField, CharField, DateField

class Student(Model):
	roll_no = IntegerField(primary_key=True)
	name = CharField(max_length=50, blank=False, null=False)
	std = CharField(max_length=20, blank=False, null=False)
	birthdate = DateField(blank=False, null=False)
