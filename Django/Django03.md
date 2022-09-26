## Code Formatter black 설정

<aside> 🧑‍💻 Code Formatter는 1인 개발에서는 코드 스타일에 대한 고민을 줄여주고, 2명 이상의 프로젝트에서 코드 스타일을 통일하기 위해 사용합니다.

</aside>

- 설정 가이드 열기

  - 참고 사이트

    [Python Code Formatter Black 적용기](https://jiku90.tistory.com/12)

    [vscode에서 black으로 code format 자동화하기 (python)](https://lovedh.tistory.com/entry/vscode에서-black으로-code-format-자동화하기-python)

  1. black 패키지 설치(가상환경 마다)

     ```bash
     pip install black
     ```

  2. vscode python formatting provider 설정

     ![Untitled](/Django/images/django3_01.png)

  3. vscode format on save 체크

     ![Untitled](/Django/images/django3_02.png)

  4. 파이썬 코드 수정 후 저장하기

  5. (위 설정으로 적용이 안되면) vscode **@id:editor.defaultFormatter @lang:python defaultFormatter 설정**

     ![Untitled](/Django/images/django3_03.png)