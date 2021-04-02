import json

from django.core.management.base import BaseCommand
from vegetableGame.models import Question, Answer

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('fruitveggie.json', 'r') as file:
            data = file.read()

        veggie_data = json.loads(data)
        Question.objects.all().delete()
        Answer.objects.all().delete()
        # print(veggie_data)

        for data in veggie_data:
            veggie = Question()
            veggie.veggie_question = data['veggie_question']
            veggie.save()
            # print(veggie.veggie_question)

        for data in veggie_data:
            veggieA = Answer()
            veggieA.veggie_answer = data['veggie_answer']
            veggieA.save()
            print(veggieA.veggie_answer)
