-- 검색 
-- select * from employees;

-- 테이블 생성
-- no, name, kor, eng, math, total, avg, rank
create table students (
no number(4), 
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);

insert into students (no,name,kor,eng,math,total,avg,rank) values(
    1, '홍길동',100,100,99,299,(299/3),1
);
insert into students (no,name,kor,eng,math,total,avg,rank) values(
    2, '유관순',100,90,99,289,(289/3),2
);

-- 완전저장
commit;

select * from students;

-- 뒤로가기
rollback;

select * from students;

--  테이블 삭제
-- drop table students;

select * from employees;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

--- aaa 1111 홍길동 010-1111-1111 
-- 내용 삽입
insert into member (id,pw,name,phone) values(
'aaa', '1111','홍길동','010-1111-1111'
);

insert into member values(
'bbb','1111','유관순','010-2222-2222'
);
insert into member values(
'ccc','이순신'
);
insert into member (id,name) values(
'ccc','이순신'
);

 --- 내용 검색
select  id, phone from member
select * from employees;
select emp_name, salary from employees;
select * from employees;
select * from member;

-- 내용 수정
update member set name = '홍길자' where id = 'aaa';

-- 내용 삭제
DELETE member WHERE id= 'ccc'

-- 데이터 확정 : commit, 