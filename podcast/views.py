from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from models import Episode
from forms import Search
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            template = loader.get_template('index.html')
            ep = Episode.objects.all().filter(Q(date__icontains=query) | Q(title__icontains=query) | Q(desc__icontains=query))
            result = template.render(context={'episode_details': ep, 'query': query})
            return HttpResponse(result)
    else:
        template = loader.get_template('index.html')
        ep = Episode.objects.all()
        result = template.render(context={'episode_details':ep})
        return HttpResponse(result)