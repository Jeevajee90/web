from django.shortcuts import render
from .models import *
from .form import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from moviepy.video.io.VideoFileClip import VideoFileClip

# Create your views here.

def home(request):
    data=upload_user.objects.all().order_by('-created')
    return render(request,'./poster/index.html',{"datas": data})

def profile(request):
    user = request.user
    video_user =upload_user.objects.filter(user=user)
    images=Profile_dp.objects.filter(user=user)
    for videos in video_user:
        
        clip = VideoFileClip(videos.file.path)
        thumbnail_path = f'media/thumbnails/{videos.pk}.jpg'
        clip.save_frame(thumbnail_path, t=5)  
        videos.thumbnail = thumbnail_path 
    return render(request,'./poster/profile.html',{'videos':video_user,'photo':images})   

def register(request):
    form = CustomuserForm()
    if request.method == 'POST':
        form = CustomuserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Register success..")
            return redirect ('login_page')
    return render(request,'poster/register.html',{"form":form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:    
        if(request.method == 'POST'):
            name = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'login successfull...')
                return redirect('/')
            else:
                messages.error(request,"login error...")
                return redirect("login_page")
        return render(request,'poster/login.html')
    
def sing_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'sign out success..')
    return redirect('/')    

def uploads(request):
    if request.method == 'POST':
        user = request.user
        video_file =request.FILES['video']
        text_data =request.POST.get('text_data')
        upload_user.objects.create(user=user,file=video_file,description=text_data)
        messages.success(request,'upload successfull..')
        return redirect('profile')
    else:
        messages.error(request,'not uploaded..')
    return render(request,'poster/uploads.html')
        


