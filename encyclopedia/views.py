from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, entry):

    valid_entry = util.get_entry(entry)

    if valid_entry:
        markdowner = Markdown()
        html_entry = markdowner.convert(valid_entry)
        title = entry.capitalize()

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
