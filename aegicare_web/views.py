# from django.views.generic import TemplateView, FormView, RedirectView, View, UpdateView
from django.shortcuts import render
from django.utils.translation import ugettext as _
from news.models import news


# def language_proc(request):
#     from django.utils.translation import get_language
#     lang_prefix = get_language().lower()
#     if lang_prefix != 'zh-cn':
#         lang_prefix += '/'
#     else:
#         lang_prefix = ''
#     return lang_prefix
#     # return {'lang_prefix': lang_prefix}
#
# class HomePage(TemplateView):
#     template_name = 'home/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePage, self).get_context_data(**kwargs)
#         context['user'] = self.request.user
#         return context

def HomePage(request):
    latest_news = news.objects.all().order_by("time")
    if len(latest_news) >= 2:
        res = latest_news[0:2]
    else:
        res = latest_news
    return render(request, 'home.html',{'news':res})

def About(request):
    all_news = news.objects.all()
    return render(request, 'about.html', {"news": all_news})

def mission(request):
    return render(request, 'mission.html')

def geneticInfo(request):
    return render(request, 'genetic.html')

def cancerInfo(request):
    return render(request, 'cancer.html')

def cdss(request):
    return render(request, 'cdss.html')

def career(request):
    return render(request, 'career.html')

def team(request):
    return render(request, 'team.html')

def report(request):
    return render(request, 'report.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def workflow(request):
    return render(request, 'workflow.html')

