import os
import django
from django.utils import timezone
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoMidtermProject.settings')
django.setup()

from polls.models import Question, Choice

def create_polls():
    # Sample questions and choices in Turkish
    polls_data = [
        {
            "question": "En sevdiğiniz programlama dili nedir?",
            "choices": ["Python", "JavaScript", "Java", "C++"]
        },
        {
            "question": "Hangi mevsimi tercih edersiniz?",
            "choices": ["İlkbahar", "Yaz", "Sonbahar", "Kış"]
        },
        {
            "question": "En sevdiğiniz kahve türü nedir?",
            "choices": ["Türk Kahvesi", "Espresso", "Latte", "Americano"]
        },
        {
            "question": "Hangi renk sizin için şans rengidir?",
            "choices": ["Kırmızı", "Mavi", "Yeşil", "Sarı"]
        },
        {
            "question": "En sevdiğiniz yemek türü nedir?",
            "choices": ["İtalyan", "Türk", "Çin", "Hint"]
        },
        {
            "question": "Hangi sosyal medya platformunu en çok kullanırsınız?",
            "choices": ["Instagram", "Twitter/X", "Facebook", "TikTok"]
        }
    ]

    for poll in polls_data:
        # Create question
        question = Question.objects.create(
            question_text=poll["question"],
            pub_date=timezone.now()
        )

        # Create choices
        for choice_text in poll["choices"]:
            Choice.objects.create(
                question=question,
                choice_text=choice_text,
                votes=random.randint(0, 10)  # Random votes for demo
            )

        print(f"Created poll: {poll['question']}")

if __name__ == "__main__":
    create_polls()
    print("Polls created successfully!")