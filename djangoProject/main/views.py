from django.shortcuts import redirect, render
## Model 추가
from .models import Board

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def board(request):

    # DB에서 Board 데이터 조회
    boardList = Board.objects.all()

    # 페이지에 데이터를 던져주어 페이지에서 boardList 데이터를 받을 수 있다.
    return render(request, 'main/board/board.html', {'boardList':boardList})

## 데이터 등록
def new_board(request):

    ## request method가 POST이면 아래 로직 수행
    if request.method == 'POST':
        Board.objects.create(
            ttl=request.POST['ttl'],
            contents=request.POST['contents'],
            writer=request.POST['writer']
        )
        ## 등록이 성공하면 목록 페이지로 이동
        return redirect('/board/')

    ## POST 요청이 아니면 등록 화면으로 이동
    return render(request, 'main/board/new_board.html')

def edit_board(request, pk):

    data = Board.objects.get(
            pk=pk
        )

    if request.method == 'POST':
        
        data.ttl = request.POST['ttl']
        data.contents = request.POST['contents']
        data.writer = request.POST['writer']
        data.save()

        return redirect('/board/')

    ## POST 요청이 아니면 수정 화면으로 이동
    return render(request, 'main/board/edit_board.html', {'board': data})

def del_board(request, pk):

    ## pk로 데이터를 조회한 후
    data = Board.objects.get(
            pk=pk
        )

    ## 데이터 삭제
    data.delete()

    ## 다시 목록 페이지로 이동
    return redirect('/board/')