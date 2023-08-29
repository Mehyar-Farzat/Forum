from django.shortcuts import render
from .models import Questions , Answer
from .forms import  Questionform

# # Create your views here.




def questions_list(request):
    data = Questions.objects.all()
    print(data)
    return render(request,'all_questions.html', {'questions' : data})




def questions_detail(request,question_id):
    data = Questions.objects.get(id=question_id)
    answer_data= Answer.objects.all()
    return render(request,'question_detail.html', {'questions':data , 'answer' : answer_data})




def add_question(request):
    if request.method == 'Questions':
        form = Qeustionform(request.Questions, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/questions/')


    else:
        form = Questionform()
    return render(request, 'add.html' , {'form' : form})




def edit_question(request, question_id):
    data = Questions.objects.get(id=question_id)
    if request.method == 'Questions':
        form = Postform(request.Question, request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect(f'/questions/{data.id}')

    else:
        form = Questionform(instance=data)
    return render(request, 'edit.html' , {'form' : form})








