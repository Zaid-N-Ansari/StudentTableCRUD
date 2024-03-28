from django.shortcuts import redirect, render
from .forms import CreateStudentForm, UpdateStudentForm
from .models import Student

def home_view(req):
	context = {}
	return render(req, 'student/home.html', context)



def create(request, *args, **kwargs):
	context = {}
	if request.method == 'POST':
		fm = CreateStudentForm(request.POST)
		context.update({'form':fm})
		if fm.is_valid():
			fm.save()
			return redirect('/student/read/')
	else:
		fm = CreateStudentForm()
		context.update({'form':fm})
	return render(request, 'student/create.html', context)




def read(req, *args, **kwargs):
	context = {}
	data = Student.objects.all()
	context.update({'tabledata':data})
	return render(req, 'student/read.html', context)



def update(req, *args, **kwargs):
	context = {}
	rn = kwargs.get('roll_no')
	data = Student.objects.get(pk=rn)
	if req.method == 'POST':
		fm = UpdateStudentForm(req.POST, instance=data)
		context.update({'form':fm})
		if fm.is_valid():
			fm.save()
			return redirect('/student/read/')
	else:
		fm = UpdateStudentForm(instance=data)
		context.update({'form':fm})
	return render(req, 'student/update.html', context)



def delete(req, *args, **kwargs):
	context = {}
	rn = kwargs.get('roll_no')
	try:
		Student.objects.get(roll_no=rn)
		context.update({'DoesExist':True})
		context.update({'rn':rn})
		
	except Student.DoesNotExist:
		context.update({'DoesExist':False})
		context.update({'rn':rn})
	return render(req, 'student/delete.html', context)


def delete_student_record(req, *args, **kwargs):
	rn = kwargs.get('roll_no')
	try:
		student = Student.objects.get(roll_no=rn)
		student.delete()
	except Student.DoesNotExist:
		pass
	return redirect('/student/read/')
