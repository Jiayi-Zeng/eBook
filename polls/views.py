from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse
from .models import Question, Choice, UserChoice, Publish
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.edit import FormView

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "republished_question_list"

    def get_queryset(self):
        """Return the published questions."""
        # publish_objects = Publish.objects.filter(status=True)
        # publish_questions = publish_objects.values_list('question', flat=True)
        # return publish_questions
        return Question.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check which questions the user has answered
        if self.request.user.is_authenticated:
            publish_objects = Publish.objects.filter(status=True)
            publish_ids = publish_objects.values_list('publish_id', flat=True)
            answered_questions_ids = UserChoice.objects.filter(user=self.request.user, publish_id__in=publish_ids).values_list('question_id', flat=True)
        else:
            answered_questions_ids = []

        # Update the context
        context.update({
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
    existing_choice = UserChoice.objects.filter(user=current_user, question_id=question_id, publish_id=publish_id).first()

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
                "polls/index.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # After saving the selected choice, save a UserChoice record
            user_choice = UserChoice(user=current_user, question_id=question_id, choice=selected_choice, publish_id=publish_id)
            user_choice.save()
    return HttpResponseRedirect(reverse("polls:index"))

    
def publish(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if not question.published:
        new_publish = Publish(question=question, status=True)
        new_publish.save()  

        question.published = True
        question.save()
        messages.success(request, f'Snippet "{question.question_text}" published successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already published.')

    return  HttpResponseRedirect('/admin/snippets/polls/question/')


def unpublish(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if question.published:
        new_publish = Publish(question=question, status=False)
        new_publish.save()  

        question.published = False
        question.save()
        messages.success(request, f'Snippet "{question.question_text}" unpublished successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already unpublished.')

    return HttpResponseRedirect('/admin/snippets/polls/question/')

