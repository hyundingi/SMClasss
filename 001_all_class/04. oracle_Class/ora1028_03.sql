-- students 학생
-- number(3)
-- char : 고정 길이
-- varchar2(20) : 가변형 길이  (데이터에 의해서 저장공간이 할당됨)
-- no, name, kor, eng, math, total, avg, rank 컬럼을 구성해서 테이블을 구현

create table students(
no number(3)
name varvchar2(20)
kor number(3)
eng number(3)
math number(3)
total number(3)
avg number(6,2)
rank number(3)
);

insert into students values (
'1','홍길동','100','100','99','299','99.67',1
);

-- 현재 생성된 테이블 보기
select * form tab;

-- 테이블 타입
desc students

create table no_tab (
no number,
name varchar2 (20),
avg1 number,
avg2 number(5,2) -- 123.23
);

insert into no_tab values(
1,'홍길동',1000/3,1000/3
);

insert into no_tab values(
2,' 유관순',1000/6,1000/6
);

select * from no_tab;

create table date_tab (
no number(4),
s_date date,
s_date2 date
);

-- sysdate : 현재 시간
insert into date_tab values(
1, '2024_09_28', sysdate
);

select * from date_tab;

-- to char : 시간 타입 변경
select to_char(s_date,'yyyy-mm-dd'), to_char(s_date2, 'yyyy-mm-dd hh24:mi:ss') from date_tab;

select to_char(s_date,'yyyy-mm-dd hh:mi:ss') from date_tab;

-- select 검색
-- 대소문자 구별 없음 / 그러나 테이블 안 값은 대소문자를 구분함.
-- select 컬럼명 from 테이블명
-- select * (모든 컬럼 의미) from 테이블명
select * from employees;
select employee_id, emp_name from employees;
select EMP_NAME FROM EMPLOYEES;

-- select emp_name from employees where emp_name = 'pat fay' 검색 안 됨
select emp_name from employees where emp_name = 'Pat Fay';

select * from employees;
-- 사원번호, 사원명, 전화번호, 입사일 출력
select employee_id, emp_name, phone_number, hire_date from employees;

select employee_id, emp_name, job_id from employees where job_id = 'SH_CLERK';

-- 테이블 삭제
drop table member;

create table member (
	id number,
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(100),
	mdate DATE
);
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (1, '9122', 'Teggart', 'gteggart0@naver.com', '314-134-5080', 'Non-binary', 'golf', '2024-04-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (2, '7364', 'Petican', 'fpetican1@goo.ne.jp', '731-743-1711', 'Male', 'swim', '2024-05-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (3, '8334', 'Deboy', 'fdeboy2@acquirethisname.com', '363-559-1354', 'Male', 'run', '2024-03-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (4, '9072', 'Sparshott', 'hsparshott3@deviantart.com', '933-703-6077', 'Female', 'book', '2024-01-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (5, '1486', 'Esslemont', 'aesslemont4@ameblo.jp', '182-410-6079', 'Male', 'golf', '2024-03-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (6, '8345', 'McGlue', 'cmcglue5@cnn.com', '678-974-8579', 'Agender', 'run', '2024-02-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (7, '5550', 'Wendover', 'cwendover6@instagram.com', '884-243-7185', 'Female', 'golf', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (8, '2329', 'Lomasna', 'alomasna7@utexas.edu', '157-974-8607', 'Male', 'book', '2024-02-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (9, '6524', 'McCarthy', 'cmccarthy8@free.fr', '454-234-2735', 'Female', 'run', '2024-10-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (10, '6030', 'Springell', 'aspringell9@aboutads.info', '284-577-8307', 'Male', 'game', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (11, '7915', 'Thewles', 'ethewlesa@devhub.com', '123-774-9151', 'Female', 'golf', '2024-07-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (12, '4702', 'Spensley', 'aspensleyb@go.com', '482-791-1826', 'Male', 'swim', '2024-01-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (13, '4096', 'Joreau', 'ljoreauc@jigsy.com', '762-299-5988', 'Female', 'golf', '2024-04-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (14, '5685', 'Footitt', 'zfootittd@sphinn.com', '705-594-1128', 'Female', 'golf', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (15, '6465', 'Christophers', 'pchristopherse@altervista.org', '722-638-0335', 'Male', 'book', '2024-05-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (16, '1440', 'Bugge', 'abuggef@so-net.ne.jp', '317-418-3340', 'Male', 'golf', '2024-06-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (17, '9150', 'Lougheid', 'ylougheidg@elegantthemes.com', '277-334-3318', 'Female', 'golf', '2024-09-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (18, '1878', 'Harbar', 'hharbarh@ebay.com', '786-782-9399', 'Male', 'run', '2024-08-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (19, '3979', 'Rushford', 'mrushfordi@jimdo.com', '985-868-3424', 'Male', 'book', '2024-03-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (20, '5894', 'Widocks', 'nwidocksj@bloglovin.com', '984-688-1772', 'Female', 'golf', '2024-06-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (21, '3317', 'Stalley', 'hstalleyk@symantec.com', '746-583-7988', 'Male', 'run', '2024-02-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (22, '8571', 'Stains', 'cstainsl@nytimes.com', '178-305-0971', 'Female', 'golf', '2024-08-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (23, '2189', 'Caukill', 'kcaukillm@wikia.com', '354-518-7602', 'Male', 'game', '2024-06-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (24, '5875', 'Lange', 'glangen@ocn.ne.jp', '943-570-0643', 'Female', 'book', '2024-10-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (25, '9058', 'Handslip', 'chandslipo@ovh.net', '710-343-7346', 'Male', 'golf', '2024-05-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (26, '9749', 'Anstee', 'ransteep@yandex.ru', '359-558-1425', 'Female', 'book', '2024-08-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (27, '4430', 'Bairstow', 'kbairstowq@addthis.com', '367-528-9397', 'Male', 'book', '2024-03-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (28, '9381', 'McWard', 'mmcwardr@state.gov', '815-556-3420', 'Female', 'game', '2024-07-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (29, '5508', 'Preshous', 'mpreshouss@google.nl', '660-615-7093', 'Male', 'run', '2023-12-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (30, '4522', 'Masseo', 'cmasseot@va.gov', '981-131-1117', 'Female', 'book', '2024-05-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (31, '9617', 'Kembley', 'qkembleyu@walmart.com', '688-885-0908', 'Male', 'run', '2024-05-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (32, '8128', 'Kubicka', 'ckubickav@soundcloud.com', '377-246-0484', 'Female', 'run', '2024-08-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (33, '6202', 'Stallebrass', 'jstallebrassw@bloomberg.com', '398-373-2437', 'Male', 'book', '2024-05-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (34, '5102', 'Maffini', 'cmaffinix@nature.com', '633-787-3981', 'Female', 'swim', '2024-07-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (35, '5404', 'Astie', 'castiey@ibm.com', '642-371-2376', 'Female', 'game', '2023-12-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (36, '3786', 'McPake', 'fmcpakez@g.co', '800-428-6374', 'Polygender', 'swim', '2024-07-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (37, '4651', 'Feldhuhn', 'pfeldhuhn10@mtv.com', '826-518-0739', 'Female', 'game', '2024-06-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (38, '5627', 'O''Noulane', 'nonoulane11@xing.com', '876-914-4799', 'Male', 'game', '2024-07-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (39, '8206', 'Pinner', 'lpinner12@yahoo.com', '856-152-3537', 'Genderfluid', 'swim', '2024-03-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (40, '9400', 'Saul', 'csaul13@jigsy.com', '688-777-0057', 'Female', 'game', '2024-04-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (41, '9514', 'Nielson', 'nnielson14@deliciousdays.com', '491-516-9927', 'Female', 'run', '2023-11-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (42, '1090', 'McCullogh', 'cmccullogh15@reddit.com', '233-246-2286', 'Agender', 'swim', '2024-07-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (43, '7144', 'Kas', 'mkas16@yandex.ru', '775-392-3613', 'Male', 'game', '2024-01-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (44, '8002', 'Milella', 'cmilella17@bluehost.com', '156-373-3454', 'Male', 'run', '2024-05-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (45, '1787', 'Lejeune', 'olejeune18@seesaa.net', '504-886-6631', 'Male', 'golf', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (46, '3329', 'Belmont', 'wbelmont19@wiley.com', '652-321-8921', 'Female', 'book', '2023-11-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (47, '5417', 'Ashbridge', 'cashbridge1a@japanpost.jp', '431-652-4410', 'Male', 'golf', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (48, '7674', 'Rops', 'krops1b@census.gov', '124-901-6351', 'Male', 'game', '2024-08-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (49, '5672', 'Sample', 'asample1c@aol.com', '921-638-2655', 'Male', 'golf', '2024-05-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (50, '2587', 'Sexten', 'nsexten1d@networksolutions.com', '878-741-8952', 'Female', 'run', '2024-04-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (51, '4416', 'Heasley', 'rheasley1e@nbcnews.com', '686-692-4366', 'Genderfluid', 'book', '2024-09-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (52, '6980', 'Mungan', 'pmungan1f@paypal.com', '232-760-3193', 'Bigender', 'game', '2024-09-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (53, '6871', 'Gofton', 'sgofton1g@ucla.edu', '154-931-6115', 'Female', 'game', '2024-06-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (54, '4911', 'Simony', 'asimony1h@yandex.ru', '325-590-7386', 'Male', 'game', '2024-08-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (55, '3150', 'Maudson', 'gmaudson1i@angelfire.com', '442-889-7622', 'Male', 'swim', '2024-06-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (56, '5387', 'Sharply', 'rsharply1j@umich.edu', '537-258-4592', 'Genderfluid', 'run', '2024-09-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (57, '2395', 'Trunks', 'jtrunks1k@uol.com.br', '442-213-6558', 'Female', 'golf', '2024-08-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (58, '5089', 'Elvey', 'relvey1l@bbc.co.uk', '476-227-3208', 'Genderfluid', 'run', '2024-02-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (59, '5136', 'Joust', 'hjoust1m@people.com.cn', '438-991-4995', 'Male', 'swim', '2024-06-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (60, '7442', 'Hablet', 'lhablet1n@instagram.com', '993-986-6250', 'Female', 'game', '2024-04-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (61, '7894', 'Schrei', 'gschrei1o@abc.net.au', '519-200-3868', 'Female', 'swim', '2024-05-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (62, '5069', 'Soars', 'esoars1p@amazon.co.jp', '435-506-9351', 'Female', 'swim', '2024-08-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (63, '8033', 'Benstead', 'jbenstead1q@nhs.uk', '585-824-0375', 'Male', 'golf', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (64, '2753', 'Lorkins', 'elorkins1r@google.de', '519-193-6800', 'Male', 'book', '2024-10-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (65, '7226', 'Licciardiello', 'tlicciardiello1s@prweb.com', '664-676-7321', 'Male', 'book', '2024-01-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (66, '1102', 'Haskell', 'ghaskell1t@bloglines.com', '295-876-5471', 'Male', 'game', '2024-05-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (67, '8768', 'McGray', 'gmcgray1u@google.pl', '288-714-3094', 'Female', 'game', '2024-03-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (68, '2461', 'Blayney', 'ablayney1v@mtv.com', '693-821-1705', 'Male', 'swim', '2023-11-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (69, '6008', 'Cote', 'jcote1w@wsj.com', '951-734-8950', 'Female', 'game', '2023-12-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (70, '6837', 'Letson', 'cletson1x@europa.eu', '258-731-2804', 'Male', 'golf', '2023-11-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (71, '6181', 'Tocqueville', 'htocqueville1y@dedecms.com', '736-907-2300', 'Male', 'swim', '2024-06-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (72, '5013', 'Cushion', 'ecushion1z@phoca.cz', '269-323-6292', 'Female', 'swim', '2024-01-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (73, '2465', 'Cockrell', 'ecockrell20@vkontakte.ru', '883-135-6627', 'Female', 'game', '2024-06-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (74, '3229', 'Syred', 'csyred21@aol.com', '611-397-9842', 'Bigender', 'game', '2024-05-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (75, '4229', 'Sammut', 'rsammut22@privacy.gov.au', '718-516-8343', 'Female', 'book', '2024-04-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (76, '6858', 'Corbally', 'jcorbally23@zimbio.com', '947-420-6316', 'Female', 'run', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (77, '1074', 'Watton', 'jwatton24@google.de', '962-765-4866', 'Female', 'game', '2024-05-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (78, '7076', 'McLeoid', 'smcleoid25@buzzfeed.com', '813-998-5299', 'Genderqueer', 'book', '2024-01-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (79, '1878', 'Gallandre', 'jgallandre26@xrea.com', '555-996-6151', 'Male', 'swim', '2024-06-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (80, '2799', 'Allmann', 'eallmann27@over-blog.com', '817-538-0016', 'Female', 'run', '2024-01-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (81, '8371', 'Walworche', 'fwalworche28@wufoo.com', '499-262-1495', 'Male', 'run', '2023-12-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (82, '3029', 'Treffrey', 'atreffrey29@berkeley.edu', '627-352-1191', 'Non-binary', 'run', '2023-12-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (83, '9011', 'Buckham', 'tbuckham2a@alexa.com', '147-605-1197', 'Female', 'book', '2023-11-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (84, '4543', 'Birchenhead', 'lbirchenhead2b@hexun.com', '430-639-0295', 'Male', 'run', '2023-10-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (85, '4173', 'Vasyagin', 'rvasyagin2c@booking.com', '379-640-1240', 'Male', 'swim', '2024-01-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (86, '6357', 'Asee', 'masee2d@rakuten.co.jp', '418-819-9113', 'Female', 'swim', '2024-01-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (87, '9984', 'Attride', 'cattride2e@netvibes.com', '715-929-4856', 'Female', 'run', '2024-02-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (88, '9595', 'Prator', 'lprator2f@foxnews.com', '303-316-6497', 'Male', 'swim', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (89, '7606', 'Hulbert', 'shulbert2g@foxnews.com', '161-373-9499', 'Male', 'golf', '2024-07-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (90, '2533', 'Foyster', 'gfoyster2h@yahoo.com', '882-796-6680', 'Female', 'golf', '2024-03-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (91, '4431', 'Cardenas', 'mcardenas2i@simplemachines.org', '748-663-2548', 'Female', 'run', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (92, '9525', 'McNickle', 'cmcnickle2j@delicious.com', '865-811-2130', 'Female', 'golf', '2024-08-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (93, '5134', 'McCluskey', 'fmccluskey2k@kickstarter.com', '849-926-2501', 'Male', 'golf', '2023-12-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (94, '4198', 'Culcheth', 'vculcheth2l@samsung.com', '712-851-3794', 'Male', 'game', '2024-09-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (95, '2244', 'Hapke', 'chapke2m@pbs.org', '814-489-5565', 'Male', 'swim', '2024-08-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (96, '8767', 'Ledeker', 'dledeker2n@nhs.uk', '344-735-7762', 'Female', 'run', '2024-07-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (97, '2551', 'Diego', 'rdiego2o@hao123.com', '510-478-4282', 'Female', 'swim', '2024-02-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (98, '4667', 'Devereu', 'cdevereu2p@forbes.com', '925-279-9726', 'Female', 'book', '2024-02-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (99, '2663', 'Dedam', 'jdedam2q@cloudflare.com', '817-678-3688', 'Male', 'book', '2024-03-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values (100, '1407', 'Vitler', 'rvitler2r@wikispaces.com', '500-376-6141', 'Male', 'game', '2024-03-20');

commit;

select * from member;

drop table member;

-- 테이블 생성(create), 삭제(drop) 
-- 테이블에 데이터 추가(insert), 삭제(delete), 검색(select), 수정(update)

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
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('aaa', '1111', '홍길동', 'rsherville0@tinyurl.com', '324-226-8544', 'Male', 'golf', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('bbb', '1111', '유관순', 'mrubinlicht1@fotki.com', '475-964-8193', 'Female', 'book', '2024-08-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ccc', '1111', '이순신', 'bchstney2@walmart.com', '541-891-0085', 'Female', 'run', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('ddd', '1111', '강감찬', 'cstubbes3@chron.com', '900-194-4605', 'Female', 'game', '2024-02-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('eee', '1111', '김구', 'tnacey4@list-manage.com', '727-883-1542', 'Female', 'golf', '2024-09-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Trineman', '6216', 'Riobard', 'rtrineman5@prweb.com', '140-720-7698', 'Male', 'book', '2024-09-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Towell', '5201', 'Bryan', 'btowell6@stumbleupon.com', '365-214-7874', 'Male', 'run', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Neagle', '4903', 'Horacio', 'hneagle7@nifty.com', '114-384-4352', 'Male', 'run', '2024-02-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gresham', '4089', 'Valentine', 'vgresham8@quantcast.com', '547-694-3516', 'Female', 'swim', '2024-10-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dare', '6041', 'Doroteya', 'dodare9@dyndns.org', '102-500-7735', 'Female', 'game', '2024-07-29');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Doumic', '1343', 'Stepha', 'sdoumica@com.com', '745-998-5005', 'Female', 'game', '2024-08-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Allmann', '9173', 'Husein', 'hallmannb@imageshack.us', '122-775-3647', 'Male', 'book', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tommis', '6716', 'Roderic', 'rtommisc@sourceforge.net', '673-244-8303', 'Male', 'book', '2024-07-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bleaden', '4168', 'Drud', 'dbleadend@123-reg.co.uk', '838-544-2408', 'Male', 'golf', '2024-06-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('D''Aguanno', '7476', 'Wini', 'wdaguannoe@cyberchimps.com', '237-714-1340', 'Female', 'run', '2024-06-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gegay', '8185', 'Bernette', 'bgegayf@yahoo.com', '982-358-5670', 'Female', 'golf', '2024-07-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Flea', '6937', 'Fidelity', 'ffleag@reverbnation.com', '602-708-0462', 'Female', 'run', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shory', '1240', 'Robb', 'rshoryh@intel.com', '621-231-3542', 'Male', 'run', '2024-09-13');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Harm', '1438', 'Flinn', 'fharmi@yelp.com', '328-792-9216', 'Male', 'golf', '2023-12-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Poschel', '9693', 'Sterling', 'sposchelj@usnews.com', '499-462-1400', 'Male', 'swim', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Medford', '5717', 'Jacquenette', 'jmedfordk@epa.gov', '634-270-7550', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gianelli', '5559', 'Katherina', 'kgianellil@wikipedia.org', '967-878-2128', 'Female', 'game', '2024-05-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kolodziejski', '5522', 'Danella', 'dkolodziejskim@jugem.jp', '110-354-1019', 'Female', 'golf', '2024-03-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mildmott', '9678', 'Jule', 'jmildmottn@wix.com', '286-208-5611', 'Male', 'run', '2024-07-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pietrowski', '6843', 'Ediva', 'epietrowskio@photobucket.com', '571-362-5389', 'Female', 'golf', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chasemoore', '9290', 'Dunc', 'dchasemoorep@geocities.jp', '390-444-9215', 'Male', 'golf', '2024-03-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Overnell', '6410', 'Barth', 'bovernellq@cdbaby.com', '825-465-2790', 'Male', 'run', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Benford', '8906', 'Margette', 'mbenfordr@twitter.com', '210-839-4892', 'Female', 'swim', '2024-06-20');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Portman', '6013', 'Orson', 'oportmans@reverbnation.com', '258-285-2186', 'Male', 'golf', '2024-06-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Elflain', '7065', 'Trish', 'telflaint@intel.com', '319-787-3297', 'Female', 'golf', '2024-04-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ockland', '7153', 'Deirdre', 'docklandu@sfgate.com', '895-501-5958', 'Female', 'run', '2023-12-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Le Floch', '5518', 'Linea', 'lleflochv@hp.com', '734-888-6261', 'Female', 'swim', '2024-01-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('McGaugan', '5439', 'Conny', 'cmcgauganw@imageshack.us', '376-451-4038', 'Male', 'game', '2023-11-08');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lilburn', '6148', 'Shepherd', 'slilburnx@sina.com.cn', '250-173-1654', 'Male', 'swim', '2024-07-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Frew', '7401', 'Meaghan', 'mfrewy@unc.edu', '276-431-6409', 'Female', 'swim', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Myner', '1917', 'Lorrie', 'lmynerz@wikimedia.org', '550-264-0011', 'Male', 'book', '2024-10-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Knightsbridge', '2295', 'Elias', 'eknightsbridge10@dedecms.com', '906-789-7346', 'Male', 'swim', '2023-12-30');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Merwood', '6745', 'Georgy', 'gmerwood11@comcast.net', '904-984-7938', 'Male', 'golf', '2024-01-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Dewsbury', '1477', 'Bond', 'bdewsbury12@amazon.co.jp', '106-232-5734', 'Male', 'swim', '2024-02-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kliche', '5468', 'Nevins', 'nkliche13@admin.ch', '608-113-7174', 'Male', 'game', '2024-06-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Fick', '7675', 'Panchito', 'pfick14@senate.gov', '430-438-4575', 'Male', 'book', '2024-03-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Danielczyk', '5661', 'Reinaldos', 'rdanielczyk15@irs.gov', '359-176-0405', 'Male', 'book', '2024-05-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Blazey', '8853', 'Lou', 'lblazey16@about.com', '729-460-3951', 'Male', 'run', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Godly', '6603', 'Pail', 'pgodly17@plala.or.jp', '190-426-8746', 'Male', 'run', '2024-06-02');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Attwoull', '3472', 'Cliff', 'cattwoull18@slideshare.net', '570-758-4710', 'Male', 'golf', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Chason', '5763', 'Terrie', 'tchason19@symantec.com', '650-189-0579', 'Female', 'run', '2024-03-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Noni', '2224', 'Jannel', 'jnoni1a@bloglovin.com', '871-506-4522', 'Female', 'book', '2024-01-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Graham', '3477', 'Mendy', 'mgraham1b@trellian.com', '887-280-4803', 'Male', 'swim', '2024-09-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Griffey', '8521', 'Raff', 'rgriffey1c@51.la', '947-561-4983', 'Male', 'swim', '2024-04-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Wretham', '3484', 'Laure', 'lwretham1d@ted.com', '183-800-2897', 'Female', 'book', '2023-11-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Sewart', '5890', 'Lodovico', 'lsewart1e@shareasale.com', '962-952-9409', 'Male', 'swim', '2024-05-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Leber', '3162', 'Cory', 'cleber1f@foxnews.com', '773-506-6136', 'Female', 'run', '2024-05-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Germain', '2786', 'Teodoor', 'tgermain1g@usda.gov', '287-887-6296', 'Male', 'book', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Dooghaine', '4249', 'Jeni', 'jodooghaine1h@washingtonpost.com', '656-654-8738', 'Female', 'book', '2024-02-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ralestone', '2620', 'Lenard', 'lralestone1i@w3.org', '692-797-1702', 'Male', 'book', '2024-09-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yong', '8340', 'Kasey', 'kyong1j@seattletimes.com', '820-634-7148', 'Female', 'run', '2023-12-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Yukhov', '6010', 'Gallard', 'gyukhov1k@weather.com', '602-990-8790', 'Male', 'run', '2023-12-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Digman', '1555', 'Britt', 'bdigman1l@google.com', '997-747-6638', 'Female', 'game', '2023-11-04');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Rocks', '1647', 'Dane', 'drocks1m@latimes.com', '455-553-6937', 'Male', 'book', '2023-12-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Lewisham', '8757', 'Danni', 'dlewisham1n@addtoany.com', '597-704-9376', 'Female', 'swim', '2024-02-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('O''Spillane', '4868', 'Hamlen', 'hospillane1o@indiegogo.com', '584-856-0076', 'Male', 'golf', '2024-02-19');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keoghane', '8511', 'Garrott', 'gkeoghane1p@accuweather.com', '655-285-1122', 'Male', 'game', '2024-01-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gransden', '3139', 'Maire', 'mgransden1q@bloglines.com', '517-233-8716', 'Female', 'book', '2024-02-24');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kobiera', '5689', 'Jaime', 'jkobiera1r@flickr.com', '325-635-7089', 'Female', 'run', '2023-11-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Craske', '6088', 'Isa', 'icraske1s@delicious.com', '903-771-5929', 'Male', 'golf', '2024-06-26');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Island', '9324', 'Terrance', 'tisland1t@cmu.edu', '569-238-3939', 'Male', 'golf', '2024-03-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Hazeldine', '9138', 'Glenn', 'ghazeldine1u@foxnews.com', '118-455-4847', 'Male', 'game', '2024-08-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gutch', '8827', 'Davin', 'dgutch1v@jiathis.com', '602-127-7922', 'Male', 'book', '2024-07-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pavlenkov', '8269', 'Elane', 'epavlenkov1w@cyberchimps.com', '172-572-0209', 'Female', 'game', '2023-12-27');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kasman', '3887', 'Davita', 'dkasman1x@de.vu', '140-813-6914', 'Female', 'book', '2024-09-15');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Andraud', '6948', 'Gunter', 'gandraud1y@rambler.ru', '999-479-2224', 'Male', 'swim', '2024-03-10');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Mandrey', '9531', 'My', 'mmandrey1z@whitehouse.gov', '809-354-8112', 'Male', 'golf', '2024-04-17');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Teers', '1997', 'Lynda', 'lteers20@bigcartel.com', '831-197-8592', 'Female', 'golf', '2024-07-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('MacBey', '8775', 'Farand', 'fmacbey21@seesaa.net', '319-735-6030', 'Female', 'swim', '2024-06-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bontoft', '2628', 'Blanca', 'bbontoft22@webnode.com', '818-469-6633', 'Female', 'run', '2024-09-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Gercken', '3185', 'Heinrik', 'hgercken23@webmd.com', '604-301-2929', 'Male', 'game', '2024-03-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Huzzay', '5857', 'Alf', 'ahuzzay24@sogou.com', '570-223-4310', 'Male', 'book', '2024-08-16');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tredger', '7675', 'Sherwood', 'stredger25@bbc.co.uk', '527-871-8185', 'Male', 'run', '2024-06-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Canadine', '8566', 'Nicolis', 'ncanadine26@devhub.com', '800-674-8410', 'Male', 'golf', '2024-08-03');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Paireman', '7080', 'Nichol', 'npaireman27@msn.com', '668-411-8679', 'Female', 'run', '2024-01-01');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Powis', '6242', 'Mehetabel', 'mpowis28@surveymonkey.com', '271-883-5391', 'Female', 'book', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Walsh', '7311', 'Luther', 'lwalsh29@gmpg.org', '523-360-3018', 'Male', 'golf', '2024-09-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Pont', '4975', 'Edd', 'epont2a@nbcnews.com', '551-629-4794', 'Male', 'golf', '2024-02-22');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Osborne', '7007', 'Gauthier', 'gosborne2b@naver.com', '711-842-1931', 'Male', 'run', '2024-05-31');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tinker', '8402', 'Andree', 'atinker2c@wp.com', '731-985-8198', 'Female', 'swim', '2023-12-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Persence', '7577', 'Obediah', 'opersence2d@elegantthemes.com', '549-594-4369', 'Male', 'run', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Boatwright', '1204', 'Ernie', 'eboatwright2e@printfriendly.com', '833-853-7804', 'Male', 'swim', '2024-01-18');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Kirkhouse', '6330', 'Pernell', 'pkirkhouse2f@soup.io', '412-173-6891', 'Male', 'book', '2024-06-12');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Ghidetti', '9376', 'Den', 'dghidetti2g@seattletimes.com', '165-768-1973', 'Male', 'run', '2024-10-21');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Keppel', '1397', 'Yolanthe', 'ykeppel2h@harvard.edu', '928-660-5279', 'Female', 'run', '2024-09-09');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Matteini', '7664', 'Zola', 'zmatteini2i@jalbum.net', '672-317-8567', 'Female', 'swim', '2024-05-28');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Malmar', '9156', 'Andriana', 'amalmar2j@ed.gov', '588-732-4548', 'Female', 'run', '2024-01-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Waplington', '7863', 'Tobiah', 'twaplington2k@dell.com', '996-187-6594', 'Male', 'game', '2024-07-11');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Cosyns', '2387', 'Lauri', 'lcosyns2l@edublogs.org', '943-340-9913', 'Female', 'game', '2024-04-05');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Atto', '5832', 'Had', 'hatto2m@mozilla.com', '624-750-8503', 'Male', 'game', '2024-06-07');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Bushell', '8202', 'Franz', 'fbushell2n@indiegogo.com', '274-938-6045', 'Male', 'game', '2024-03-06');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Glassford', '3189', 'Virgil', 'vglassford2o@usatoday.com', '361-318-5270', 'Male', 'run', '2024-05-23');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Aron', '3277', 'Freeland', 'faron2p@timesonline.co.uk', '724-482-5099', 'Male', 'game', '2024-08-25');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Tavner', '8684', 'Brig', 'btavner2q@webeden.co.uk', '366-125-0586', 'Male', 'run', '2024-05-14');
insert into member (id, pw, name, email, phone, gender, hobby, mdate) values ('Shiliton', '5557', 'Sandi', 'sshiliton2r@abc.net.au', '407-488-9852', 'Female', 'book', '2024-01-11');

commit;

select * from member;

-- 삭제, where 조건절 컬럼에 해당되는 값
delete member where id='Trineman';
commit;
delete member where gender = 'Male';
rollback;

delete member where gender = 'Male' and hobby='golf';
delete member where gender = 'Male' or hobby='golf';

delete students where name = '홍길동';
delete students where name = '유관순';
rollback;

-- 수정 
select * from member;
update member set name = '김유신' where id = 'Towell';
commit;

update member set id = 'fff' where id = 'Towell';
commit;

update member set id = 'ggg', name = '홍길자' where id = 'Neagle';

-- 취미가 swim > bike
update member set hobby = 'bike' where hobby = 'swim';
rollback;

-- 연산자
-- 타입 : 숫자인 경우만 연산자가 가능하다. / 더하기 까지는 가능 ㅇㅇ
select * from students;
select name, (kor+eng), kor+math from students;
select name, total -kor/2 from students;

select * from employees;
-- 사원 월급 (달러) > 한화로 표시
select salary, to_char(salary*1384.66, '999,999,999.99') from employees;


select count(*) from member;


