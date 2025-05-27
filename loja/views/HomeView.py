#from django.http import HttpResponse
#def home_view(request):
 #   return HttpResponse('<h1>Olá mundo!</h1>')


from django.shortcuts import render
def home_view(request):
    return render(request, template_name='home/home.html', status=200)
