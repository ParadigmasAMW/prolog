from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from app.models import Software
# Create your views here.


def home(request):
    return render_to_response('home.html')


def search(request):
    return render_to_response('search.html',
                              context_instance=RequestContext(request))


def result(request):
    Software.populate_database()
    name = request.GET['name']
    category = request.GET['category']
    language = request.GET['language']
    license = request.GET['license']
    platform = request.GET['platform']
    size = request.GET['size']
    initial_date = request.GET['initial_date']
    final_date = request.GET['final_date']
    value = request.GET['value']

    Software.refresh_asserts()
    softwarelist = Software.filter()
    # softwarelist = Software.filter(
    #     name=name, category=category, language=language, license=license,
    #     platform=platform, size=size, initial_date=initial_date,
    #     final_date=final_date, value=value)

    print softwarelist

    return render_to_response('results.html')


def register(request):
    if request.method == 'GET':
        return render_to_response('register.html',
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        software = Software()
        software.Name = request.POST['proj_name']
        software.Category = request.POST['category']
        software.Language = request.POST['language']
        software.License = request.POST['license']
        software.Platform = request.POST['platform']
        software.Size = request.POST['size']
        software.Initial_Date = request.POST['initial_date']
        software.Final_Date = request.POST['final_date']
        software.Value = request.POST['value']
        software.save()

        Software.refresh_asserts()

        return redirect('/')
