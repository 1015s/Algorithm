places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


# output
def solution(places):
    answer = []
    for place in places:
        array = set_place(place)
        person = person_position(array)
        answer.append(check_place(array, person))
    return answer

# input 가공 (2차원 배열)
def set_place(place):
    # 2차원 배열로 세팅
    array = []
    for row in place:
        array.append(list(row))
    return array

# array 돌면서 사람 배열 만들기
def person_position(array):
    person = []
    for i in range (5):
        for j in range (5):
            if array[i][j] == "P":
                person.append([i,j])
    return person

# 거리두기 체크
def check_place(array, person):
    distance = 0
    for i in range(len(person)):
        for j in range(i+1, len(person)):
            distance = manhattan_distance(person[i], person[j])
            if distance == 2:
                if check_partition(array, person[i], person[j]) == False:
                    return 0
            elif distance == 1:
                return 0
    return 1

# 두 좌표 사이에 파티션 있는지 체크
def check_partition(array, A, B):
    # 대각선
    if A[0] != B[0] and A[1] != B[1]:
        if array[A[0]][B[1]] == "X" and array[B[0]][A[1]] == "X":
            return True
        else:
            return False
    
    # 상하좌우
    else:
        if A[0] == B[0]:
            x = A[0]
            y = min(A[1], B[1]) + 1
        else:
            x = min(A[0], B[0]) + 1
            y = A[1]
        
        if array[x][y] == "X":
            return True
        else:
            return False


# 맨하탄 거리 계산
def manhattan_distance(A, B):
    distance = 0
    for i in range (len(A)):
        distance += abs(A[i]-B[i])
    return distance

print(solution(places))