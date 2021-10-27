from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin

from django.views.defaults import permission_denied

# from mysite import crawling
#
# from django.shortcuts import render


#--TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
    
class BotView(TemplateView):
    template_name = 'schedulebot.html'    

#-User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm 
    sucess_url = reverse_lazy('register_done')
    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)
    
# #-crawlign 추가
# class CrawlingForm(TemplateView):
#     template_name = 'crawlingform.html' 
#
#
# def dispcrawling(request):
#     #response = request.GET.get('word',None)
#     #response.content.decode('utf8')
#
#     word = request.POST.get('word',None)
#     print('============= 크롤링 작업 ===================' + str(word))
#     data = crawling.search(word)
#     print(data)
#     return render(request,'dispCrawling.html',{"data":data})   
