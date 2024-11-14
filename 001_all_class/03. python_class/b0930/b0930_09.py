stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
  [1, '홍길동', 100, 100, 100, 99],
  [2, '유관순', 100, 100, 100, 99],
  [3, '이순신', 100, 99, 98, 99],
  [4, '김구', 80, 100, 90, 99],
  [5, '김유신', 80, 100, 90, 99],
  ]

#append 사용하여 합계, 평균값 추가하여 출력

print('               [학생성적프로그램]')
for s_t in stu_title:
  print("{}".format(s_t), end = '\t')
print() # 줄바꿈
print('-'*60)

for s in stu_datas:
  # stu_total = s[2]+s[3]+s[4]+s[5] 
  # stu_avg = round(stu_total/4,2)
  # s.append(stu_total)
  # s.append(stu_avg)
  # s.append(s[2]+s[3]+s[4]+s[5])
  s.append(sum(s[2:6]))
  s.append(round((s[2]+s[3]+s[4]+s[5])/4,2))
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))

