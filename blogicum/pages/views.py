from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'


class RulesTemplateView(TemplateView):
    template_name = 'pages/rules.html'


def permission_denied(request, exception):
    return render(request, 'pages/403.html', HttpResponseForbidden)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', HttpResponseForbidden)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', HttpResponseNotFound)


def server_error(request):
    return render(request, 'pages/500.html', HttpResponseServerError)
