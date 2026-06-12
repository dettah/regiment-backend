from django.urls import path
from .views import *

urlpatterns = [

    path(
        "chatbot/",
        chatbot
    ),

    path(
        "tts/",
        text_to_speech
    ),

    path(
        "stt/",
        speech_to_text
    ),

    path(
        "quiz/",
        get_quiz
    ),

    path(
        "quiz/submit/",
        submit_quiz
    ),

]