from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import Counter
import re
# Create your views here.
from django.views.generic import TemplateView, ListView

from . import forms
from .models import Note


def count_unique_words(text):
    words = re.findall(r"[a-я'-]+", text.lower())
    unique_words_number = len(dict((k, v) for k, v in Counter(words).items() if v == 1))
    return unique_words_number


def index(request):
    return render(request, 'base.html')


def success(request):
    return render(request, 'success.html', {"success": "Поздравляем! Ваша заметка добавлена успешно!"})


class NoteFormView(TemplateView):
    template_name = 'add_notes.html'

    form_for_note = forms.NoteForm

    def post(self, request):
        form = forms.NoteForm(request.POST)
        context = {
            'form_for_note': form
        }

        if form.is_valid():
            note = Note()
            note.text = form.cleaned_data["text"]
            note.count_unique_words = count_unique_words(note.text)
            note.save()
            return redirect("/success/")
        else:
            return render(request, self.template_name, context)

    def get(self, request):
        context = {
            'form_for_note': self.form_for_note
        }
        return render(request, self.template_name, context)


class NotesListView(ListView):
    template_name = "notes.html"
    context_object_name = "notes_list"

    def get_queryset(self):
        return Note.objects.order_by("-count_unique_words")
