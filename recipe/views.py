from django.shortcuts import render,redirect
from .models import recipe
from .forms import ItemDetail
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.


def home(request):
    recipes = recipe.objects.all()[:11]
    data = {
        'recipes':recipes,
    }
    return render(request, "blogs.html",data)

def search(request):
    if request.method=='POST':
        f = request.POST['search']
        if f is not None:
            o = recipe.objects.filter(category=f)
            print("hello")
            return render(request,'detail.html',{'p':o})
        else:
            return redirect('/')
    else:
        return redirect('/')

def post(request,id):
    item = recipe.objects.get(id=id)
    return render(request,'post.html',{'item':item})
#
# def create_item(request):
#     form = ItemDetail(request.POST or None)
#     print("nicha")
#
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,"item-add.html",{'form':form})
def create_item(request):
    upload = ItemDetail()
    if request.method == 'POST':
        upload = ItemDetail(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/'}}">reload</a>""")
    else:
        return render(request, 'item-add.html', {'upload_form':upload})
def about(request):
    return render(request,'about.html',{})


def update(request, id):
    id = int(id)
    try:
        book_sel = recipe.objects.get(id = id)
    except recipe.DoesNotExist:
        return redirect('/')
    form = ItemDetail(request.POST or None, instance = book_sel)
    if form.is_valid():
       form.save()
       return redirect('/')
    return render(request, 'item-add.html', {'upload_form':form})

def delete(request, id):
    id = int(id)
    try:
        sel = recipe.objects.get(id = id)
    except recipe.DoesNotExist:
        return redirect('/')
    sel.delete()
    return redirect('/')



