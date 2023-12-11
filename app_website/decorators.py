from django.shortcuts import render, redirect

def requires_form_submitted(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('form_submitted', False):
            return redirect('home.html')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
