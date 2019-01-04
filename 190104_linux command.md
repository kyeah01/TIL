# 2019.01.04 

## 1. 약어설정하는 법

~~~bash
vi ~/.bash_profile 또는 code ~/.bash_profile
alias 약어="명령어"  #띄어쓰기 없어야 함
# 하고 빠져나와서(vim에서는 :wq, code에서는 저장 후 종료)
source ~/.bash_profile
~~~

## 2. 과제풀이





## 3. Cloud9을 통한 flask - cli

~~~bash
kyeah:~/workspace $ echo hello 					# 지정한 문자열이나 (standard out)
hello
kyeah:~/workspace $ echo "hello"				# ""는 변수 활용가능 
hello
kyeah:~/workspace $ echo 'Hello'				# ''는 문자열 그 자체를 땡겨옴
Hello
kyeah:~/workspace $ MYVAR=sometext
kyeah:~/workspace $ echo 'single $MYVAR'
single $MYVAR
kyeah:~/workspace $ echo "double $MYVAR"
double sometext
kyeah:~/workspace $ echo "i'm double"
i'm double
kyeah:~/workspace $ echo 'i'm single'
> ^C
kyeah:~/workspace $ man							# menual page 호출
~~~

### bash 단축키

`ctrl` +`a`  는 현재 커맨드라인 맨 앞으로 c9에서는 `End`

`ctrl` + `e` 는 현재 커맨드라인 맨 뒤로 c9에서는 `Home`키로도 가능

`ctrl` + `l` 은 bash창 clear

`ctrl` + `u` 는 현재 커맨드 전체삭제

`ctrl`  + `w`는 현재 커맨드 커서 기준으로 한 단어 삭제

`ctrl`  + `d` 터미널 종료

`alt` 를 누르고 있으면 마우스로 커맨드위치 선택가능



~~~bash
kyeah:~/workspace $ echo "Someone Like You" > adele.txt		# echo 부등호 하나는 덮어씌움
kyeah:~/workspace $ echo "Hello" >> adele.txt				# 두개는 append
kyeah:~/workspace $ cat adele.txt							# cat은 파일내용 화면에 보여줌
Someone Like You
Hello
kyeah:~/workspace $ echo "Someone Like You" > adele_2.txt
kyeah:~/workspace $ echo "rolling in the deep" >> adele_2.txt 
kyeah:~/workspace $ diff adele.txt  adele_2.txt 			# 비슷한 파일의 다른 점 확인
2c2
< Rolling in the Deep
---
> rolling in the deep
kyeah:~/workspace $ echo 'Im not the only one' > line.txt            
kyeah:~/workspace $ echo 'cant you hear me' > line_2.txt
~~~



~~~bash
kyeah:~/workspace $ cat line.txt > song.txt
kyeah:~/workspace $ cat song
cat: song: No such file or directory
kyeah:~/workspace $ cat song.txt
Im not the only one
kyeah:~/workspace $ cat line2_.txt >> song.txt 
cat: line2_.txt: No such file or directory
kyeah:~/workspace $ cat line_2.txt >> song.txt                       
kyeah:~/workspace $ man cat
kyeah:~/workspace $ cat line_2.txt line.txt  > song_revers.txt
kyeah:~/workspace $ cat song_reverse.txt 
cant you hear me
Im not the only one
~~~



~~~bash
kyeah:~/workspace $ ls					# 숨김파일을 제외한 모든 폴더와 파일을 확인할 수 있음
README.md  adele_2.txt  line_2.txt  song_reverse.txt
adele.txt  line.txt     song.txt 
kyeah:~/workspace $ ls *.txt			# 확장자명이 txt인 파일 모두 서치
adele.txt    line.txt    song.txt
adele_2.txt  line_2.txt  song_reverse.txt
kyeah:~/workspace $ ls s*.txt			# s로 시작하면서 확장자명이 txt인 파일 모두 서치
song.txt  song_reverse.txt				
~~~

~~~python
kyeah:~/workspace $ ls -l									# long format
total 28
-rw-rw-r-- 1 ubuntu ubuntu 699 Aug 31  2017 README.md
-rw-r--r-- 1 ubuntu ubuntu  37 Jan  4 06:40 adele.txt
-rw-r--r-- 1 ubuntu ubuntu  37 Jan  4 06:40 adele_2.txt
-rw-r--r-- 1 ubuntu ubuntu  20 Jan  4 06:42 line.txt
-rw-r--r-- 1 ubuntu ubuntu  17 Jan  4 06:43 line_2.txt
-rw-r--r-- 1 ubuntu ubuntu  37 Jan  4 06:44 song.txt
-rw-r--r-- 1 ubuntu ubuntu  37 Jan  4 06:46 song_reverse.txt

kyeah:~/workspace $ ls -a									# 숨김파일까지 호출
./   .c9/       adele.txt    line.txt    song.txt
../  README.md  adele_2.txt  line_2.txt  song_reverse.txt

kyeah:~/workspace $ ls -r									# 최근 파일 호출
song_reverse.txt  line_2.txt  adele_2.txt  README.md
song.txt          line.txt    adele.txt
~~~

조합해서 활용가능, 커맨드의 순서는 상관없다.



~~~bash
kyeah:~/workspace $ mv test test_file.txt		#이름 바꾸기

kyeah:~/workspace $ mv test test_file.txt
kyeah:~/workspace $ cat test_file.txt 
test test
kyeah:~/workspace $ cp test_file.txt copy_file.txt

kyeah:~/workspace $ rm copy_file.txt 
kyeah:~/workspace $ rm -i test_file.txt                              
rm: remove regular file ‘test_file.txt’? y		# y나 Y만 답으로 인식

kyeah:~/workspace $ rm -f song.txt 				# force의 약자
~~~

~~~bash
kyeah:~/workspace $ ls -l
total 36
-rw-rw-r-- 1 ubuntu ubuntu  699 Aug 31  2017 README.md
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:40 adele.txt
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:40 adele_2.txt
-rw-r--r-- 1 ubuntu ubuntu   20 Jan  4 06:42 line.txt
-rw-r--r-- 1 ubuntu ubuntu   17 Jan  4 06:43 line_2.txt
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:46 song_reverse.txt
-rw-r--r-- 1 ubuntu ubuntu 9339 Jan  4 07:45 sonnes.txt

kyeah:~/workspace $ ls -hl										#human readable
total 36K
-rw-rw-r-- 1 ubuntu ubuntu  699 Aug 31  2017 README.md
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:40 adele.txt
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:40 adele_2.txt
-rw-r--r-- 1 ubuntu ubuntu   20 Jan  4 06:42 line.txt
-rw-r--r-- 1 ubuntu ubuntu   17 Jan  4 06:43 line_2.txt
-rw-r--r-- 1 ubuntu ubuntu   37 Jan  4 06:46 song_reverse.txt
-rw-r--r-- 1 ubuntu ubuntu 9.2K Jan  4 07:45 sonnes.txt
~~~

head

tail

~~~bash
kyeah:~/workspace $ wc sonnets.txt			# wc = word count 
 2621 17671 95642 sonnets.txt				# 줄 단어 바이트 순으로 
kyeah:~/workspace $ wc sonnets_head.txt 
 10  46 294 sonnets_head.txt
kyeah:~/workspace $ head sonnets.txt | wc	# 좌측의 출력을 오른쪽의 입력으로 보냄
     10      46     294
kyeah:~/workspace $ 
~~~

