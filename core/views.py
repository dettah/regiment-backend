
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import *
from .serializers import *
from .services.nlp_service import ask_nlp
from pathlib import Path
from gtts import gTTS
import speech_recognition as sr
import uuid
import random


@api_view(['POST'])
def chatbot(request):

    text = request.data.get("message")

    result = ask_nlp(text)

    return Response(result)


@api_view(['POST'])
def text_to_speech(request):

    text = request.data.get("text")
    
    media_dir = Path(settings.MEDIA_ROOT)

    media_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{uuid.uuid4()}.mp3"
    
    filepath = media_dir / filename

    tts = gTTS(text)

    tts.save(str(filepath))

    return Response({
        "audio_url": f"{settings.MEDIA_URL}{filename}"
    })


@api_view(['POST'])
def speech_to_text(request):

    audio_file = request.FILES['file']

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(audio_file) as source:

            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return Response({
            "text": text
        })

    except:

        return Response({
            "text": "Could not understand audio"
        })



@api_view(["GET"])
def get_quiz(request):

    questions = QuizQuestion.objects.all()

    if not questions.exists():

        return Response(
            {"error": "No quiz questions found"},
            status=404
        )

    question = random.choice(list(questions))

    return Response({
        "id": question.id,
        "question": question.question
    })


@api_view(["POST"])
def submit_quiz(request):

    question_id = request.data.get("id")

    user_answer = request.data.get("answer", "")

    try:

        question = QuizQuestion.objects.get(
            id=question_id
        )

        correct = (
            user_answer.strip().lower()
            ==
            question.answer.strip().lower()
        )

        return Response({
            "correct": correct,
            "answer": question.answer
        })

    except QuizQuestion.DoesNotExist:

        return Response(
            {"error": "Question not found"},
            status=404
        )