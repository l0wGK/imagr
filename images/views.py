from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_image = Image(
            file = request.FILES['img']
        )
        new_image.save()
        return render(request, 'index.html', {'new_url': str('localhost:8000' + new_image.file.url)})
    else:
        return render(request, 'index.html')