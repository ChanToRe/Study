A = 2 #할당
print(A)

A == 2 #A가 2인지 판단

A != 2 #A가 2가 아닌지 판단

B = c(2, 3, 4, 5) #벡터 생성 -> 벡터는 하나의 열(Column)
print(B)

#####

x1 = c(1:10) #1~10까지
x1_2 = seq(from=1, to = 10, by = 1) #1부터 10까지 1씩 증가
print(x1)
x2 = seq(from=1, to=10, by=2)
y1 = rep(1, 10) #1을 10회 반복
print(y1)
y2 = rep(c(1, 10), 2)
print(y2)
y3 = rep(c(1, 10), c(2, 2)) #1 두번, 10 두번
print(y3)

#####

MATRIX_R = matrix(data = x1, nrow = 5) #data x1을 5행으로 끊어서 출력
print(MATRIX_R)
MATRIX_C = matrix(data = x1, ncol = 5) #data x1을 5열로 끊어서 출력
print(MATRIX_C)

DATA_SET = data.frame(X1 = x1, X1_2 = x1_2, X2 = x2, y = y) #변수명 = 벡터값 형태
print(head(DATA_SET, 5)) #head(data.frame, 출력되는 행의 수)

#####

length(x1) #1차원 벡터 원소의 갯수
dim(MATRIX_R) #2차원 행렬 원소의 개수 : 행, 열
dim(DATA_SET) #데이터 프레임 원소의 개수 : 행, 열

#####

A = c(1,2,3,4,5)
print(A)

for(i in A){
    print(i)
}

B = c()
for(k in seq(from = 1, to = 10, by = 1)){
    B = c(B, k)
}
print(B)

A[2] #2번쨰 값
A[1:2] #1, 2번째 값
A[-3] #3번째 값 제외
A[c(1,2,4,5)] #1, 2, 4, 5번째 값

DATA_SET[1,] # 1행 전부
DATA_SET[,1] # 1열 전부
print(DATA_SET)
print(DATA_SET[c(1, 2, 3), -2]) #1, 2, 3행만 , -2열 빼고