from django.shortcuts import redirect


def not_logged_in_required(view_funtion):
    def wrapper(request,*args,**kwarsg):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_funtion(request,*args, **kwarsg)
    return wrapper    
    