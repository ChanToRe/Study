Numeric_Vector = c(1:20) #1~20
Chr_Vector = c("A", "B", "C")
str(Numeric_Vector) #str : 데이터 타입 확인
str(Chr_Vector)
print(Numeric_Vector)

##### 시간, 날짜

DATE_0 = "2018-01-02" #chr
str(DATE_0)

DATE_C = as.Date(DATE_0, format = "%Y-%m-%d") #as.Date : 포맷을 맞춰줘야함
str(DATE_C)


DATE_02 = "2015-02-04 23:13:23"
DATE_P = as.POSIXct(DATE_02, format = "%Y-%d-%d %H:%M:%S")
str(DATE_P)

format(DATE_P, "%A") #날짜 정보를 뽑아 새로운 변수 생성 가능

##### as문 과 is문
#as : 변수 x를 ~로 취급하겠다 선언
x = c(1:10)

x1 = as.integer(x) #int
x2 = as.numeric(x) #num
x3 = as.factor(x) #Factor
x4 = as.character(x) #chr

str(x1)
summary(x1)
str(x2)
summary(x2)
str(x3)
str(x4)
summary(x4)
#is : 변수 x가 ~인지 판단하라
x = c(1:10)
y = c("str", 'str2', "str3", "str4")
is.integer(x)
is.factor(y)