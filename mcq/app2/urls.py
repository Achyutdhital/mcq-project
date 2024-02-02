from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from .views import GetQuestionSetsView


app_name ='dashboard'
urlpatterns = [
        path('',views.index,name='index'),
        path('login/', views.login, name='login'),
        path('logout', views.userlogout, name='logout'),
        # path('question/<int:id>/',views.question,name='question'),
        # path('question-set/<str:question_set_slug>/', views.question_set_detail, name='question_set_detail'),
        path('question/<int:id>/', views.question, name='question'),
        path('question/delete', views.question_delete, name="question_delete"),
        path('subcategories', views.load_sub_category, name="ajax_load_courses"),

        path('slider/',views.slider,name='slider'),
        path('deleteSlider/<int:id>/',views.deleteSlider,name='deleteSlider'),

        path('add_Slider',views.add_edit_Slider,name='add_Slider'),
        path('edit_Slider/<int:id>/',views.add_edit_Slider,name='edit_Slider'),
        
        
        path('categorie',views.categorie,name='categorie'),
        path('category/<slug:slug>', views.category_related_sets, name='related_question_sets'),
        path('deleteCategories/<int:id>/',views.deleteCategories,name='deleteCategories'),

        path('add_Categories',views.add_edit_Categories,name='add_Categories'),
        path('edit_Categories/<int:id>/',views.add_edit_Categories,name='edit_Categories'),
        
        path('questionSets',views.questionSets,name='questionSets'),
        path('questionset/delete/<int:id>',views.deletequestionSets, name='delete_question_set'),
        path('deletequestionSets/<int:id>/',views.deletequestionSets,name='deletequestionSets'),

        path('add_QuestionSets',views.add_edit_QuestionSets,name='add_QuestionSets'),
        path('edit_QuestionSets/<int:id>/',views.add_edit_QuestionSets,name='edit_QuestionSets'),
        
        
        path('purchase_list/', views.purchase_list, name='purchases'),
        path('update_purchase_list/<int:id>/', views.update_purchase_list, name='update_purchase_list'),
        path('deletepurchases/<int:id>/',views.deletepurchases,name='deletepurchases'),

        path('add_question', views.add_question, name='add_question'),
        path('add_question/<int:setid>', views.add_question, name='addquestion'),
        path('add_question/update/<int:question_id>', views.add_question, name='update_question'),

        path('get_question_sets/', GetQuestionSetsView.as_view(), name='get_question_sets'),

        path('change_password/', views.change_password, name='change_password'),
        path('questions/', views.question, name='questions'),

        #testing
        path('test',views.add_question, name='test'),
        path('user/', views.user, name='user'),
        

        #question ajax
        path('get_question',views.get_question_details, name='get_question_details')


]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)