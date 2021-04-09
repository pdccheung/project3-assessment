from django.shortcuts import render, redirect
from .models import Widget
from django.db.models import Sum

# Create your views here.
def home(request):
    if Widget.objects.all().exists():
        widgets = Widget.objects.all()
        count = widgets.aggregate(Sum("quantity"))["quantity__sum"]
    else:
        widgets = None
        count= None
    
    return render(request, 'home.html', {
        "widgets": widgets,
        "count": count,
    }
    )

def delete_widget(request, w_id):
    print(w_id)
    w = Widget.objects.get(id=w_id)
    w.delete()
    response = redirect("home")
    return response

def add_widget(request):
    w = Widget(
        description=request.POST.get("description"),
        quantity=request.POST.get("quantity")
    )
    w.save()
    response = redirect("home")
    return response