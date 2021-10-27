from django.shortcuts import render
from django.views.generic import ListView,DetailView
from bookmark.models import Bookmark
from boto.connection import HTTPResponse

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    
class BookmarkDV(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'
    
def start(request):
    return HTTPResponse(
        '''<h1>장고 프로젝트 연습</h1>
            <a href='admin/'>관리자모드</a>
            <a href='bookmark/'>북마크</a>''')
    
class BookmarkCreateView(LoginRequiredMixin, CreateView): 
    model = Bookmark 
    fields = ['title', 'url'] 
    success_url = reverse_lazy('bookmark:index') 

    def form_valid(self, form): 
        form.instance.owner = self.request.user 
        return super().form_valid(form) 


class BookmarkChangeLV(LoginRequiredMixin, ListView): 
    template_name = 'bookmark/bookmark_change_list.html' 

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): 
    model = Bookmark 
    fields = ['title', 'url'] 
    success_url = reverse_lazy('bookmark:index') 


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): 
    model = Bookmark 
    success_url = reverse_lazy('bookmark:index')