from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import  login,authenticate,logout
from .models import Question , User_Registry
from first_page.form import Login_Page
from first_page import models
def quiz_view(request,category):
    questions = Question.objects.filter(category=category).prefetch_related('choice')

    if request.method == 'POST':
        score = 0
        results = []
        for question in questions:
            
            selected = request.POST.get(f'question_{question.id}')
            if selected!=None:
                correct = question.choice.first().choice_text[ord(question.choice.first().answer)-69] # Assuming one Choice per Question
                selected=selected.replace('\n','').strip()
                correct=correct.replace('\n','')
                is_correct = selected == correct
                results.append((question.question_text, selected, correct, is_correct))
                if is_correct:
                    score += 1

        data=User_Registry.objects.get_or_create(Name=request.user.id)[0]
        scores=models.Score_Board.objects.create(User_Registry=data,Name=category,Score=score)
        scores.save()

        return render(request, 'result.html', {'score': score, 'results': results, 'total': questions.count()})
    return render(request, 'quiz.html', {'questions': questions})

def select_Category(request):
    categories = ['Python', 'Java','SQL']
    selected = None
    if request.method == 'POST':
        selected = request.POST.get('category')
        return redirect('first_page:Quiz', category=selected)  
    return render(request, 'select_category.html', {'categories': categories})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            User_Registry.objects.create(Name=user)
            login(request, user)
            # return HttpResponse(f'<h1>Welcome {user.username}</h1>')
            return redirect('first_page:welcome')  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def welcome_page(request):
    if request.user.is_authenticated and request.user.username:
        data=User_Registry.objects.get_or_create(Name=request.user.id)
        score= models.Score_Board.objects.filter(User_Registry=data[0].id)
        return render(request,'welcome.html',{'scores':score})
    else:
        return redirect('logout')
    # return HttpResponse(f'<h1>Welcome{request.user.username}</h1>')


def login_view(request):
    if request.method =='POST':
        form=Login_Page(request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=user,password=password)
            if user!=None:
                login(request, user)
                return redirect('first_page:welcome')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form=Login_Page()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    
    logout(request)
    return redirect('login')
