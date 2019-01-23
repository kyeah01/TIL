# 2019.01.07

09:00 c9 복습

10:00 c9 - grep

11:00 c9-디렉토리 조작법

## 1. c9 파일조작법

~~~bash
kyeah:~/workspace $ head -13 sonnets.txt			#디폴트값 10 -> 13으로 변경하여 출력
kyeah:~/workspace $ head -n 13 sonnets.txt 			#이게 더 정확한 명령어

~~~

~~~bash
kyeah:~/workspace $ less sonnets.txt				#메뉴얼페이지처럼 파일보기
~~~

`u`는 반페이지 뒤로, `d`는 반페이지 앞으로

`f`는 한페이지 뒤로, `b`는 한페이지 앞으로

`G`는 마지막 줄, 100`G`는 100번째 줄

`/`검색어 는 파일 내에서 서치

~~~bash
kyeah:~/workspace $ grep * sonnets.txt			#*을 서치해서 볼수있게 모두 출력함
kyeah:~/workspace $ grep -i  rose sonnets.txt	# 대소문자 구별하지 않고 서치
~~~



### - grepping process

~~~bash
kyeah:~/workspace $ ps aux							#전체 프로세스를 보는 커맨드
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   1104     4 ?        Ss   00:01   0:00 /mnt/shared/sbin/tini -- /mnt/shared/sbin/micro-inetd 22 /mnt/shared/sb
root           7  0.0  0.0   4052   192 ?        S+   00:01   0:00 /mnt/shared/sbin/micro-inetd 22 /mnt/shared/sbin/dropbear -i -s -m -R
ubuntu       706  0.0  0.0 132712  3648 ?        Rs   00:02   0:00 /mnt/shared/sbin/tmux -u2 -L cloud92.2 new -s kyeah@cli_922 export ISOU
ubuntu       707  0.0  0.0  11276  2660 pts/1    Ss   00:02   0:00 bash -c export ISOUTPUTPANE=0;bash -l
ubuntu       708  0.0  0.0  29124 12780 pts/1    S+   00:02   0:00 bash -l
root        2274  0.0  0.0  19376  2020 ?        Ss   00:06   0:00 /mnt/shared/sbin/dropbear -i -s -m -R
ubuntu      2275  0.1  0.0 1257404 46484 ?       Sl   00:06   0:03 vfs-worker {"pingInterval":5000,"nodePath":"/mnt/shared/lib/node_module
ubuntu      3392  0.0  0.0 123736  2528 pts/2    Ss+  00:24   0:00 /mnt/shared/sbin/tmux -u2 -L cloud92.2 new -s kyeah@cli_987 export ISOU
ubuntu      3394  0.0  0.0  11276  2728 pts/4    Ss   00:24   0:00 bash -c export ISOUTPUTPANE=0;bash -l
ubuntu      3395  0.0  0.0  29080 12960 pts/4    S    00:24   0:00 bash -l
ubuntu      4413  0.0  0.0  17268  2452 pts/4    R+   00:44   0:00 ps aux
~~~

~~~bash
kyeah:~/workspace $ kill -15 2047					#'2047' 프로세스 종료 커맨드
kyeah:~/workspace $ pkill -15 -f ubuntu				#프로세스 이름으로 서치하여 종료
~~~

~~~bash
kyeah:~/workspace $ grep -n rose sonnets.txt			
											#grep을 통해 서치하고 해당 line number 출력
~~~

## 2. 디렉토리

`/` 절대경로 부르는법, root directory

`~`홈디렉토리

/home/ubuntu		==		 ~

```bash
kyeah:~ $ pwd 				#현재위치확인
```



~~~bash
kyeah:~ $ find . -name '*.txt'				# '.'은 홈이하 모든것을 해당하게하는 커맨드

kyeah:~/workspace/cli_test $ cd -			#이전 작업 디렉토리로 이동
/home/ubuntu/workspace
~~~

명령어 결합

```bash
kyeah:~/workspace $ ./configure ; make ; make install 
								# ;으로 연결하여 다음 명령어까지 한번에 오더

kyeah:~/workspace $ ./configure && make && make install
								#';'과는 달리 &&는 앞의 명령어가 실행되지 않으면 실행하지 않음
```

~~~bash
kyeah:~/workspace/cli_test/foobar $ cp -r ../text_files . 		#파일 자체를 복사
kyeah:~/workspace/cli_test/foobar $ cp -r ../text_files/ . 		#파일 내의 내용물을 가져옴
kyeah:~/workspace/cli_test/foobar $ cp -r ../text_files/* .		#파일 자체를 복사
~~~

~~~bash
kyeah:~/workspace/cli_test $ rm -rf second_dir/			# 파일지우기
kyeah:~/workspace/cli_test $ grep -r sesquipedalian text_files/		#파일찾기
~~~

~~~bash
kyeah:~/workspace/cli_test $ mkdir foo && cd foo && echo baz > bar.txt && cat bar.txt  && cd - 
~~~





