from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from core.models import Dict


def index_view(request):
    return render(request, 'index.html')


@csrf_exempt
def quiz_view(request):
    # index_view에서 POST로 받아온 사용자의 이름
    username = request.POST.get('username')

    # Dict model에서 'id'와 'mean' 필드의 값들만 가져옴
    # 랜덤으로 정렬('?')한 후, 딕셔너리 타입으로 변환
    dicts = dict(Dict.objects.values_list('id', 'mean').order_by('?'))

    ctx = {
        'username': username,
        'dicts': dicts.items,
    }

    return render(request, 'quiz.html', ctx)


@csrf_exempt
def result_view(request):
    username = request.POST.get('username')

    # word와 mean을 가져옴. id는 가져오지 않고, 자동 정렬을 이용해 index로부터 추정하는 방식.
    answers = list(Dict.objects.values_list('id', 'word', 'mean'))
    result = []
    score = 0

    # POST로 받아온 각각의 input name을 반복하면서
    for word_id in request.POST.keys():
        # 진짜 model에 들어있는 id를 빼낸 후
        raw_id = int(word_id[4:])
        # answers에서 그 id에 해당하는 word를 찾고
        answers_pos = index_2d(answers, raw_id)[0]
        # id, 유저의 정답, Model의 단어, Model의 단어뜻을 갖는 리스트
        result.append((answers[answers_pos][0], request.POST[word_id], answers[answers_pos][1], answers[answers_pos][2]))
        # 채점
        if request.POST[word_id] == answers[answers_pos][1]:
            score += 1

    ctx = {
        'username': username,
        'score': score,
        'result': result,
    }
    return render(request, 'result.html', ctx)


def index_2d(list, value):
    i = 0
    j = 0

    for inner_list in list:
        for one in inner_list:
            if one == value:
                return i, j
            j += 1
        i += 1
        j = 0

    return -1, -1
