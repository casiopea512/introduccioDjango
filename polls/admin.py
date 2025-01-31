from django.contrib import admin
from .models import Question, Choice

# lo pone de una manera inline
# class ChoiceInline(admin.StackedInline): #deriva de stackedinline
#     model = Choice
#     extra = 1

# lo pone como tablitas
class ChoiceInline(admin.TabularInline): #deriva de TabularInline
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin): #deriva de modeladmin
    fieldsets = [  #controlas las cosas que el usuario visualice y pueda editar, para ponerlo de manera chula y bonita
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently","numero_opcions"] # para que al ver las preguntas en la tabla veas más información, puedes poner
    # atributos y también funciones que hemos hecho antes en la clase que lo que hace es uan subquery
    list_filter = ["pub_date"] # para agregar un filtro
    search_fields = ["question_text"] #para agregar un buscador

    #saber cuántas hay de questions, en vez de en el model podemos hacerlo aquí -> estas funciones relentizan cuando hay muchas entradas y no son óptimas si hay muchas entradas
    def numero_opcions(self,obj):
        #obj -> el modelo que está iterando el questionadmin
        return obj.choice_set.count()

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)