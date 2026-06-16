from django.contrib import admin
from .models import *

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("name", "time", "trigger")


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ("command_text", "activity")


@admin.register(LanguageGuide)
class LanguageGuideAdmin(admin.ModelAdmin):
    list_display = ("letter", "code_word")


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("question",)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("username", "score")