from django.shortcuts import render
from django.views.generic.base import TemplateView

class ChatBotView(TemplateView):
    template_name = "chatbot/chatbot.html"

import zhipuai
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PromptSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

zhipuai.api_key = "7c0e5a4e41390082510d6d894b70c7d6.8dsT54HqVFbh3GwM"
messages = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好! 我是人工智能助手，很高兴见到你，欢迎问我任何问题。"}
  ]

# @method_decorator(csrf_exempt, name='dispatch')
class OpenAIView(APIView):
    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            messages.append({"role": "user", "content": prompt})
            
            response = zhipuai.model_api.invoke(
                model="chatglm_lite",
                prompt=messages
            )
            if 'data' in response:
                msg = response['data']['choices'][0]
                messages.append(msg)
                # return Response({'response': Response({'response': response['data']['choices'][0]})})
                return Response(response)
            else:
                print(response)

        return Response(serializer.errors, status=400)

