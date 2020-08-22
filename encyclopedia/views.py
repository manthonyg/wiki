from django.shortcuts import render, redirect
from markdown2 import Markdown
from django.http import Http404
from . import util
from .forms import NewEntryForm
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def view_entry(request, title):
    valid_entry = util.get_entry(title)
    print(valid_entry, title)
    if valid_entry:
    
        html_entry = markdowner.convert(valid_entry)
        title = title.capitalize()

        return render(request, "encyclopedia/wiki.html", {
            "entry": html_entry,
            "title": title
        })
    else:
        error_title = 'Entry not found'
        error_body = 'No entry matches your request'
     
        return render(request, "encyclopedia/error.html", {
            "error_title": error_title,
            "error_body": error_body
        })

def search(request):
    q = request.GET.get('q').strip()

    if q in util.list_entries():
        return redirect("view_entry", title=q)

    matches = util.search(q)
    return render(request, "encyclopedia/search.html", {
        "entries": matches,
        "q": q
    })

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title=request.POST['title']
            content=request.POST['content']
            util.save_entry(title=title, content=content)
            return redirect('view_entry', title=title)
    else:
        form = NewEntryForm()
        return render(request, 'encyclopedia/new.html', {
        'form': form
    })

def edit(request):
    title = request.GET['title']
    content = util.get_entry(title)
    form = NewEntryForm(initial={'title': title, 'content': content})
    form.title = title
    form.content = content
    print(form)
    return render(request, 'encyclopedia/new.html', {
        'form': form,
        'title': title,
        'edit': True
    })
    


def random(request):
    random_entry = util.random_index()
    return redirect("view_entry", title=random_entry)
    