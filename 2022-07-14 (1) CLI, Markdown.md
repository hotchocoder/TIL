# CLI

1. **GUI와 CLI**

   * GUI(Graphic User Interface)

     * 일반 사용자가 쓰는 파란 화면.
     * <u>그래픽을 통해</u> 사용자와 컴퓨터가 상호작용하는 방식

   * CLI(Command Line Interface)

     * 개발자가 쓰는 검은 화면.

     * <u>명령어를 통해</u> 작용

       

2. **기본적인 명령어**

   - touch: 파일 생성

     - 파일의 날짜와 시간을 수정하는 명령어이나, 0바이트 파일을 생성하기 위해 자주 사용됨

   - mkdir(Make directory): 폴더 생성

   - ls(list segment): 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여줌

   - cd(change directory): 현재 작업 중인 디렉토리를 변경

   - rm(remove)

     - rm -r 폴더: 폴더 지울때는 -r 삽입

     

3. **절대경로 vs 상대경로**

   - 절대경로: 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
     - C:/User/hotchocoder/Desktop
   - 상대경로: 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
     - 현재 작업하고 있는 디렉토리가 C:/User일 때, 윈도우 바탕화면으로의 상대 경로는 hotchocoder/Desktop



# Markdown

텍스트 기반의 가벼운 <u>마크업(markup)</u> 언어

<u>문서의 구조와 내용</u>을 같이 쉽고 빠르게 적고자 탄생



1. **Github 문서의 시작과 끝**

   - README.md 파일을 통해 오픈 소스의 공식 문서 작성

   - 개인 프로젝트의 소개 문서 작성

   - 매일 학습한 내용 정리

     => github의 readme 파일은 markdown으로 작성된 설명글임

     

2. **Typora**

   - 실시간 마크다운 변환 (미리보기) 제공
   - 이미지 또는 표 삽입시 매우 편한 UI 제공
   - VS Code 등의 프로그램도 마크다운을 지원하지만 전용 프로그램을 사용하면 더 편함
     - ctrl/ 부르면 원래 문법으로 볼 수 있음



# Markdown 연습

###### 헤딩

- 헤딩(Heading)

  - #,
  - 문서의 제목이나 소제목으로 사용
  - #의 개수에 따라 제목의 수준을 구별 (h1 ~ h6)
  - 문서 구조의 기본
  - 글자 크기를 키우기 위해서 사용하면 안됨

  

- 

- 리스트(List)

  - 1., *, -
  - <u>순서가 있는</u> 리스트(1. 2. 3.)와 <u>순서가 없는</u> 리스트(* - )
  - 목록을 표시하기 위해 사용
  - 많이 사용하는 태그 중 하나

  

  ```code block```

  `inline code block`

- 코드 블럭(Code Block)

  - `
  -  일반 텍스트와 다르게 코드를 예쁘게 출력
  - 개발자가 마크다운 사용
    - like 파이썬에서 콘솔화면에 글자를 출력하기 위해 print()를 사용

  

  [구글](https://google.com)

- 링크(link)

  - [string] (url)
  - string은 보여지는 부분, url은 연결할 곳을 나타냄

  

  ![멍멍](https://item.kakaocdn.net/do/bd40e615e4583f3eb8ad2d940b80173a7154249a3890514a43687a85e6b6cc82)

- 이미지(image)

  - ![string](img_url)
  - 링크와 비슷하지만 이미지를 삽입함
  - 이미지의 너비와 높이는 조절할 수 없음

  

**Bold**

*italic*

~~취소선~~

- 텍스트 강조(Text Emphasis)

  - **, *, ~~

  

---

- 수평선(horizontal line)

  - ---,

  - 가로로 긴 수평선
