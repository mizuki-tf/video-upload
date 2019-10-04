from django.urls import reverse_lazy
from django.views import generic
from .models import Video
from .forms import VideoCreateForm

"""最初の表示画面"""
class IndexView(generic.ListView):
    model = Video

"""動画投稿画面"""
class UploadView(generic.CreateView):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('movieapp:index')

"""動画再生画面"""
class PlayView(generic.DetailView):
    model = Video
