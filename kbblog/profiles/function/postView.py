import math

from django.core.paginator import Paginator

from django.core.exceptions import ObjectDoesNotExist

#model
from profiles.models import Post

def get_current_post(post_number):
    post = Post.objects

    try:
        post_qs = post.get(post_num=post_number)

        return {
            'post_qs': post_qs,
            'user_about_post_qs': post_qs.author
        }
    except ObjectDoesNotExist:
        return []

def get_recently_post(index, number):
    post = Post.objects
    try:
        return post.order_by(index)[:number]
    except ObjectDoesNotExist:
        return [] 

def post_calc_pagenator(current_page):
    qs = get_recently_post('post_date', 6)

    recently_post_list = qs.values('post_num', 'author_id', 'post_title', 'post_content', 'post_date')
    
    post_list = [
        {
            "title": 'first',
            "desc": 'Lorem Ipsum.',
            "date": 'date'
        },
        {
            "title": 'second',
            "desc": 'Lorem Ipsum is simply dummy text.',
            "date": 'date'
        },
        {
            "title": 'third',
            "desc": 'Lorem Ipsum is simply dummy text of the.',
            "date": 'date'
        },
        {
            "title": 'fourth',
            "desc": 'Lorem Ipsum is simply dummy text of the printing.',
            "date": 'date'
        },
        {
            "title": 'fifth',
            "desc": 'Lorem Ipsum is simply dummy text of the printing and typesetting.',
            "date": 'date'
        },
        {
            "title": 'sixth',
            "desc": 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            "date": 'date'
        }
    ]
    
    show_to_show = 16
    #paginator
    post_pagenator = Paginator(post_list, show_to_show)

    postData = {}
    postData['post_list'] = post_list
    postData['recently_post_list'] = recently_post_list
    postData['post_paginator'] = post_pagenator

    return postData
