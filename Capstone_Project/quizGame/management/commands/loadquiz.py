import json

from django.core.management.base import BaseCommand
from quizGame.models import Question, Answer


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fruitveggie.json', 'r') as file:
            data = file.read()

        veggie_data = json.loads(data)
        Question.objects.all().delete()
        Answer.objects.all().delete()
        # print(veggie_data)

        for info in veggie_data:
            food = Question()
            food.veggie_question = info['veggie_question']
            food.save()
            for choice in info['answers']:
                answer = Answer()
                answer.question = food
                answer.veggie_answer = choice
                if choice == info['veggie_answer']:
                    answer.correct = True

                answer.save()

            print(food)