#파일 읽고 쓰기
# 파일 객체 = open(파일 이름, 파일 열기 모드)

#addData.py
f = open('C:/Users/min00/newFile.txt', 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
