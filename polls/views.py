from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from .models import Question, Choice, UserChoice
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
    
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
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"



class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        user_choices = UserChoice.objects.filter(question=question)
        context['user_choices'] = user_choices
        return context
    
    list_display = ('user', 'question', 'choice')
    search_fields = ('user__username', 'question__question_text', 'choice__choice_text')

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