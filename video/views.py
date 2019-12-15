from django.shortcuts import render, redirect, get_object_or_404
from hitcount.views import HitCountDetailView
from main.models import *
from .forms import *
from django.utils import timezone

# Create your views here.
class videoDetail(HitCountDetailView):
    model=Video
    template_name='video/videoDetail.html'
    context_object_name='videoObj'
    count_hit=True

class myVideoDetail(HitCountDetailView):
    model=Video
    template_name='video/myVideoDetail.html'
    context_object_name='videoObj'
    count_hit=True

def myVideo(request):
    qs = Video.objects.all()
    q = request.GET.get("q")
    if q:
        qs = qs.filter(title__icontains=q)
    qs = qs.filter(user=request.user)
    return render(request, 'video/myVideos.html', {'videoList': qs})


def videoUpload(request):
    if request.method == 'POST':
        form = videoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.publishedDate = timezone.now()
            if post.videoURL != "":
                post.videoURL = "https://www.youtube.com/embed/" + str(post.videoURL)
            post.save()
            return redirect("myVideoDetail", pk=post.pk)
        else:
            return render(request, 'video/videoUpload.html', {'form': form})
    else:
        form = videoUploadForm()
        return render(request, 'video/videoUpload.html', {'form': form})


def videoEdit(request, pk):
    post = get_object_or_404(Video, pk=pk)
    videoObj = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = videoUploadForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = str(request.user)
            post.publishedDate = timezone.now()
            post.save()
            return redirect('myVideoDetail', pk=post.pk)
    else:
        form = videoUploadForm(instance=post)
    return render(request, 'video/videoEdit.html', {'form': form, 'videoObj': videoObj})


def videoDelete(request, pk):
    return render(request, 'video/videoDelete.html')


def videoDeleteConfirm(request, pk):
    videoObj = Video.objects.get(pk=pk)
    if str(request.user) == videoObj.user:
        videoObj.delete()
        return redirect("/video/myVideos")
    else:
        return redirect("/accounts/innormalAccess")