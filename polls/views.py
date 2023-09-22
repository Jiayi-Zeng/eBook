from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse
from .models import Question, Choice, UserChoice, Publish, PublishForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.edit import FormView

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    questions = Question.objects.filter(published=True)

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all questions
        all_questions = Question.objects.all()

        # Check which questions the user has answered
        if self.request.user.is_authenticated:
            answered_questions_ids = UserChoice.objects.filter(user=self.request.user).values_list('question_id', flat=True)
        else:
            answered_questions_ids = []

        # Update the context
        context.update({
            'all_questions': all_questions,
            'answered_questions_ids': answered_questions_ids,
        })

        return context
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        user_choices = UserChoice.objects.filter(question=question)
        context['user_choices'] = user_choices
        return context


def vote(request, question_id):
    current_user = request.user

    # Check if the user has already made a choice for this question
    existing_choice = UserChoice.objects.filter(user=current_user, question_id=question_id).first()

    if existing_choice:
        messages.error(request, f'For Question {existing_choice.question}, you have already submitted Option {existing_choice.choice}')
        # Redirect to the appropriate page
    else:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choices.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # After saving the selected choice, save a UserChoice record
            user_choice = UserChoice(user=current_user, question_id=question_id, choice=selected_choice)
            user_choice.save()
    return HttpResponseRedirect(reverse("polls:index"))

class PublishView(FormView):
    form_class = PublishForm
    template_name = "polls/publish.html"
    success_url = '/some-success-url/'  

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            question_id = self.kwargs['pk']
            question = Question.objects.get(pk=question_id)
            context['question_text'] = question.question_text
            return context


    def form_valid(self, form):
        question_id = self.kwargs['question_id']
        question= Question.objects.get(pk=question_id)

        Publish.objects.create(question=question, delay_duration=form.cleaned_data['duration'])
        # publish.save()  
        return super().form_valid(form)


def publish(request, pk):
    snippet = get_object_or_404(Question, pk=pk)

    if not snippet.published:
        snippet.published = True
        snippet.save()
        messages.success(request, f'Snippet "{snippet.question_text}" published successfully.')
    else:
        messages.warning(request, f'Snippet "{snippet.question_text}" is already published.')

    return  HttpResponseRedirect('/admin/snippets/polls/question/')

