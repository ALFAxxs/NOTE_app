from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password 
from .models import User, Note

from django.urls import reverse

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_exists = user.check_password(password)
        except User.DoesNotExist:
            user_exists = False

        if user_exists:
            login(request, user)
            return redirect(reverse('general', kwargs={'id': user.id}))
    return render(request, 'login.html')


def registration_page(request):
    if request.method == 'POST':
        password = request.POST.get('Password')
        hashed_password = make_password(password)
        user = User.objects.create(
            first_name=request.POST.get('FirstName'),
            last_name=request.POST.get('LastName'),
            email=request.POST.get('email'),
            password=hashed_password
        )
        return redirect('login')
    return render(request, 'registration.html')

def add_note(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=id)
            Note.objects.create(
                title=request.POST.get('Title'),
                description=request.POST.get('Description'),
                owner=user
            )
            return redirect('posts', id=id) 
        except User.DoesNotExist:
            return HttpResponse("User not found", status=404)
    return render(request, 'add_note.html')


def posts_page(request, id):
    user = get_object_or_404(User, id=id)
    notes = Note.objects.filter(owner=user)
    return render(request, 'notes.html', {'notes': notes, 'user': user})



def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        
        note.title = title
        note.description = description
        note.save()
        user_id = note.owner.id
        return redirect(reverse('posts', kwargs={'id': user_id}))
    else:
        return render(request, 'add_note.html', {'note': note})


def note_delete(request, id):
    note = get_object_or_404(Note, pk=id)
    note.delete()
    user_id = note.owner.id
    context = {
        'note':note
    }
    return redirect(reverse('posts', kwargs={'id': user_id}))

def general_page(request, id):
    user = get_object_or_404(User,id=id)
    return render(request, 'general.html', {'user':user})
