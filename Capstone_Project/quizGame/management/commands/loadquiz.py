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
            db_types = []
            for answer in info['answers']:
                obj, created = Answer.objects.get_or_create(veggie_answer=answer)
                db_types.append(obj)
            food = Question()
            food.veggie_question = info['veggie_question']
            food.save()
            print(food)
        #     for type in db_types:
        #         print(type)
        #         mon.types.add(type)

        #     mon.save()