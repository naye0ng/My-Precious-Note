from django.shortcuts import render

def index(request) :
    return render(request, 'notes/list.html')

def like(request, notes_id) :
    pass

def create(request) :
    return render(request, 'notes/create.html')    

def update(request) :
    return render(request, 'notes/update.html')

def delete(request) :
    pass