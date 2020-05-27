from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

# Create your views here.
from .models import TodoModel
from .forms import TodoForm

def index(request):
    # return HttpResponse('My...TODOlst...') --testing purpose
    mytodomodel = TodoModel.objects.order_by('id')
    mytodoform = TodoForm()
    context = {'mytodomodel':mytodomodel, 'mytodoform': mytodoform}
    return render(request, 'todo/index.html', context)

@require_POST
def addNewTodo(request):
    mytodoform = TodoForm(request.POST)

    if mytodoform.is_valid():
        mynewtodo = TodoModel(todotext=request.POST['text'])
        mynewtodo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    mytodoobj = TodoModel.objects.get
    mytodoobj.complete = True
    mytodoobj.save()
    return redirect('index')

def deleteTodo(request):
    TodoModel.objects.filter(complete__exact=True).delete()
    return redirect('index')

