from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Comic, Genre, Photo
from .forms import ReadingForm
from django.contrib.auth import login

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'catcollector187'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def comics_index(request):
    comics = Comic.objects.filter(user=request.user)
    return render(request, 'comics/index.html', { 'comics': comics })

@login_required
def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    genres_comic_doesnt_have = Genre.objects.exclude(id__in = comic.genres.all().values_list('id'))
    reading_form = ReadingForm()
    return render(request, 'comics/detail.html', { 'comic': comic, 'reading_form': reading_form, 'genres': genres_comic_doesnt_have })

@login_required
def add_reading(request, comic_id):
  form = ReadingForm(request.POST)
  if form.is_valid():
    new_reading = form.save(commit=False)
    new_reading.comic_id = comic_id
    new_reading.save()
  return redirect('detail', comic_id=comic_id)

@login_required
def assoc_genre(request, comic_id, genre_id):
  Comic.objects.get(id=comic_id).genres.add(genre_id)
  return redirect('detail', comic_id=comic_id)

@login_required
def unassoc_genre(request, comic_id, genre_id):
  Comic.objects.get(id=comic_id).genres.remove(genre_id)
  return redirect('detail', comic_id=comic_id)

class ComicUpdate(LoginRequiredMixin, UpdateView):
  model = Comic
  fields = ['publisher', 'description', 'year']

class ComicDelete(LoginRequiredMixin, DeleteView):
  model = Comic
  success_url = '/comics/'

class ComicCreate(LoginRequiredMixin, CreateView):
    model = Comic
    fields = ['name', 'publisher', 'description', 'year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, comic_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, comic_id=comic_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', comic_id=comic_id)

class GenreList(LoginRequiredMixin, ListView):
  model = Genre

class GenreDetail(LoginRequiredMixin, DetailView):
  model = Genre

class GenreCreate(LoginRequiredMixin, CreateView):
  model = Genre
  fields = '__all__'

class GenreUpdate(LoginRequiredMixin, UpdateView):
  model = Genre
  fields = ['name']

class GenreDelete(LoginRequiredMixin, DeleteView):
  model = Genre
  success_url = '/genres/'