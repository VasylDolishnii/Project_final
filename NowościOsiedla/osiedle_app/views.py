from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, TemplateView

from osiedle_app.models import Post
from django.contrib.auth.decorators import login_required

class ProtectedView(TemplateView):
    template_name = 'login.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@method_decorator(login_required)
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
	model = Post
	template_name = 'new_post.html'
	fields = '__all__'


class PostEditView(UpdateView):
	model = Post
	template_name = 'edit_post.html'
	fields = ['title', 'content']


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')