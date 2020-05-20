from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo

# Create your views here.


class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'   #장고에서 알아서 찾아가도록

class PhotoCreate(CreateView):  # CreateView 상속받아
    model = Photo
    fields = ['author', 'text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

    def from_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            #form:모델폼
            form.instance.save()
            return redirect('/')
        else:
            #올바르지않다면
            return self.render_to_response({'form':form})

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['author', 'text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

#generic view를 상속 받았기 때문에 field가 꼭필요함

class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'

