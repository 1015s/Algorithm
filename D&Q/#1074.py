# 분할 정복
# 다 저장하면 메모리 초과 -> 내가 원하는 값이 있는 상자만 찾아야 됨

# r행 c열
N, r, c = map(int, input().split())

line = pow(2, N)

def find_box(row, col, n, first):
    new = n // 2
    
    if n > 2:
        # 4등분
        if row < new :
            if col < new :
                # 1번 박스
                first_num = first + pow(new, 2) * 0
            else:
                # 2번 박스
                first_num = first + pow(new, 2) * 1
                col = col - new
        else:
            if col < new :
                # 3번 박스
                first_num = first + pow(new, 2) * 2
                row = row - new
            else:
                # 4번 박스
                first_num = first + pow(new, 2) * 3
                row = row - new
                col = col - new
        find_box(row, col, new, first_num)
    else:
        # 2의 배수 -> 앞 줄, 2의 배수가 아니면 -> 뒷 줄
        if row % 2 == 0:
            if col % 2 == 0:
                print(first)
            else:
                print(first + 1)
        else:
            if col % 2 == 0:
                print(first + 2)
            else:
                print(first + 3)
                
            
find_box(r, c, line, 0)
        