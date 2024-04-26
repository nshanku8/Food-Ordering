from django.shortcuts import render
from empmodule.models import Jobdetails


# Create your views here.
def viewfood(request):
    return render(request,'customermodule/viewfood.html')


def viewfood1(request):
    viewfood1=Jobdetails.objects.all()
    return render(request,'customermodule/viewfood.html',{'job_details_list':viewfood1})
def southveg(request):
    return render(request,'customermodule/southveg.html')
def addtocart(request):
    return render(request,'customermodule/addtocart.html')
def paynow(request):
    return render(request,'customermodule/paynow.html')
def deserts(request):
    return render(request,'customermodule/deserts.html')
def feedback(request):
    return render(request,'navbar/feedback.html')
def aboutus(request):
    return render(request,'navbar/aboutus.html')

def review_list(request):
    if request.method == 'GET':
        reviews = TouristReview.objects.all()
        return render(request,'reviewpage.html',{'reviews':reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('review_list')
        else:
            form = ReviewForm()
        return render(request,'reviewpage.html',{'form':form})