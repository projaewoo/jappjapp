from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import FileUpload

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES['imgFile']
        fileupload = FileUpload(
            title=title,
            content=content,
            imgFile=img,
        )
        fileupload.save()
        return redirect('/homepage')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'upload_template.html', context)