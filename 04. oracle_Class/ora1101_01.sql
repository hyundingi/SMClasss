-- 11/01 하다가 렉걸려서 날라감 . 강사쌤거 참고하길

CREATE TABLE EMP3 AS SELECT * FROM EMPLOYEES; -- TABLE COPY
CREATE TABLE EMP4 AS SELECT * FROM EMPLOYEES WHERE 1=2; -- TABLE COPY NO CONTENTS
SELECT * FROM EMP3;
SELECT * FROM EMP4;
-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
INSERT INTO EMP4 SELECT * FROM EMPLOYEES;
-- INSERT UPDATE DELETE -- COMMIT/ROLLBACK
-- 제약조건이 NULL 이 들어가면 안되는 것을 확인
INSERT INTO EMP4(EMPLOYEE_ID,EMP_NAME,HIRE_DATE,SALARY) SELECT EMPLOYEE_ID,EMP_NAME,HIRE_DATE,SALARY FROM EMPLOYEES;
------ 테이블
-- CREATE ALTER DROP
SELECT * FROM EMP4;
-- ALTER ADD ; 테이블에 컬럼 추가
ALTER TABLE EMP4 ADD(HIRE_DATE2 DATE);
DESC EMP4;
-- 컬럼변경 ; 컬럼안에 데이터가 있다면 제약조건, 65 길이의 문자가 있을 경우 50으로 변경 불가
ALTER TABLE EMP4 MODIFY(EMAIL VARCHAR2(70));
ALTER TABLE EMP4 MODIFY(EMAIL VARCHAR2(50));
SELECT EMP_NAME FROM EMP4;
SELECT MAX(LENGTH(EMP_NAME)) FROM EMP4;
SELECT LENGTH(EMP_NAME) FROM EMP4 ORDER BY LENGTH(EMP_NAME)DESC;
-- 다른 타입인 경우 데이터를 NULL 로 변경 후 타입을 변경
DESC EMP4;
-- 이메일에 EMPLOYEE_ID 값 복사
UPDATE EMP4 SET EMAIL = EMPLOYEE_ID;
-- EMPLOYEE_ID PHONE_NUMBER 입력 -- PHONE_NUMBER 문자형타입 EMPLOYEE_ID 숫자형 타입
UPDATE EMP4 SET PHONE_NUMBER = EMPLOYEE_ID;
-- 문자형타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 안됨
UPDATE EMP4 SET MANAGER_ID = PHONE_NUMBER;
UPDATE EMP4 SET PHONE_NUMBER = '198A' WHERE EMPLOYEE_ID = 198;
-- 컬럼 이름 변경
ALTER TABLE EMP4 RENAME COLUMN PHONE_NUMBER TO P_NUMBER;
-- 속성 변경
ALTER TABLE EMP4 MODIFY HIRE_DATE DATE NULL;
ALTER TABLE EMP4 MODIFY HIRE_DATE DATE NOT NULL;
-- 컬럼 삭제
ALTER TABLE EMP4 DROP COLUMN HIRE_DATE2;
-- 테이블 삭제
DROP TABLE EMP2;
DROP TABLE EMP3;
-- 테이블 이름 변경
RENAME EMP44 TO EMP4;
----
DROP TABLE BOARD;
DROP TABLE BMEMBER;
-- CHECK - MALE,FEMALE 2가지 형태 외에는 입력 안되게
-- NOT NULL - 빈공백은 가능함
SELECT * FROM BMEMBER;
-- PRIMARY KEY ; 중복불가 NULL 불가
CREATE TABLE EMP3(
EMPNO NUMBER(4) UNIQUE,
ENAME VARCHAR2(30) NOT NULL,
JOB VARCHAR2(9),
DEPTNO NUMBER(2)
);
INSERT INTO EMP3 VALUES(
1,'홍','01','01'
);
INSERT INTO EMP3 VALUES(
2,'유','02','02'
);
-- UNIQUE NULL 값은 혀용
INSERT INTO EMP3 (ENAME,JOB,DEPTNO) VALUES(
'이','03','03'
);
-- UNIQUE 중복은 불가
INSERT INTO EMP3 VALUES(
2,'강','04','04'
);
SELECT * FROM EMP3;
-- primary key 등록시 null 값이 존재하면 안됨 중복도 존재하면 안됨
-- primary key 추가, 수정
-- constraint id_pk 이름 설정
ALTER TABLE MEMBER ADD CONSTRAINT ID_PK PRIMARY KEY(ID);
SELECT * FROM MEMBER;
INSERT INTO MEMBER VALUES('fff','1111','홍길자','aaa@aaa.COM','123-456-789','Female','golf',sysdate);
alter table member drop constraint id_pk;
create table board(
bno number(4)primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

select * from board;


insert into board values (
board_seq.nextval, '제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);

insert into board values (
board_seq.nextval, '제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);

insert into board values (
board_seq.nextval, '제목5','내용5','eee',board_seq.currval ,0,0,0,sysdate,''
);

commit;

select * from bmember; --  bno, btitle, id, bcontent, bgroup, bstep, bindent, bhit, bfile
select * from board;      -- id, pw, name, nicname, age, gender, email, bdate

-- member 의 id 는 primary key / board.id = foreign key
select bno, btitle, bcontent, nicname, email, bgroup, bstep, bindent, bhit, bfile from board, bmember where board.id = bmember.id;

select employee_id, emp_name, email, salary, department_id from employees;

select department_id , department_name from departments where department_id =10;

select employees.department_id, department_name, emp_name from employees, departments 
where departments.department_id = employees.department_id;

-- 테이블 생성할 때 foreign key 생성
create table board2 (
bno number(4) primary key,
btitle varchar2 (1000) not null,
bcontent clob,
id varchar2 (30),
constraint fk_board2_id foreign key (id) references bmember (id)
);

-- foreign key 추가 변경 / bmember id(유일키) > board id(외래키로 설정 추가)
alter table board add constraint id_fk foreign key (id) references bmember(id);
-- foreign key 삭제
alter table board drop constraint id_fk;

select * from board;
-- abc 글을 등록하면 , 등록이 안 됨
insert into board values (
board_seq.nextval, '제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,''
);

delete board where bno = 6;
commit;

-- bmember 테이블 id, foreign key 로 board, board2 에 등록
-- foreign key : 외래키 / primary key : 기본키
-- [ foreign key 삭제 방법 ] ----------
-- 원본의 primary key 데이터를 지우려면 , 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨
-- foreign key를 해제해야 삭제 가능
select * from board;
select * from bmember;
delete bmember where id = 'aaa';


-------------------------------------------------------------

alter table board drop constraint id_fk;
----  primary key를 삭제할 때 foreign key 에 데이터가 있으면 삭제가 안됨
---- on delete cascade : primary key 가 삭제되면 foreign key로 등록된 모든 글을 삭제시킴
alter table board add constraint id_fk foreign key (id) references bmember (id) on delete cascade;

alter table board add constraint fk_board_id foreign key (id) references bmember (id) set update cascade;

-- 외래키 삭제
-- on delete restricted 
---- 1. 기본값 : 입력하지 않을 시, 자식데이터가 있을 경우, 부모데이터가 삭제되지 않음 
alter table board add constraint id_fk foreign key (id) references bmember (id);
-- 자식 테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
delete bmember where id = 'aaa';
delete board where bno = 3;

-- on delete cascade
-- 2. 부모데이터 삭제 시 , 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key (id) references bmember (id) on delete cascade;
-- 부모 데이터를 삭제하면, 자식데이터의 모든 글이 삭제 됨
delete bmember where id = 'aaa';

-- on delete set null
-- 3. 부모데이터 삭제 시, 자식 데이터에 해당되는 값이 null 로 표시
alter table board add constraint id_fk foreign key (id) references bmember (id) on delete set null;
-- 부모데이터를 삭제하면 자식데이터의 해당 컬럼만 null 변경되고, 데이터는 그대로 존재
delete bmember where id = 'aaa';







-- check 구문
create table emp01 (
empno number (4) primary key,
ename varchar2 (30) not null,
salary number (7,2) check (salary between 2000 and 20000),
gender varchar2 (10) check (gender in ('Male','Female'))
);

-- check 가 지정되어 있는 컬럼 에 추가
-- salary 범위를 벗어나면 에러, Male, Female 이외의 단어 입력시 에러
insert into emp01 values (
1, '홍길동', 2500, 'Male'
);
insert into emp01 values (
2, '유관순', 20000, 'Female'
);
insert into emp01 values (
3, '이순신', 20000, 'male'
);

-- default : insert  시 값이 입력이 되지 않을 시, 문자, 숫자, 날짜를 넣ㅇ르 수 있음
create table emp02 (
empno number (4) primary key,
ename varchar2 (30) default '무명',
income number (4) default 0,
salary number (7,2) check (salary between 2000 and 20000),
gender varchar2 (10) check (gender in ('Male','Female')),
edate date default sysdate
);

-- 
insert into emp02 (empno, salary, gender) values(
1,5000,'Male'
);

select * from emp02;

-- commit;

--drop table board2;
--drop table emp01;
--drop table emp44;
--drop table emp3;
--drop table stu;
--drop table chartable;
--drop table chartable2;
--drop table detetable;

create table mem(
id varchar2 (30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number (3) default 0,
birth date ,
gender varchar2(6) check(gender in ('Male', 'Female')),
hobby varchar2 (50) default 'game',
mdate date default sysdate
);

insert into mem values (
'aaa','1111','홍길동','24','2000/05/05','Male', 'golf', sysdate
);
insert into mem values (
'bbb','1111','유관순','24','2000/06/05','Female', 'book', sysdate
);
insert into mem values (
'ccc','1111','이순신','23','2001/07/25','Male', 'game', sysdate
);
commit;

select * from mem;
select department_id, count(*) from employees, departments where department_id = 50 group by department_id ;

select count(*), a.department_id, department_name from employees a, departments b 
where a.department_id = b.department_id and a.department_id = 50 group by a.department_id, department_name ;

insert into mem values (
'ddd','1111','강감찬','22','20220312','Male','game',sysdate
);
rollback;

select * from mem;




