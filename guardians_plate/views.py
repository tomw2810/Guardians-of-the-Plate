from django.shortcuts import render

# Create your views here.
def get_guardians_plate(request):
    return render(request, 'guardians_plate/home.html')
