from django.shortcuts import render
from .forms import TextAreaForm


# Create your views here.

def home(request):
    form = TextAreaForm()
    return render(request, 'home.html', {'form' : form})

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.POST.get('fulltext', '') #이 코드 자체가 입력되는 원문 그 자체
    words = text.split() #공백기준으로 나눠서 리스트로 만들어짐 총 단어 수 = len(words)
    #사전형 자료형 빈 사전 = {처음 보는 단어 = 1 , 사전에 있는 단어 +=1}
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1
    return render(request, 'count.html', {'full': text, 'total':len(words), 'dictionary' : word_dictionary.items()})