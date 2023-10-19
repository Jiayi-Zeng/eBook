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
from django.db.models import Max, Count, Q
from django.http import Http404
from django.utils import timezone

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "publish_objects"

    def get_queryset(self):
        current_datetime = timezone.now()
        days_ago = current_datetime - timezone.timedelta(days=1)
        # 使用过滤器获取最近1天内发布的 Publish 实例
        return Publish.objects.filter(status=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check which questions the user has answered
        if self.request.user.is_authenticated:
            publish = Publish.objects.filter(status=True)
            answered_publish = UserChoice.objects.filter(user=self.request.user, publish__in=publish)
            answered_publish_id =  answered_publish.values_list('publish_id', flat=True)
            
            end_publish = Publish.objects.filter(status=False)
            answered_end = UserChoice.objects.filter(user=self.request.user, publish__in=end_publish)
            answered_end_id =  answered_end.values_list('publish_id', flat=True)

            unanswered_publish = publish.exclude(
                Q(userchoice__user=self.request.user) | Q(publish_id__in=answered_publish)
            )

        else:
            answered_publish = []
            answered_publish_id = []
            answered_end = []
            answered_end_id = []
            unanswered_publish = []

        # Update the context
        context.update({
            'answered_publish': answered_publish,
            'answered_publish_id': answered_publish_id,
            'answered_end': answered_end,
            'answered_end_id': answered_end_id,
            'unanswered_publish': unanswered_publish
        })

        return context
    
@method_decorator(login_required, name='dispatch')
class HistoryView(generic.ListView):
    template_name = "polls/history.html"
    context_object_name = "answer_objects"

    def get_queryset(self):
        """Return the answered questions."""
        published_history = Publish.objects.filter(status=False)
        return UserChoice.objects.filter(user=self.request.user, publish__in=published_history)
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        question = self.get_object()
        all_publish_id = Publish.objects.filter(question=question).values_list('publish_id', flat=True)

        publish_id = self.request.GET.get('publish_id')
        if not publish_id:
            publish_id = Publish.objects.filter(question=question).aggregate(max_id=Max('publish_id'))['max_id']
       
        publish_object = get_object_or_404(Publish, pk=publish_id)
        user_choices = UserChoice.objects.filter(publish=publish_id)
        
        choice_vote_dict = countVote(publish_object)

        context = {
            'user_choices': user_choices,
            'question': question,
            'publish_id': publish_id,
            'all_publish_id': all_publish_id,
            'choice_vote_dict': choice_vote_dict
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

    publish_object_id = Publish.objects.filter(question_id=pk).aggregate(max_id=Max('publish_id'))['max_id']
    publish_object = Publish.objects.get(publish_id=publish_object_id)
    
    if publish_object.status:
        publish_object.status=False
        publish_object.save()

        question.published = False
        question.save()

        publish_answer = UserChoice.objects.filter(publish=publish_object)
        for user_choice in publish_answer:
            if user_choice.choice == publish_object.question.correct_choice:
                user_choice.correct = True
                user_choice.save()
                
        messages.success(request, f'Snippet "{question.question_text}" unpublished successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already unpublished.')

    return HttpResponseRedirect(f'/admin/snippets/polls/{pk}/')

def countVote(publish):
    question = Question.objects.get(publish=publish)

    choices = Choice.objects.filter(question=question)
    choice_vote_dict = {choice.choice_text: 0 for choice in choices}
    
    user_choices = UserChoice.objects.filter(publish=publish)
    choice_counts = user_choices.values('choice').annotate(choice_count=Count('choice'))

    # 现在 choice_counts 包含每个 Choice 的 text 和票数
    for choice_info in choice_counts:
        choice_id = choice_info['choice']
        choice_count = choice_info['choice_count']
        choice = Choice.objects.get(pk=choice_id)
        choice_text = choice.choice_text
        choice_vote_dict[choice_text] = choice_count\
        
    return choice_vote_dict

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
 
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        question_id = self.get_object()
        
        question_object = get_object_or_404(Publish, pk=question_id)
    
        context = {
            'question': question_object,
            'question_id': question_id,
        }
        return context