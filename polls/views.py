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
from django.db.models import Max

# @method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "publish_objects"

    def get_queryset(self):
        """Return the published questions."""
        # publish_objects = Publish.objects.filter(status=True)
        # publish_questions = publish_objects.values_list('question', flat=True)
        # return publish_questions
        return Publish.objects.filter(status=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check which questions the user has answered
        if self.request.user.is_authenticated:
            publish_objects_ids = Publish.objects.filter(status=True).values_list('publish_id', flat=True)
            answered_publish_ids = UserChoice.objects.filter(user=self.request.user, publish_id__in=publish_objects_ids).values_list('publish_id', flat=True)
        else:
            answered_publish_ids = []

        # Update the context
        context.update({
            'answered_publish_ids': answered_publish_ids,
        })

        return context
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        question = self.get_object()
        
        all_publish_id = publish_id = Publish.objects.filter(question=question).values_list('publish_id', flat=True)
        new_publish_id = Publish.objects.filter(question=question).aggregate(max_id=Max('publish_id'))['max_id']
        publish_object = get_object_or_404(Publish, pk=new_publish_id)
        
        user_choices = UserChoice.objects.filter(publish=publish_object)
        
        context = {
            'user_choices': user_choices,
            'question': question,
            'new_publish_id': new_publish_id,
            'all_publish_id': all_publish_id
        }
        return context


def vote(request, publish_id):
    current_user = request.user

    # Check if the user has already made a choice for this question
    existing_choice = UserChoice.objects.filter(user=current_user, publish_id=publish_id).first()

    if existing_choice:
        messages.error(request, f'For Question, you have already submitted Option {existing_choice.choice}')
        # Redirect to the appropriate page
    else:
        publish_object = Publish.objects.get(publish_id=publish_id)
        question = publish_object.question
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
            user_choice = UserChoice(user=current_user, choice=selected_choice, publish_id=publish_id)
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

    publish_id = Publish.objects.filter(question_id=pk).aggregate(max_id=Max('publish_id'))['max_id']
    publish_object = get_object_or_404(Publish, pk=publish_id)

    if publish_object.status:
        publish_object.status=False
        publish_object.save()

        question.published = False
        question.save()
        messages.success(request, f'Snippet "{question.question_text}" unpublished successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already unpublished.')

    return HttpResponseRedirect('/admin/snippets/polls/question/')

