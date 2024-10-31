-- 문자형 함수
--------------------------------------------------------------------------------
select * from member;

select sysdate-1, sysdate, sysdate+1 from dual;
select hire_date, round(hire_date, 'month') from employees;
select hire_date, trunc(hire_date, 'month') from employees;
-- vip 요금제로 변경하면 다음달 1일 부터 적용
select add_months(trunc(sysdate, 'month'),1) from dual;

-- 입사일 기준 다음달 1일 부터 혜택 제공
select hire_date, add_months(trunc(hire_date, 'month'),1) from employees;

-- 입사일 기준 1년 후 날짜 출력
select hire_date, add_months(hire_date,12) from employees;
select hire_date, hire_date+365 from employees;

-- 입사일 기준 1년 후 날짜와 1년후 마지막 그달의 날짜 출력
select hire_date, hire_date+365 입사1년, last_day(hire_date+365) 입사1년의마지막 from employees;

-- 입력일 기준 1년 후 마지막 날짜가 9/30, 10/31 인 학생들을 모두 출력
select sdate, last_day(sdate+365) sdate2, last_day(add_months(sdate,12)) sdate3 from students 
where   last_day(sdate+365)  in ( '2025/9/30','2025/10/31','2024/9/30','2024/10/31')
order by sdate2;

-- extract 함수 : 년,월,일,시,분,초 구분해서 가져올 수 있는 함수
-- sysdate 년,월,일
select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimestamp 년,월,일,시,분,초
select extract(day from systimestamp) from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

-- substr 함수 : 문자에서 시작위치, 가져올 개수
select sysdate, substr(sysdate,4,2) from dual;
select sdate, last_day(sdate+365) sdate2 from students where substr(last_day(sdate+365),4,2) in (8,11,12) order by sdate2;

-- 날짜 > 문자 : to_char      ## 날짜 포맷
-- 문자 > 날짜 : to_date      ## 날짜, 사칙연산
-- 숫자 > 문자 : to_char      ## 천단위 기호, 숫자 앞에 0표시 , 통화 표시
-- 문자 > 숫자 : to_number ## 천단위 기호 > 삭제 후 숫자형으로 변환해 사칙연산

-- 날짜 형변환해서 날짜 포맷 변경
-- date 타입 > char 타입으로 변경해서 포맷
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh24:mi:ss day') from dual;
select sysdate, to_char(sysdate, 'yy-mm-dd hh24:mi:ss dy') from dual;
select sysdate, to_char(sysdate, 'yy-Mon-dd am hh:mi:ss dy') from dual;

select hire_date, to_char(hire_date, 'yyyy-mm-dd hh:mi:ss') from employees;

-- students >  sdate 2024/01/01
select sdate, to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor = 70;
select kor, to_char(kor*1000000) from students;

-- 숫자타입 > 문자타입 변경해서 포맷 천단위 표시
-- 0 : 자릿수가 맞지 않을 경우 0으로 채움
-- 9 : 자릿수가 맞지 않을 경우 빈공백으로 채움
select salary*1382.86*12 from employees;
select to_char(salary*1382.86*12, '000,000,000,000') from employees;
-- L : 국가통화기호 표시 / $ : $ 표시
select to_char(salary*1382.86*12, 'L000,999,999') from employees;

select to_char(12,'000') from dual;
select 12 from dual;
select to_char(1,'999') from dual;

create table chartable2(
no number(4),
kor number(10),
ko_char number(10),
kor_mark number(10)
);

insert into chartable values(
1, 10000, to_char(10000,'00000000'), to_char(10000,'0,000,000')
);

insert into chartable values(
1, 10000, 100000, 010000
);

-- 숫자형 타입은 숫자 앞에 0이 있어도 표시가 되지 않음 : 문자형 타입에만 가능
-- 천단위 기호는 숫자형 타입에 입력할 수 없음 : 문자형 타입에만 가능
insert into chartable2 values(
3,30000000,30000000,30000000
);

select * from chartable;
select * from chartable2;
commit;

-- 숫자형 타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형 타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능. ( 천단위 표시 기호는 문자형 타입)
-- 숫자형 타입 + 문자 (숫자형) 타입 = 두타입 결과값 출력됨

select kor+ko_char from chartable;
select kor+kor_mark from chartable;

desc chartable; -- number, varchar2
desc chartable2; -- 모두 number

insert into chartable values(
1,10000,0000,10000
);

select * from chartable;

-- 2일 이후의 날짜를 출력하시오
select '20241031' , to_date('2024-10-31')+2, sysdate+2 from dual;

select to_char(to_date('20231031'),'yyyy-mm-dd') from dual;
-- number 형 타입 >  날짜형 타입으로 변경 
-- 문자형 타입 > 날짜형 타입
select sysdate - to_date(20231031) from dual;
select sysdate - to_date('20231031') from dual;


-- 문자형 타입 > 숫자형 타입
-- 천단위 문자형 타입 > 천단위 제외 숫자형 타입
select to_number('20,000', '999,999') from dual;
select * from chartable;

select kor, number(to_char(kor_mark, '999,999')) from chartable;
delete chartable;

insert into chartable values(
2, 30000, '0020000','2,000,000'
);
-- 문자형 천단위 타입 > 숫자형 타입으로 변환 후 사칙연산 가능
select kor+to_number(kor_mark, '999,999,999') from chartable;

select department_id from employees;
select department_id from employees where department_id is null;
select commission_pct from employees where commission_pct is null;
select commission_pct from employees where commission_pct is not null;

-- 월급 * 커미션을 계산하시오
select salary + salary * nvl(commission_pct,0) from employees;
-- null인 경우 : CEO 표시
select nvl(to_char(department_id), 'CEO') from employees;

-- 그룹함수 
-- sum : 합계 / avg : 평균 / count : 개수 / min : 최소값 / max : 최대값
select salary from employees;

-- 천단위 구분 기호 삽입, salary 합계 sum
select to_char(sum(salary),'999,999') from employees;

-- 소수점 2자리 반올림, salary 평균 avg
select round(avg(salary),2) from employees;

-- 최대값 max / 최소값 min
select max(salary), min(salary) from employees;

------ 평균값 보다 월급이 높은 사원 출력
select count(salary) from employees where salary > = 6461.83;
select count(salary) from employees where salary > = (select avg(salary) from employees);

-- emp_name : 단일함수 / avg : 그룹함수 || 단일함수와 그룹함수는 같이 쓸 수 없음
select emp_name, avg(salary) from employees;

-- students 테이블 모든 학생의 kor 점수 합계와 평균 최대값 최소값 구하기
select sum(kor), avg(kor), max(kor), min(kor) from students;

-- 부서 번호가 50 사원들의 월급의 합 평균 최대값 최소값 출력
select sum(salary), avg(salary), max(salary), min(salary) from employees where department_id = 50;

-- group by 단일함수 : 단일 함수를 그룹 함수와 함께 출력하고 싶을 때 사용 
select department_id, max(salary) from employees group by department_id;
select department_id, round(avg(salary)) from employees group by department_id order by department_id;

-- 평균 월급보다 높은 사람 수를 출력하시오
select count(salary), max(salary), min(salary) from employees where salary > = (select avg(salary) from employees); 

-- 수학함수
-- abs: 절대값 /  ceil: 올림 / floor: 버림 / round: 반올림 / trunc: 절사 / mod: 나머지 / power: 제곱 / sqrt: 제곱근
-- 제곱
select power(2,3),2*2*2 from dual;

-- 문자, 숫자형 타입 > 날짜형 타입 변경 가능
-- 숫자, 날짜형 타입 > 문자형 타입 변경 가능
-- 문자, 숫자형 타입 > 숫자형 타입 변경 가능
-- 날짜형 타입 > 숫자형 타입 변경 불가 x
----날짜형 > 문자형 > 숫자형 가능
select '2', to_number('2') from dual;
select '20240101', to_number('20240101') from dual;
-- select 20240101, to_date(20240101), to_number(to_date(20240101)) from dual;
select sysdate, to_number(to_char(sysdate, 'yyyymmdd')) from dual;
-- select sysdate, to_number(sysdate) from dual;
select to_char(sysdate, 'yyyy"년"mm"월"dd"일"') from dual;


-- 숫자형 타입은 사칙연산을 하면 계산해서 출력됨
--- 문자형 함수 : 더하기 기호를 사용해 합치려고 하면 에러
select emp_name + email from employees;

-- || , concat 함수 사용 해야 합칠 수 있음
select emp_name||email from employees;
select concat(emp_name, email) from employees;

select name from member;

-- lower : 소문자 / upper : 대문자 / initcap : 첫글자 대문자 
select * from member where lower(name) = 'bryan';
select 'joHn', initcap('joHn'), lower('joHn'), upper('joHn') from dual;

-- lpad : 왼쪽 자리수 만들어줌
select 'john', lpad('john',10,'#') from dual;

-- rpad : 오른쪽 자리수 만들어줌
select 'john', rpad('john',10,'#') from dual;

--- trim : 빈공백 없애기 / ltrim : 왼쪽공백 / rtrim : 오른쪽 공백
select length('           a          '), length(trim('           a          ')) from dual;
select replace('  a  a  a   ',' ',''), trim('  a  a  a   ') from dual; 
-- 안에 있는 공백 지우기 replace


-- substr : 특정 위치 자르기 (시작위치, 개수)
select 'abcdefg', substr('abcdefg',1,3), substr('abcdefg',3,5) from dual;

select hire_date, substr(hire_date,4,2) from employees;
-- 입사일이 3월인 사우너 출력
select emp_name, hire_date from employees where substr(hire_date,4,2) = '03';

-- translate 치환 : x > a , y > b / replace 치환 xy > ab
select 'axyz', translate('axyxyfdgxtyz','xy','ab') from dual; -- aababfdgatbz
select 'axyz', translate('axyxyfdgxtyz','xyf','ab') from dual; -- aababdgatbz
select 'axyz', replace('axyxyfdgxtyz','xy','ab') from dual; -- aababfdgxtyz

-- length() : 문자열 길이
-- students 테이블 name 글자 길이가 5자 이상인 학생만 출력
select name from students where length(name) > = 5;

-- 사원의 월급의 합, 평균
select sum(salary) 합계, round(avg(salary),2) 평균 from employees;
-- 영어점수의 합 평균 최대값 최소값
select sum(eng), round(avg(eng),2), max(eng), min(eng) from students;
-- students 테이블에서[ 홍길동, 등록일 : 2023년 12월 02일 ]출력
select '홍길동, 등록일 : '||to_char(sdate, 'yyyy"년" mm"월" dd"일"') from students where name in ('홍길동','유관순');


