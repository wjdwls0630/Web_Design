from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Question, Choice
from django.utils import timezone


class IndexView(generic.ListView):
    """docstring forIndexView."""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self) :
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """docstring forDetailView."""
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """docstring forResultsView."""
    model = Question
    template_name = 'polls/results.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :
        return render(request, 'polls/detail.html',{
        'question' : question,
        'error_message' : "You didn't select a choice!"
        })
    else :
        selected_choice.vote=selected_choice.vote+1
        selected_choice.save()
        return redirect('results', pk=pk)
