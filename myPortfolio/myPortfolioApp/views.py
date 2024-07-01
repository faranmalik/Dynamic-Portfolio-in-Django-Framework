from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Header, Skill, Experience, Education, Project, Contact

DEFAULT_USERNAME = 'faranmalik'  # Replace with your actual default username


def home(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = get_object_or_404(User, username=DEFAULT_USERNAME)

    headers = Header.objects.filter(user=user).first()  # Fetching the header for the user
    skills = Skill.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    education_list = Education.objects.filter(user=user)
    projects = Project.objects.filter(user=user)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Save the contact message
        contact = Contact(user=user, name=name, email=email, message=message)
        contact.save()

        # Add a success message
        messages.success(request, 'Your message has been submitted successfully!')

        # Set a session flag to indicate a successful form submission
        request.session['form_submitted'] = True

        # Redirect back to the home page with the same URL
        if username:
            return redirect('user_home', username=username)
        else:
            return redirect('home')

        # Clear the form submission flag after redirecting
    form_submitted = request.session.pop('form_submitted', False)

    context = {
        'headers': headers,
        'skills': skills,
        'experiences': experiences,
        'education_list': education_list,
        'projects': projects,
        'portfolio_user': user,
    }

    return render(request, 'portfolio/index.html', context)
