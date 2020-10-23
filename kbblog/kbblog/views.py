from django.shortcuts import redirect

from django.views import View

class indexView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/profiles/')