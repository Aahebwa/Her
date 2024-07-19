from django.shortcuts import render, redirect
from .forms import FileUploadForm, CreateCourseUnit
from .models import UploadFile, Course_unit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    current_url = request.build_absolute_uri()
    return render(request, 'home.html', {'current_url':current_url})

def it(request):
    return render(request, 'it.html')

def electr(request):
    return render(request, 'electr.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/department/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/department/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def course_unit(request):
    course_units = Course_unit.objects.all()
    return render(request, 'file_list.html', {'course_units':course_units})

@login_required
def add_course_unit(request):
    if request.method == 'POST':
        form = CreateCourseUnit(request.POST)
        if form.is_valid():
            course_unit = form.save(commit=False)
            course_unit.unit_author = request.user
            course_unit.save()
            return redirect('/')
    else:
        form = CreateCourseUnit()
    return render(request, 'create.html', {'form':form})

def details(request, slug):
    detail = Course_unit.objects.get(slug=slug)
    files = UploadFile.objects.all().order_by('uploaded_at')
    return render(request, 'details.html', {'detail':detail, 'files':files})

def computer_science(request):
    files = UploadFile.objects.all()
    return render(request, 'computer_science.html', {'files':files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_creator = form.save(commit=False)
            file_creator.file_author = request.user
            file_creator.save()
            return redirect('/')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form':form})

# @login_required
# def file_list(request):
#     files = UploadFile.objects.all()
#     return render(request, 'details.html', {'files':files})
#
# def dash_file_list(request):
#     pass
