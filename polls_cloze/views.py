from django.shortcuts import render, get_object_or_404
from .models import ClozeQuestion, ClozePublish, ClozeUserChoice
from django.http import Http404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.db.models import Q, Max
from django.http import Http404
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

# def detail(request, question_id):
#     try:
#         question = ClozeQuestion.objects.get(pk=question_id)
#     except ClozeQuestion.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls_cloze/detail.html", {"question": question})

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = "polls_cloze/index.html"
    context_object_name = "publish_objects"

    def get_queryset(self):
        current_datetime = timezone.now()
        days_ago = current_datetime - timezone.timedelta(days=1)
        # 使用过滤器获取最近1天内发布的 Publish 实例
        return ClozePublish.objects.filter(status=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check which questions the user has answered
        if self.request.user.is_authenticated:
            publish = ClozePublish.objects.filter(status=True)
            answered_publish = ClozeUserChoice.objects.filter(user=self.request.user, publish__in=publish)
            answered_publish_id =  answered_publish.values_list('publish_id', flat=True)
            
            end_publish = ClozePublish.objects.filter(status=False)
            answered_end = ClozeUserChoice.objects.filter(user=self.request.user, publish__in=end_publish)
            answered_end_id =  answered_end.values_list('publish_id', flat=True)

            unanswered_publish = publish.exclude(
                Q(clozeuserchoice__user=self.request.user) | Q(publish_id__in=answered_publish)
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

def publish(request, pk):
    question = get_object_or_404(ClozeQuestion, pk=pk)
    
    if not question.published:
        new_publish = ClozePublish(question=question, status=True)
        new_publish.save()  

        question.published = True
        question.save()
        messages.success(request, f'Snippet "{question.question_text}" published successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already published.')

    return  HttpResponseRedirect('/admin/snippets/polls_cloze/clozequestion/')

def unpublish(request, pk):
    question = get_object_or_404(ClozeQuestion, pk=pk)

    publish_object_id = ClozePublish.objects.filter(question_id=pk).aggregate(max_id=Max('publish_id'))['max_id']
    publish_object = ClozePublish.objects.get(publish_id=publish_object_id)
    
    if publish_object.status:
        publish_object.status=False
        publish_object.save()

        question.published = False
        question.save()

        publish_answer = ClozeUserChoice.objects.filter(publish=publish_object)
        for user_choice in publish_answer:
            if user_choice.answer == publish_object.question.correct:
                user_choice.correct = True
                user_choice.save()
                
        messages.success(request, f'Snippet "{question.question_text}" unpublished successfully.')
    else:
        messages.warning(request, f'Snippet "{question.question_text}" is already unpublished.')

    return HttpResponseRedirect(f'/admin/snippets/polls_cloze/{pk}/')

def vote(request, question_id):
    current_user = request.user

    # Check if the user has already made a choice for this question
    publish_id = ClozePublish.objects.filter(question__id=question_id).aggregate(max_id=Max('publish_id'))['max_id']
    publish = ClozePublish.objects.get(publish_id=publish_id)

    existing_choice = ClozeUserChoice.objects.filter(user=current_user, publish=publish).first()


    # if existing_choice:
    #     # messages.error(request, f'For Question, you have already submitted Option {existing_choice.answer}')
    #     # Redirect to the appropriate page
    #     pass
    # else:
    publish_object = ClozePublish.objects.get(publish_id=publish_id)
    question = publish_object.question
    
    answer = request.POST.get('answer')
    answer = answer.replace(" ", "").replace("\n", "")
    
    user_choice = ClozeUserChoice(user=current_user, answer=answer, publish_id=publish_id)
    print(user_choice)
    user_choice.save()

    url = request.path.replace("/vote/", "")
    return redirect(url)

def vote2(request, question_id):
    current_user = request.user

    # Check if the user has already made a choice for this question
    publish_id = ClozePublish.objects.filter(question__id=question_id).aggregate(max_id=Max('publish_id'))['max_id']
    publish = ClozePublish.objects.get(publish_id=publish_id)

    existing_choice = ClozeUserChoice.objects.filter(user=current_user, publish=publish).first()


    # if existing_choice:
    #     # messages.error(request, f'For Question, you have already submitted Option {existing_choice.answer}')
    #     # Redirect to the appropriate page
    #     pass
    # else:
    publish_object = ClozePublish.objects.get(publish_id=publish_id)
    question = publish_object.question
    
    answer = request.POST.get('answer')
    answer = answer.replace(" ", "").replace("\n", "")
    
    user_choice = ClozeUserChoice(user=current_user, answer=answer, publish_id=publish_id)
    print(user_choice)
    user_choice.save()

    return HttpResponseRedirect(reverse("polls:history"))


class ResultsView(generic.DetailView):
    model = ClozeQuestion
    template_name = "polls_cloze/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        question = self.get_object()
        all_publish_id = ClozePublish.objects.filter(question=question).values_list('publish_id', flat=True)

        publish_id = self.request.GET.get('publish_id')
        if not publish_id:
            publish_id = ClozePublish.objects.filter(question=question).aggregate(max_id=Max('publish_id'))['max_id']
       
        publish_object = get_object_or_404(ClozePublish, pk=publish_id)
        user_choices = ClozeUserChoice.objects.filter(publish=publish_id)
        
       
        
        context = {
            'user_choices': user_choices,
            'question': question,
            'publish_id': publish_id,
            'all_publish_id': all_publish_id,
        }
        return context


@method_decorator(login_required, name='dispatch')
class HistoryView(generic.ListView):
    template_name = "polls/history.html"
    context_object_name = "answer_objects"

    def get_queryset(self):
        """Return the answered questions."""
        published_history = ClozePublish.objects.filter(status=False)
        return ClozeUserChoice.objects.filter(user=self.request.user, publish__in=published_history)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        questions = ClozeQuestion.objects.all()
        
        if self.request.user.is_authenticated:
            user_answer = ClozeUserChoice.objects.filter(user=self.request.user).values_list('publish_id', flat=True)
            user_choice = ClozeUserChoice.objects.filter(user=self.request.user)
            answered_question_list =  ClozePublish.objects.filter(publish_id__in=user_answer).values_list('question_id', flat=True)
        else:
            user_answer = None
            user_choice = None
            answered_question_list = None

        answered_publish = ClozeUserChoice.objects.filter(user=self.request.user, publish__in=publish)
        answered_publish_id =  answered_publish.values_list('publish_id', flat=True)

        context = {
            'cloze_questions': questions,
            'cloze_user_answer': user_answer,
            'cloze_answered_question_list': answered_question_list,
            'cloze_user_choice': user_choice,
            'answered_publish_id': answered_publish_id
        }
        return context
    
def detail(request, question_id):
    try:
        question = ClozeQuestion.objects.get(pk=question_id)
    except ClozeQuestion.DoesNotExist:
        raise Http404("ClozeQuestion does not exist")
    
    publish_id = ClozePublish.objects.filter(question=question).aggregate(max_id=Max('publish_id'))['max_id']
    if publish_id:
        publish = get_object_or_404(ClozePublish, pk=publish_id)
    else:
        publish = None

    if request.user.is_authenticated:
        user_answer_id = ClozeUserChoice.objects.filter(user=request.user, publish__question_id=question_id).aggregate(max_id=Max('id'))['max_id']
        if user_answer_id:
            user_answer = ClozeUserChoice.objects.get(id=user_answer_id)
        else:
            user_answer = None
        num = ClozeUserChoice.objects.filter(user=request.user, publish__question_id=question_id).count()
        flag = True
    else: 
        flag = False
        user_answer = None
        num = 0

    context = {
        'question': question,
        'user_answer': user_answer,
        'publish': publish,
        'flag': flag,
        'num': num
    }
    return render(request, "polls_cloze/detail_page.html", context)
 
from .serializers import ClozeQuestionSerializer, ClozePublishSerializer, ClozeUserChoiceSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class ClozeQuestionViewSet(viewsets.ModelViewSet):
    queryset = ClozeQuestion.objects.all()
    serializer_class = ClozeQuestionSerializer
    
class ClozePublishViewSet(viewsets.ModelViewSet):
    queryset = ClozePublish.objects.all()
    serializer_class = ClozePublishSerializer


class ClozeUserChoiceViewSet(viewsets.ModelViewSet):
    queryset = ClozeUserChoice.objects.all()
    serializer_class = ClozeUserChoiceSerializer

