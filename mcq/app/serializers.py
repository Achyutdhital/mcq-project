from . models import Categories, Questions, QuestionSets, Answer, Purchases,Slider,Score,PaymentPatner
from rest_framework import serializers


domain = "http://192.168.18.11:8000"


# Slider Serializer Class
class SliderSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Slider
        fields =['image','order_number']

    def get_image_url(self, obj):
        return f'{domain}{obj.image.url}'


# categorie serializer 
class CategoriesSerailizers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Categories
        fields =['id','categories_name','image','order_number','previous_price','current_price','short_descriptions','categories_slug']

    def get_image_url(self, obj):
        return f'{domain}{obj.image.url}'
    

#question set Serializer
class QuestionSetSerializers(serializers.ModelSerializer):
    categorie = CategoriesSerailizers(many=True, read_only=True, source='question_sets')

    class Meta:
        model = QuestionSets
        fields = ['id','categorie', 'set_name', 'is_free', 'questions_set_slug']



#Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields =['answer','correct']

#question sets related question and answer 
class QuestionSerializer(serializers.ModelSerializer):
    set_name = serializers.StringRelatedField(read_only=True)
    option1 = serializers.SerializerMethodField()
    option2 = serializers.SerializerMethodField()
    option3 = serializers.SerializerMethodField()
    option4 = serializers.SerializerMethodField()
    correct_option = serializers.SerializerMethodField()

    def get_option1(self, obj):
        answers = obj.answers.all()
        return answers[0].answer if answers else None

    def get_option2(self, obj):
        answers = obj.answers.all()
        return answers[1].answer if len(answers) > 1 else None

    def get_option3(self, obj):
        answers = obj.answers.all()
        return answers[2].answer if len(answers) > 2 else None

    def get_option4(self, obj):
        answers = obj.answers.all()
        return answers[3].answer if len(answers) > 3 else None


    def get_correct_option(self, obj):
        correct_answer = obj.answers.filter(correct=True).first()
        if correct_answer:
            options = [self.get_option1(obj), self.get_option2(obj), self.get_option3(obj), self.get_option4(obj)]
            for index, option in enumerate(options, start=1):
                if option == correct_answer.answer:
                    return f'option{index}'
        return None
    
    class Meta:
        model = Questions
        fields = ['id','set_name', 'question', 'option1', 'option2', 'option3', 'option4','correct_option']



    # class Meta:
    #     model = Questions
    #     fields = ['set_name', 'question', 'answers']


# question set purchase serializers
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields =['sets','payment_method','payment_slip','paid_amount']



# Score Serializer
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields =['marks']


class PaymentPatnerSerailizer(serializers.ModelSerializer):
    qr_code = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model  = PaymentPatner
        fields = '__all__'

    def get_image_url(self, obj):
        return f'{domain}{obj.qr_code.url}'