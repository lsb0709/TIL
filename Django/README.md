#### [개발환경설정가이드(mac)](Django%20%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95%EA%B0%80%EC%9D%B4%EB%93%9C.md)

#### [Dhango01](/Django/Django01.md)

# Django 개발 환경(mac) 설정 가이드

1. mkdir 파일이름(파일생성)

   ```bash
   mkdir text
   ```

2. cd 가상환경을 설치할 경로(파일)

   ```bash
   cd 파일명
   cd text
   ```

3. 가상환경 생성

   ```bash
   python3 -m venv 가상환경이름
   python3 -m venv test-venv
   ```

4. 가상환경 활성화 (가상환경 켜기)

   ```bash
   source 가상환경이름/bin/activate
   source text-venv/bin/activate
   ```

5. 가상환경 비활성화(가상환경 끄기)

   ```bash
   deactivate
   ```

6. 패키지 다운(Django)

   ```bash
   pip3 install django==원하는 버전
   pip3 install django==3.2.12
   ```

7. 장고관리자를 통해 장고시작

   ```bash
   django-admin startproject [프로젝트이름] [시작경로(현재폴더는 .)]
   django-admin startproject firstpjt .
   ```

8. 장고실행

   ```bash
   python3 manage.py runserver
   ```

9. 구동확인

   ```bash
   인터넷 주소창에 localhost:8000
   ```
