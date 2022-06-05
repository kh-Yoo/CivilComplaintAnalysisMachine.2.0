# CivilComplaintAnalysisMachine.2.0
## 1. 개발 환경

IntelliJ

![IntelliJ_IDEA_Icon svg](https://user-images.githubusercontent.com/62977669/172030000-b6e32247-e216-494e-b024-c5fa28f08d6a.png)

**사용한 프레임 워크**

![Spring-BOOT-Interview-questions-1](https://user-images.githubusercontent.com/62977669/148311178-285b494a-20e4-42be-9fdd-f38f6232a363.jpg)

## 2. 사용한 언어

Python
![bf534326c82256e07ebcf3a115ed38f5e86a8fb61ea5db06aac1c5195b72e17db21c18b364865e765c22de9795a736590d630966d7d887a17a023fc6ce4bc7b3e6fa33322a215727df10002f4d1ae06b41cc18027fae6b6bce8187e715eed522](https://user-images.githubusercontent.com/62977669/148309905-f7dbb320-8b73-484f-98de-bc5e991ef6f1.png)

Java

![og-social-java-logo](https://user-images.githubusercontent.com/62977669/148309984-d561f395-be9d-4343-9251-992e6dd43565.gif)

## 3. 실행 화면 (동영상)

https://youtu.be/03XD9mLious


## 4. 개선된 점

**네이버 및 구글 로그인 기능 추가**
<img width="950" alt="스크린샷 2022-06-05 오전 9 43 25" src="https://user-images.githubusercontent.com/62977669/172030300-f534f258-792f-468e-b093-9cf002e3ee12.png">

**게시글 조회 기능**
<img width="947" alt="스크린샷 2022-06-05 오전 9 44 29" src="https://user-images.githubusercontent.com/62977669/172030319-1b24fe80-6249-4f24-865f-6e9167159569.png">

**게시글 등록 기능**
<img width="1425" alt="스크린샷 2022-06-05 오전 9 45 06" src="https://user-images.githubusercontent.com/62977669/172030334-4efdbe6d-8325-42ff-8a00-5a9f4b875e2e.png">
<img width="942" alt="스크린샷 2022-06-05 오전 9 45 27" src="https://user-images.githubusercontent.com/62977669/172030335-9b19798e-3be9-4b7e-82fa-1fb5222c46dd.png">

**게시글 수정 기능**
<img width="1418" alt="스크린샷 2022-06-05 오전 9 46 08" src="https://user-images.githubusercontent.com/62977669/172030345-1f4b49a6-1b34-425e-b93f-5f95f369f70a.png">
<img width="952" alt="스크린샷 2022-06-05 오전 9 46 16" src="https://user-images.githubusercontent.com/62977669/172030346-58a50af0-bceb-400d-9126-db74bc234879.png">

**게시글 삭제 기능**
<img width="1422" alt="스크린샷 2022-06-05 오전 9 46 25" src="https://user-images.githubusercontent.com/62977669/172030356-efbdeed7-b97e-44a2-84ed-26af383cfdfd.png">
<img width="1041" alt="스크린샷 2022-06-05 오전 9 46 33" src="https://user-images.githubusercontent.com/62977669/172030357-3ac6e403-7220-43c5-b49f-b6e540dfe508.png">

## 5. 개선된 이유

회원가입과 로그인 기능 대신에 네이버 및 구글 로그인 기능을 선택한 이유는 사용자들이 번거롭지 않기 위해 많은 사용자가 사용하는 웹사이트들의 로그인 기능으로 대체해 편의성을 제공하기 위해서입니다.

게시판을 만든 이유는 사용자들이 민원 분석을 하다가 에러 및 민원이 발생하면 사용자들의 편의 사항을 위해서 민원 분석 도구를 재빠르게 개선하기 위해서입니다.

## 6. 참고한 책 및 개발한 이유
스프링 부트와 AWS로 혼자 구현하는 웹 서비스.

인턴을 진행하면서 제작 기간이 짧아서 툴을 만들기에 급급했고 클린 코드 및 코드에 대한 가독성보다는 기능을 구현하기에 몰두했습니다. 그러다 보니 스프링 부트에 대한 이해와 제가 구현한 코드에 대해서도 잘 모르는 경우가 태반이였습니다. 그러므로 책을 구입해서 읽으면서 민원 분석기를 개선하면서 클린 코드와 어떤 코드로 기능이 구현하는 지에 대해 배웠습니다.
그리고 스프링과 스프링에서 편의성을 제공하기 위해 톰캣 등이 내장된 스프링 부트와의 차이점을 알게 되었고 저는 Request 데이터를 받을 Dto, API 요청을 받을 Controller, 트랜잭션, 도메인 기능 간의 순서를 보장하는 Service 부분들을 사용하면서 스프링 부트에 대해 조금은 알게된 것 같습니다.
