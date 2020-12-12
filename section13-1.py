# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 겜임 제작 및 기본 완성

import random
import time


words = [] #영어단어리스트(1000개로드)
n= 1 #게임 시도 횟수
cor_cnt = 0 #정답개수

with open('./resource/word.txt','r') as f:
    for c in f:        
        words.append(c.strip())#strip()양쪽 공백제거

#print(words) #단어 리스트 확인

input("Ready?  Press Enter Key!") #Enter Game Start!

start = time.time()
while n<=5:
    random.shuffle(words)
    q=random.choice(words)

    print()
    print("*Question # {}".format(n))
    print(q) #문제를 출력

    x= input()  #타이핑 입력
    print()

    if str(q).strip()==str(x).strip() : #입력확인(공백제거)
        print("Pass!")
        cor_cnt+=1
    else:
        print("Wrong!")         

    n+=1#다음문제 전환

end = time.time()#End Time
print(end)
et= end-start #총게임시간

et = format(et,".3f")#소수 셋째자리 출력(시간)

#수행시간 출력
print("게임시간 : ",et,"초","정답개수 : {}".format(cor_cnt))

#시작지점
if __name__ == '___main__':
    pass