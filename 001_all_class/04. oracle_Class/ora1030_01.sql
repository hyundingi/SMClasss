-- 임시로 넣는 가상 테이블 dual
select sysdate-30,sysdate,sysdate+30 from dual;

-- employees 테이블 hire_date 컬럼  
-- 날짜 형태는 + - 가능함
select hire_date -1, hire_date, hire_date+1 from employees;

-- 날짜 범위 검색 가능, 정렬  order by , asc : 순차정렬 desc : 역순정렬
select emp_name, hire_date from employees where hire_date >= '02/01/01' and hire_date <= '04/12/31'
order by hire_date desc;

select emp_name, hire_date from employees where hire_date between '02/01/01' and '04/12/31'
order by hire_date;

-- like 
select * from employees where emp_name like '____a%';
select * from employees where emp_name like '%a__';

-- 정렬
-- asc : 널 값이 가장 아래  desc : 널 값이 가장 위 
select department_id from employees order by department_id desc;
select emp_name, job_id, salary, hire_date from employees order by hire_date ;

select no, name, total from students order by total desc;
select name, kor, eng, math from students order by kor desc, eng desc;

-- 입사일이 빠른 순으로 정렬, 이름은 역순
select emp_name, hire_date from employees order by hire_date desc, emp_name desc; 

-- abs 절대값
select -10, abs(-10) as 절대값 from dual;
select kor, kor-eng, abs(kor-eng) from students;

-- floor 소수점 이하 버림
select 3.141592, floor(3.141592) from dual;

-- trunc : 버림 , 자리수 지정 가능 34.56
select 34.5678, trunc(34.5678,2) from dual;

-- ceil : 올림
select 3.14592, ceil(3.14592) from dual;

-- round 반올림 , 소수점 첫째자리에서 반올림 35
select 34.5678, round(34.5678) from dual;
-- 소수점 둘째자리에서 반올림 34.57
select 34.5678, round(34.5678, 2) from dual;
-- 양수 첫째자리에서 반올림 30
select 34.5678, round(34.5678, -1) from dual;

-- mod : 나머지
select 27/2, mod(27,2) from dual;
select 30/3, mod(30,3) from dual;

-- 사원 번호가 홀수인 사원 출력
select *  from employees where mod(employee_id,2) != 0 order by employee_id;

-- 연봉(월급*12)+월급*12*커미션 , 소수점 2자리에서 반올림 
select salary, to_char(round((salary*12+(salary*12)*nvl(commission_pct,0))*1381.86795,1),'999,999,999.0') as 최종연봉 from employees ;

-- 시퀀스 : 자동으로 번호 부여
-- 시퀀스 생성
create sequence stu_seq 
start with 1 
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;
-- 시퀀스에서 번호 생성
-- currval 현재 시퀀스 번호 보여줌 / nextval 다음 시퀀스 번호 생성
select stu_seq.currval from dual;
select stu_seq.nextval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),
id varchar2 (30),
bhit number(10),
bdate date
);

insert into board values(
1, '제목입니다.','내용입니다.','aaa',1,sysdate
);
insert into board values(
stu_seq.nextval, '제목입니다.2','내용입니다.2','aaa',1,sysdate
);

select * from board;
commit;

-- 시퀀스 생성
create sequence borad_seq 
start with 21            -- 시작 번호
increment by 1        -- 증감 숫자
minvalue 1              -- 최소값
maxvalue 9999        -- 최대값
nocycle                    -- 1~9999 이상이 되면 1부터 다시 시작 x 
nocache;                 -- 메모리에 시퀀스값을 미리 할당해서 진행할거냐

insert into board values(
borad_seq.nextval, '제목21','내용21','aaa',1,sysdate
);

update board set btitle='제목을 다시 변경' where bno = 21;

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob,    -- varchar2 의 무제한 버전(대용량 글자타입)
id varchar2(20),
bgroup number(4),   -- 답변달기 그룹핑
bstep number(4),      -- 답변달기 경우 순서 정의
bindent number(4),  -- 답변달기 들여쓰기
bhit number(10),      -- 조회수
bdate date              -- 등록일
);

insert into board values(
board_seq.nextval, '제목1', '내용1', 'aaa', board_seq.currval, 0, 0, 1, sysdate
);

select * from board;

-- students_seq.nextval 1씩 증가
-- students 테이블에 101번 데이터 홍길순 

create sequence students_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

insert into students values(
students_seq.nextval,'홍길순',99,99,90,(99+99+90),(99+99+90)/3,1,sysdate
);

select * from students;
select no, name, kor, eng,math, total, round(avg,2),rank,sdate from students;
-- 테이블에 별칭 추가
select s.*, round(avg,2) from students s;

select dept_seq.nextval from dual;

-- s_seq 시작 1 증가 1 최대값 99999
select s_seq.nextval from dual;

select emp_seq.currval from dual;




-- 타입 
-- 문자형, 숫자형, 날짜형
-- char, varchar2, bchar, nvarchar2, long, clob
-- char, varchar2 : 한글 문자 입력 시, 3byte 사용
-- varchar2(6) : 한글 2글자 입력 가능 (바이트)
-- nvarchar2(5) : 한글 5글자 입력 가능 (글자 수) - 2byte
-- number
-- date: 초까지 입력, timestamp : 밀리초까지 입력


select '홍길동' from dual;
select length('홍길동') from dual;                                             -- length : 문자 길이
select name, length(name) n from students order by n desc;  -- 이름의 길이로 역순정렬
select lengthb('홍길동') from dual;                                           -- lengthb : 문자 byte 크기

-- 합계 200점 이상, 번호 10 - 50 사이, 이름 두번째 자리에 e가 들어가 있는 학생 출력
select * from students 
where total >= 200 and no >= 10 and no <= 50 and name like '_e%';
-- 2중 쿼리
select * from (
select * from students where total >= 200
) where name like '_e%' and no >= 30;

select no, name, total, rank from students;
-- 등수함수 rank() over(기준점) 입력
-- no : 중복이 없음/ 유일키, 기본키, 프라이머리 키 (primary key)
select no, rank() over(order by total desc) ranks from students;
select no, name, total from students order by total desc;

 -- 수정: update
update students set rank = (
select ranks from (select no, rank() over(order by total desc) as ranks from students) as b where students.no = b.no ) ;

select no, rank() over (order by total desc) as ranks from students;

update students
set rank = 1
where no = 101;
update students set rank = 4 where no = 64;
update students set rank = 5 where no = 49;

rollback;

-- 사원번호가 높은 순으로 등수 생성 
select employee_id, rank() over(order by employee_id desc) ranks from employees;
create table emp2 as select * from employees;

select rank() over(order by employee_id desc) from employees;

alter table emp2 add rank number(4);

select * from emp2;

update emp2 set rank = (
select ranks from (select employee_id, rank() over(order by employee_id desc) ranks from emp2) e where emp2.employee_id = e.employee_id
);

-- 컬럼 순서 변경
-- 컬럼 숨기기
alter table emp2 modify email invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify manager_id invisible;
alter table emp2 modify commission_pct invisible;
alter table emp2 modify retire_date invisible;
alter table emp2 modify department_id invisible;
alter table emp2 modify job_id invisible;
alter table emp2 modify create_date invisible;
alter table emp2 modify update_date invisible;

-- 컬럼 나타내기
alter table emp2 modify email visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify manager_id visible;
alter table emp2 modify commission_pct visible;
alter table emp2 modify retire_date visible;
alter table emp2 modify department_id visible;
alter table emp2 modify job_id visible;
alter table emp2 modify create_date visible;
alter table emp2 modify update_date visible;

select * from emp2;

-- 컬럼 삭제
desc emp2;
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column salary;
alter table emp2 drop column commission_pct;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;

select * from departments;
select * from emp2;
alter table emp2 add department_name varchar2(80);

-- departments 의 부서명을 emp2로 가져오기
update emp2 set department_name = '배송부' where department_id = 50;
update emp2 set department_name = (select department_name from departments where emp2.department_id = departments.department_id);

create table stu as select * from students;
alter table stu drop column rank;

select * from stu;

-- total , avg 컬럼 추가
alter table stu add total number(3) ;
alter table stu add avg number(3);
alter table stu add rank number(2);

alter table stu modify sdate visible;

update stu set total = kor+eng+math;
update stu set avg = total/3;

-- 오류 
update stu s  
set rank = 
(select ranks from (select no, rank() over(order by total desc) as ranks from stu) s2 
where s.no = s2.no
);

select no, rank() over(order by total desc) as ranks from stu;
select no, total, rank() over(order by total desc) ranks from stu;

select * from stu;


delete stu where no=101;

commit;


-- 날짜 함수
-- 현재 날짜 : sysdate
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable (
no number(4),
predate date,
today date,
nextdate date
);

-- 회원 등록 1달치, 6달치, 1년치
insert into datetable values(
1, sysdate-30, sysdate, sysdate+180
);

select no, predate, today 가입일, nextdate 만료일 from datetable;
select id, name, mdate, round(sysdate-mdate) from member where sysdate >= mdate +180;

-- 입사일 ~ 현재날짜 며칠이 지났는지
select emp_name, hire_date, round(sysdate - hire_date) as i  from employees order by i desc;

-- 15일 이상이면 1달을 올림. 15일 미만이면 일을 초기화
select hire_date, round(hire_date,'month') from employees;

-- 일자 버림 > 모두 1일로 바꿔버림
select hire_date, trunc(hire_date,'month') from employees;

-- 입사일, 현재일 기준의 달수
select hire_date, sysdate, months_between(sysdate, hire_date) from employees;
-- months_between : 두 일자 가운데 지나간 달 수
select hire_date, sysdate, round(months_between(sysdate,hire_date)) as 달수, round(sysdate-hire_date) as 일수 from employees;

-- add months : 달 수 +
select hire_date, add_months(hire_date,3) from employees;

-- next_day : 다가오는 요일에 대한 날짜를 알려줌
select next_day(sysdate,'수요일') from dual;
select next_day(sysdate, '토요일') from dual;

-- last_date : 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;
select last_day(sysdate) from dual;

-- 형변환 함수
select sysdate from dual;
select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
-- 입력의 타입 : 날짜형이 되어야함
select to_char(to_date('24/01/01'), 'yyyy-mm-dd') from dual;


update member set id = 'asd', pw = '1111', name = '배현지', email = 'qo0723@naver.com'  where id='Trineman';
select * from member;
commit;






