from django.shortcuts import render

# Create your views here.

def home (request) : 

    

    return render(request, 'home.html')

def result(request) :
    sentence = request.GET['sentence']

    # 띄어쓰기를 기준으로 나눠 리스트에 저장 .
    stext = sentence.split()

    # 빈 딕셔너리 생성
    words = {}

    # 리스트에 있는 단어를 for 문 돌린다.
    for word in stext:
        # 만약 딕셔너리에 있는 단어라면,
        if word in words:
            # 딕셔너리에 해당 단어(키값)의 value 값을 1 늘린다.
            words[word] += 1
        # 만약 딕셔너리에 없는 단어라면,
        else:
            # 딕셔너리에 해당 단어(키값)의 value 값을 1로 할당하여 딕셔너리에 추가해준다.
            words[word] = 1

    return render(request, 'result.html', {'fulltext': sentence, 'count':len(stext), "wordDict": words.items})