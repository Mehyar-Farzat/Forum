from django.shortcuts import render
from .models import Questions

# # Create your views here.




def questions_list(request):
    data = Questions.objects.all()
    return render(request,'all_questions.html', {'questions' : data})




# def questions_detail(request,question_id):
#     data = post.objects.get(id=question_id)
#     return render(request,'question_detail.html', {'questions':data})
