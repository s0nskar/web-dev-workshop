from django.shortcuts import render, redirect

from basic.models import User, Feedback, Team

def index(request):
	context = {}
	if request.method == "POST":
		name = request.POST.get('name', '')
		branch = request.POST.get('branch', '')
		year = request.POST.get('year', '')
		phone = request.POST.get('phone', '')
		email = request.POST.get('email', '')

		u = User.objects.create(
				name=name,
				branch=branch,
				year=year,
				phone=phone,
				email=email
			)
		return redirect('thanks')
	else:
		return render(request, 'index.html', context)

def feedback(request):
	context = {}
	if request.method == "POST":
		ratings = request.POST.get('ratings', '')
		feedback = request.POST.get('feedback', '')

		f = Feedback.objects.create(
				title=ratings,
				feedback=feedback
			)
		return redirect('thanks')
	else:
		return render(request, 'feedback.html', context)

def contacts(request):
	context = {}
	team = Team.objects.all()
	context['team'] = team
	return render(request, 'contacts.html', context)

def thanks(request):
	return render(request, 'thanks.html', {})