from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy


def group_required(*groups):

    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            return HttpResponseRedirect(reverse_lazy("registrar"))

        return wrapper

    return decorator