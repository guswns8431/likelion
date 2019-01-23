from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dictionary={}
    space=0
    eng=0
    kor=0
    
    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    for a in text:
        if a ==' ':
            space+=1

    for count_if_eng_or_kor in text:
        if count_if_eng_or_kor >='A' and count_if_eng_or_kor <='z':
            eng+=1
        else:
            kor+=1
    return render(request,'result.html',{'full':text,'total':len(words),'dictionary':word_dictionary.items(),'space':space,'eng':eng,'kor':(kor-space)})
    