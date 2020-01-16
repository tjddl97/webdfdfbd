from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')
    
def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for i in word_list:
        if i in word_dictionary:
            word_dictionary[i] +=1
        else:
            word_dictionary[i] = 1
    return render(request, 'result.html',{'fulltxt': full_text, 'total':len(word_list), 'dictionary': word_dictionary.items()})