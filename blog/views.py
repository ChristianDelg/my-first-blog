from django.shortcuts import render
from django.utils import timezone
from . models import Post
# Create your views here.
def post_list(request):
        #sera que esto aparece
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})

def login(request):
        mensaje = ''
        if request.method == 'POST':
                mensaje = 'Mensaje enviado cn POST'
        else:
                mensaje = 'sin post'
        return render(request, 'blog/login.html', {'mensaje': mensaje})

#renderizara(construira)