from django.shortcuts import render, redirect
from memories.models import Memory
from memories.forms import MemoryForm

# Create your views here.
def memories(request):
    ctx = {}
    if request.method == "POST":
        memory_form = MemoryForm(request.POST)
        if memory_form.is_valid():
            Memory.objects.create(
                title=memory_form.cleaned_data['title'],
                description=memory_form.cleaned_data['description'],
                start_date=memory_form.cleaned_data['start_date']
            )
        else:
            ctx["errors"] = memory_form.errors
    else:
        memory_form = MemoryForm()
    ctx["memories"] = Memory.objects.all().order_by('start_date')
    ctx["form"] = memory_form
    return render(request, "index.html", ctx)

def confirm_delete(request, id):
    memory = Memory.objects.get(id=id)
    ctx = {
        "memory": memory
    }
    return render(request, "confirm_delete.html", ctx)

def delete(request, id):
    Memory.objects.filter(id=id).delete()
    return redirect("/")