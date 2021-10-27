from django.views.generic import ListView,DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from django.conf import settings
#댓글달기는 여기서
from blog.forms import PostSearchForm
from django.db.models import Q #검색기능이 있는 클래스
from django.shortcuts import render

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

#from django.views.generic import FormView #from django.views.generic import 앞대가리만 같으면 ,로 엮을 수 있음
#from django.forms.forms import Form

# Create your views here.

#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

#--- DetailView
class PostDV(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}-{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context
    
#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    
class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

#--- Tag View    
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'
    
class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post
    
    def get_queryset(self): #self=TaggedObjectLV, ListView를 상속받음
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self,**kwargs): #* : list형태, ** : dictionary형태
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    
#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'
    
    def form_valid(self,form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(
            Q(title__icontains = searchWord) |
            Q(description__icontains = searchWord) |
            Q(content__icontains = searchWord)
            ).distinct()
        context = {}
        
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        
        return render(self.request,self.template_name,context)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'} 
    #fields = ['title', 'description', 'content', 'tags'] 
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags']
    success_url = reverse_lazy('blog:index')


class PostDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('blog:index')
    
    