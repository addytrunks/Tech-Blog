from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView,TemplateView
from .models import Post,Category
from .forms import AddPostForm,UpdatePostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def LikeViews(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False

    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog:detail',args=[str(pk)]))


def Profile(request):
    count = Post.objects.filter(author=request.user.id).count()
    return render(request,'profile.html',context={'count':count,})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 3


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    order_by = ['name']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context =super(CategoryListView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context



def CategoryView(request,cats):
    #you are filtering(storing only)categories from the Post model
    category_list = Post.objects.filter(category=cats)
    return render(request,'categories.html',context={'cats':cats,'category_list':category_list})

def about(request):
    return render(request,'about.html')

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self,*args,**kwargs):
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])

        total_likes = stuff.total_likes()

        liked = False

        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context =super(ArticleDetailView, self).get_context_data(*args,**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked

        return context

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = AddPostForm

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = UpdatePostForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')


def search(request):
    query = request.GET['query']

    posts = Post.objects.filter(title__icontains=query,text__icontains=query)
    return render(request,'search.html',{'posts':posts,'query':query})
