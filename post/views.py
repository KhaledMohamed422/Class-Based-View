from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView
# Create your views here.

# Class Based View
# https://ccbv.co.uk/


class PostList(ListView):
    """default for CBV

    TemplateName : return <NameModel>_<list.html>

    To Change : 

    a) Using attribute : 
       template_name = "post/data.html" 

    b) Using a method : 
        def get_template_names(self):
            return ['new_template.html']

    The default query :  <NameModel>.objects.all() 

    To Change : 

    a) Using attributes : 
       queryset = MyModel.objects.filter(some_field='some_value') 

    b) Using a methods : 
       def get_queryset(self):
          return MyModel.objects.filter(some_field='some_value')

    The default context  :  object_list  

    To Change : 

    a) Using attributes : 
       context_object_name = 'my_object_list'

    b) Using a methods : 
       def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs) # This add too context of default to django
            context['some_key'] = 'some_value'
            return context

    """
    model = Post
    # template_name = "post/data.html" --> a)


class PostDetail(DetailView):
    model = Post


# class PostDelete(DeleteView):
    # pass


# class PostList():
#     pass
