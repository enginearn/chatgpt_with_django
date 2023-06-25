from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from dotenv import load_dotenv
import os
import openai

dot_env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dot_env_path)
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ChapGPT(
    message: str, model="gpt-3.5-turbo", max_tokens=150, temperature=0.9
) -> str:
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": message},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    answer = response.choices[0].message.content
    return answer

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
def chat(request):
    if request.method == "POST":
        if request.POST.get("message") != "":
            message = request.POST.get("message")
            response = ask_ChapGPT(message)
            return JsonResponse({"message": message, "response": response})
        else:
            return JsonResponse({"message": "message is empty"})
    return render(request, "chatbot.html")
