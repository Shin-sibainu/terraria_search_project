from django.shortcuts import render

# Create your views here.
def homeView(request):
  domain_url = request.META.get("HTTP_HOST")
  context = {
    'domain_url': domain_url
  }
  return render(request, 'home.html', context)
