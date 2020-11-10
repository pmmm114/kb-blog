from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from django.views import View
from django.views import generic

#Post.Form
from .forms import PostClientForm
#Post.Function
from profiles.function.postView import post_calc_pagenator
from profiles.function.postView import get_current_post

class MainViewClass(View):
    def get(self, request, *args, **kwargs):
        rendered = render_to_string('profiles/profile_index.html', {
            'cssFiles': [
                'profiles/scss/main.scss',
            ],
            'cdn_link_js': [
                "https://unpkg.com/swiper/swiper-bundle.min.js",
            ],
            'cdn_link_css': [
                "https://unpkg.com/swiper/swiper-bundle.min.css",
            ],
        }, request)
        return HttpResponse(rendered)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', None)

        if page is None:
            return redirect('/profiles/post?page=1')

        # page number required, default: 1
        post_dictionary = post_calc_pagenator(page)

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
