from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout, login, authenticate


from django.views import View
from django.views import generic

#Post.Form
from .forms import PostClientForm
#Post.Function
from profiles.function.postView import post_calc_pagenator
from profiles.function.postView import get_current_post

#auth function
from profiles.function.auth_func import is_authenticated

#Login.Form
from .forms import LoginForm

#login decorators
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#conditional redirect decorator
from django.contrib.auth.decorators import user_passes_test

class MainViewClass(View):
    def get(self, request, *args, **kwargs):
        rendered = render_to_string('profiles/profile_index.html', {
            'cssFiles': [
                'profiles/scss/main.scss',
            ]
        }, request)
        return HttpResponse(rendered)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        # page number required, default: 1
        post_dictionary = post_calc_pagenator(1)

        #paginator
        rendered = render_to_string('profiles/profile_post.html', {
            'cssFiles': [
                'profiles/scss/post.scss',
            ],
            'postList': post_dictionary['post_list'],
            'recentlyPostList': post_dictionary['recently_post_list'],
            'postPage': post_dictionary['post_paginator'].page_range
        }, request)
        return HttpResponse(rendered)

class PostDetailView(View):
    template = 'profiles/profile_post_detail.html'

    def get(self, request, *args, **kwargs):
        # get param ( post_id )
        post_detail_object = get_current_post(self.kwargs['post_id'])
        
        post_detail_model = post_detail_object['post_qs']
        user_about_post_model = post_detail_object['user_about_post_qs']

        author = (user_about_post_model.username) if (user_about_post_model.first_name is not None and user_about_post_model.last_name is not None) else (user_about_post_model.first_name + user_about_post_model.last_name) 

        rendered = render_to_string(PostDetailView.template, {
            'cssFiles': [
                'profiles/scss/post.scss',
            ],
            'post': {
                'post_author': author,
                'post_title': post_detail_model.post_title,
                'post_content': post_detail_model.post_content,
                'post_date': post_detail_model.post_date,
            },
        }, request)

        return HttpResponse(rendered)

@method_decorator(login_required, name='post')
@method_decorator(login_required, name='get')
class PostWriteView(View):
    template = 'profiles/profile_post_write.html'

    def post(self, request, *args, **kwargs):
        # get param ( post_id )
        form = PostClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(post, request.user.id)
            post.author_id = request.user.id
            post.save()
            return redirect('/profiles/post')

        rendered = render_to_string(PostWriteView.template, {
            'cssFiles': [
                'profiles/scss/post.scss',
            ],
            'test': self.kwargs['post_id']
        }, request)

        return HttpResponse(rendered)
    
    def get(self, request, *args, **kwargs):
        form = PostClientForm()

        rendered = render_to_string(PostWriteView.template, {
            'cssFiles': [
                'profiles/scss/post.scss',
            ],
            'cdn_link_css': [
                'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/codemirror.min.css',
                'https://uicdn.toast.com/editor/latest/toastui-editor.min.css',
            ],
            'cdn_link_js': [
                'https://uicdn.toast.com/editor/latest/toastui-editor-all.min.js',
            ],
            'form': form
        }, request)

        return HttpResponse(rendered)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(request.GET['next'])

# login_url = return url
# @method_decorator(user_passes_test(is_authenticated), name='post')
# @method_decorator(user_passes_test(is_authenticated), name='get')
class Loginview(View):
    template = 'profiles/login.html'
    form = LoginForm()

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            url =  '/profiles' if (request.GET.get('next', None) is None) else request.GET.get('next', None)
            return redirect(url)
        else:
            rendered = render_to_string(Loginview.template, {
                'cssFiles': [
                    'profiles/scss/login.scss',
                ],
                'form': Loginview.form,
                'login_fail_check': True
            }, request)
            return HttpResponse(rendered)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/profiles')
        else:
            rendered = render_to_string(Loginview.template, {
                'cssFiles': [
                    'profiles/scss/login.scss',
                ],
                'form': Loginview.form
            }, request)
            return HttpResponse(rendered)


    