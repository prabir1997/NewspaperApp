# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # new

from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView # new
from django.urls import reverse_lazy # new
from .models import Article


from django.shortcuts import render
class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    
class ArticleDetailView(LoginRequiredMixin,DetailView): # new
    model = Article
    template_name = 'article_detail.html'
class ArticleUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    
    # def get_queryset(self): # new
    #     queryset = super().get_queryset()
    #     return queryset.filter(author=self.request.user)
    
    def test_func(self):
        return self.request.user == self.get_object().author
    
    
    
    
class ArticleDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    # def get_queryset(self): # new
    #     queryset = super().get_queryset()
    #     return queryset.filter(author=self.request.user)
    
    def test_func(self):
        return self.request.user == self.get_object().author
    
class ArticleCreateView(CreateView,LoginRequiredMixin): # new    
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def home(request):
    return render(request,'home.html')




    

