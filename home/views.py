# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(request):
    userName = request.user.username
    return render(request, "home/index.html", {"name":userName})

def sum(request):
    return render(request, "home/sum.html")

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    ans = val1 + val2
    return render(request, "home/sum.html", {"result": ans})

def show_items(response, id):
    # Show items for a ToDoList with the following id
    ls = ToDoList.objects.get(id=id) # Adding to list no 2

    if ls in response.user.todolist.all():
        # only show the ToDoList if the current user made that ToDoList

        if response.method=='POST':
            # print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt)>2:
                    # Validation
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")

    else:
        # If someone tries to do that show them this error page
        return render(response, "home/not_allowed.html")
    
    return render(response, "home/show_items.html", {"myList": ls})

def create_list(response):
    # Create a todolist for a user
    if response.method=="POST":
        listName = response.POST.get("listName")
        t = ToDoList(name=listName)
        t.save()
        response.user.todolist.add(t)
        # ---  instead of :
        # t = ToDoList(name=listName)
        # t.save()

    return render(response, "home/create_list.html")

def view_list(response):
    return render(response, "home/view_list.html")



##  ------- EXTRA ----------
def addEntry_prev(request):
    # for normal html form
    if request.method=="POST":
        id = int(request.POST.get("id"))
        itemName = request.POST.get("itemName", "")
        isComplete = request.POST.get("complete", False) == "on"
        # Note: if the checkbox is not ticked we've to give False on our own

        t = ToDoList(id=id)
        # t.save() # This is used when creating a new object
        t.item_set.create(text=itemName, complete=isComplete)

    return render(request, "home/add_entry.html")

from .forms import AddEntryForm

def addEntry(request):
    if request.method == "POST":
        form = AddEntryForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            itemName = form.cleaned_data['itemName']
            isComplete = form.cleaned_data['complete']

            t = ToDoList(id=id)
            t.item_set.create(text=itemName, complete=isComplete)
            return render(request, "home/add_entry.html")
    else:
        form = AddEntryForm()

    return render(request, "home/add_entry.html", {'form': form})

