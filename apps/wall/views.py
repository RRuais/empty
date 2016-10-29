from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User, Message, Comment

def index(request):
    return render(request, 'wall/index.html')

def register(request):
    if request.method == "POST":
        result = User.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password'])
        if result[0]:
            request.session['first_name'] = result[1].first_name
            request.session['email'] = result[1].email
            request.session['id'] = result[1].id
            return redirect('users')
        else:
            messages.add_message(request, messages.INFO, result[1])
            return redirect(reverse('index'))

def login(request):
    if request.method == "POST":
        result = User.objects.login(email=request.POST['email'], password=request.POST['password'])
        if result[0]:
            request.session['first_name'] = result[1].first_name
            request.session['email'] = result[1].email
            request.session['id'] = result[1].id
            return redirect('wall')
        else:
            messages.add_message(request, messages.INFO, result[1])
            return redirect(reverse('index'))

def users(request):
    context = {
    'users' : User.objects.all()
    }
    return render(request, 'wall/users.html', context)

def logout(request):
    request.session.clear()
    return redirect(reverse('index'))

def delete_users(request, id):
    if request.method == 'POST':
        print request.session['id']
        print id
        if id == request.session['id']:
            User.objects.get(id=id).delete()
            return redirect(reverse('index'))
        else:
            print ('Else')
            User.objects.get(id=id).delete()
            return redirect(reverse('wall'))

def wall(request):

    context = {
        'messages' : Message.objects.all(),
        'comments' : Comment.objects.all()
        }

    return render(request, 'wall/wall.html', context)

def post_message(request):
    user_id = User.objects.get(id=request.session['id'])
    message = Message.objects.create(message=request.POST['message'], user_id=user_id)
    return redirect('wall')

def delete_message(request, id):
    Message.objects.get(id=id).delete()
    return redirect(reverse('wall'))

def post_comment(request, id):
    user_id = User.objects.get(id=request.session['id'])
    message_id = Message.objects.get(id=id)
    comment = Comment.objects.create(comment=request.POST['comment'], user_id=user_id, message_id=message_id)
    return redirect(reverse('wall'))

def delete_comment(reguest, id):
    Comment.objects.get(id=id).delete()
    return redirect(reverse('wall'))
