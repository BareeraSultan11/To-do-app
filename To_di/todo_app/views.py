from django.shortcuts import render, redirect
from .models import Tasks
# Create your views here.
def create_task(request):
  if request.method=='POST':
    # to get values from form
    name = request.POST.get("name")
    descript = request.POST.get("descript")
    date = request.POST.get("date")
    Tasks.objects.create(name=name, descript=descript, date=date)
    return redirect("display")
  return render(request, "todo_app/create.html")
