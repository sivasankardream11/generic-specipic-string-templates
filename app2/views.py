from django.shortcuts import render

# Create your views here.
def htmlfile_1(request):
    return render(request,'htmlfile_1.html')

def htmlfile_2(request):
    return render(request,'htmlfile_2.html')