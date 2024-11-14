--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
    no number(4),
    id varchar2(20),
    pw varchar2(20),
    name varchar2(20),
    phone varchar2(20),
    mdate date
);

-- insert 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
1, 'aaa', '1111', '홍길동', '010-1111-1111', '2024-10-29'
);
insert into member values(
2, 'bbb', '1111', '유관순', '010-1111-1111', '2024-10-29'
);


select * from member;

commit;
rollback;

-- delete 삭제
delete member where no=1;
delete member;

-- update 수정
update member set name='홍길자' where no = 1;
update member set name ='김구';

-- create 테이블 생성
create table students (
stuno number(4),
name varchar(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

- sysdate : 현재 날짜 시간 저장
insert into students values(
1, '홍길동', 100,100,100+100,sysdate
);

commit;

select * from students;
-- 특정컬럼을 입력하면 컬럼만 검색
select name, sdate from students;

-- 일부 컬럼만 지정하여 삽입 가능
insert into students (stuno,name) values (
2, '유관순'
);

-------------------------------
-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2;

-- 테이블 구조
desc employees;

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재할 경우 데이터만 복사할 ㄸ ㅐ
create table member2 as select * from member where 1=2;
insert into member2 select * from member;

-- 컬럼데이터 타입, 길이 변경
-- alter 변경 : member 테이블의 no컬럽의 타입 길이를 변경
alter table member modify no number(10);
-- alter 변경 : member 테이블의 컬럼 이름 변경 ( 컬럼명 : 대소문자 구분 x ) / 안에 들어가있는 데이터만 대소문자 구분함
alter table member rename column no to memberNo;

update member set no='';
select * from member;
alter table member modify no varchar2(10);

select * from member;
desc member;


-- employees 테이블에서 사원번호 , 사원 이름, 입사일 출력 
select * from employees;
select employee_id, emp_name, hire_date from employees;

-- 연산자 : 산술 연산자 , +, -, *, /
--drop table member;
--drop table member2;
--drop table emp2;
--drop table emp3;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

commit;

select kor, eng, (kor+eng) from studets;
select kor,eng,(kor+eng), abs(kor-eng) from students;
--  문자 더하기 안 딤
select emp_name+email from employees;

-- concat 명령어, ||
select cincat (employee_id, eml_name) from employees;
select employee_id || emp_name from employees;

-- 달러환산
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name, salary, salary*1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values ( 1, '홍길동', 100);
insert tnto stu values (2,'유관순', 99);

commit;

insert into values(3,'',0);
insert into stu values (4, null, null);
-- 널 값 검색
select * from stu where name is null;

-- 널이 아닌 것 출력
select * from employees;
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 연봉계산
select salary, salary*12 from employees;
select salary, salary*12, salary*1384 from employees;

-- 커미션이 없는 사원은 null 값이 있는데 연산을 써서 null값으로 변경
select salary, salary*12, salary*12 + (salary*12)*nvl(commission_pct,0)*0.01 from employees;

-- 컬럼명 별칭 사용 as , '' 특수문자, 사이공간까지 컬럼명으로 사용 가능
select salary, salary*12, salary*12  as  연봉+ (salary*12)*nvl(commission_pct,0)*0.01 as real_yearSalary from employees;


-- nvl() 함수, nvl( kor,0) : kor 칼럼에 null 값이 있으면 0으로 표시
select * from stu;
select no, name kor, kor+100 from stu;
select no, name, kor, nvl(kor, 0) +100 from stu;


-- kor 국어, 영어, 수학, 합께 컬럼명 별칭을 이용해 출력 >> as 는 넣어도 되고 안 넣어도 됨
select * from students;
select no as 번호, name as 이름, kor 국어, eng as 영어, math as 수학, total as 합계 from students;

-- 사원번호 이름 이메일 합쳐서 출력
-- concat 는 2개만 하나로 합칠 수 잇음.
select * from employees;
select employee_id || emp_name || email from employees;
select concat(concat (employee_id, emp_name), email) from employees; 
select emp_name || ' is a ' || job_id from employees;

-- 중복제거 distinct
select department_id from employees;
select distinct department_id from employees;
-- 정렬 : order by  - asc 순차 정렬 : 생략가능, desc - 역순정렬
select distinct department_id from employees order by department_id desc;

job_id 중복제거 후 출력
select distinct job_id from employees;
select job_id from employees;

-- 문자열 자르기 0,1,2앞 까지 출력
select substr(job_id,0,2) from employees;

-- 4번째 컬럼데이터를 가져와서 중복을 제거함
select distinct substr (job_id,4) from employees;

-- where 절 : 조건 비교 연산자 >, >=, <, <=, =, !=
select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id > 100;

-- students 합계 250이상 출력 / 정렬
select * from students where total >= 250 order by total;

-- 합계 250 kor 90 이상
select * from students where total >=250 and kor>=90;

-- 영어 점수 70이상 90 이하 
select * from students where eng >= 70 and eng <= 90;

-- employees 월급이 5000이상 8000이하
select * from employees where salary > = 5000 and salary <= 8000;

-- 월급이 7000이 아닌 것
select * from employees where salary != 7000;

-- 50번이 아닌 것의 개수
select count(department_id) from employees;                      -- 106개
select count(*) from employees where department_id is null; -- 1개
select count(*) from employees where department_id = 50; -- 45개
select count(*) from employees where department_id !=50; -- 61개 ( 널값은 카운트하지 않음) 

-- 급여 4000이하 사원번호 사원명 급여 출력
select employee_id, emp_name, salary from employees where salary <= 4000;
select employee_id as 사원번호, emp_name as 사원명, salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교 연산자 가능
select emp_name, hire_date from employees;
select emp_name, hire_date from employees where hire_date >= '2002/01/01';

-- 191231 이전에 입사한 사람
select emp_name, hire_date from employees where hire_date <= '1999/12/31';

-- 010101 ~ 041231
select emp_name, hire_date from employees where hire_date <= '2004/12/31' and hire_date >= '2001/01/01';

-- 논리연산자
-- 국어점수가 90점 이상 또는 영어점수가 50점 이상을 출력하시오. students 테이블

select count(*) from students where kor >= 90 or eng >=90; 

-- 부서번호가 80번이면서 job_id - man
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';

select commission_pct from employees where commission_pct is not null;
-- 커미션이 0.2,0.3,0.5 출력
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);  

-- 사원번호 110,120,130 출력
select employee_id from employees where employee_id in (110,120,130);
select employee_id from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;

-- 150-170 사원번호 출력
select * from employees where employee_id >= 150 and employee_id <=170;
-- between <= >= 만 가능 
select * from employees where employee_id between 150 and 170;

-- 020607 - 040217
select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');
-- 날짜 비트윈
select hire_date from employees where hire_date between '2002/06/07' and '2004/02/17';

-- job man 출력
select * from employees where substr(job_id,4) = 'MAN';

-- like 연산자 : 포함되어 있는 글자 검색
-- man으로 끝나는 단어를 검색
select * from employees where job_id like '%MAN';
-- st 로 시작하는 단어를 검색
select * from employees where job_id like 'ST%';

-- 소문자 a가 들어가 잇는 이름 검색
select * from employees where emp_name like '%a%';

-- 2번째 자리에 t가 들어가 있느 이름 출력
select * from employees where emp_name like '_t%';

-- 4번째 자리에 v 가 들어가 있는 이름 출력
select * from employees where emp_name like '___v%';

-- 뒤에서 2번째 자리에 l이 들어가 있는 이름 출력
select * from employees where emp_name like '%l_';

-- 첫번째 D 가 들어가 있는 이름 출력
select * from employees where emp_name like 'D%';

