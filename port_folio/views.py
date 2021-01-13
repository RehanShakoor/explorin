from django.shortcuts import render


# Create your views here.
def p_IndexView(request):
    return render(request,'p_index.html')

def Page4View(request):
    return render(request,'page4.html')    

def Page3View(request):
    return render(request,'page3.html')    

def Page2View(request):
    return render(request,'page2.html')     

def ButtonView(request):
    return render(request,'button.html')  

def JqueryHw1(request):
    return render(request,'jqueryhw1.html')

def JqueryHw2(request):
    return render(request,'jqueryhw2.html')    




