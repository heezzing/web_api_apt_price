<img width="700" alt="스크린샷 2022-09-14 오후 4 08 22" src="https://user-images.githubusercontent.com/97447841/190085148-f3aea0a0-9504-427b-891f-2c4318c18782.png">

Date : 2022.4.18~2022.4.21

Tags : `MongoDB` `Flask` `Dashboard` 

Link : [https://github.com/heezzing/project3.git](https://github.com/heezzing/project3.git)

발표영상 : [https://www.youtube.com/watch?v=6ZoDUOP_lXU](https://www.youtube.com/watch?v=6ZoDUOP_lXU)

## 개요
- 주제 : 광명시 아파트 매매가 예측 웹 어플리케이션
- 데이터 출처  :  공공데이터포털
    
    [경기도 광명시_아파트매매 실거래자료 현황](https://www.data.go.kr/data/15033120/openapi.do)
    
- 기여 내용 : mongodb 데이터 적재,Flask 이용한 웹 어플리케이션, 대시보드 ,데이터 분석

## 프로젝트 내용
- 주제는 광명시 아파트 매매가 예측 웹 어플리케이션 입니다.
- 프로젝트 목적 : 데이터베이스에 데이터 적재 후 flask를 이용하여 웹 어플리케이션 제작하는 과정을 알기위해 제작하였습니다.
- 데이터 수집은 공공데이터포털에서 경기도 광명시_아파트매매 실거래자료 현황 csv,json 파일을 다운받았습니다.

### 파이프라인
<img width="700" alt="스크린샷 2022-09-14 오후 4 33 04" src="https://user-images.githubusercontent.com/97447841/190090313-1bd7df49-24d9-4f04-9bb3-a7c415ed363f.png">

- 공공기관에서 json파일을 다운받았습니다.
- json파일을 MongoDB에 적재하였습니다.
- 적재된 데이터를 Flask를 이용해 웹 어플리케이션을 만들어 보았습니다.

### 서비스 시연 1(html)
<img width="700" alt="스크린샷 2022-09-14 오후 4 33 46" src="https://user-images.githubusercontent.com/97447841/190090456-dc0461e9-8831-4620-98b6-ea9249d79320.png">

- 광명시 아파트 리스트를 html로 표현해 보았습니다

### 서비스 시연 2(Dash board)
<img width="700" alt="스크린샷 2022-09-14 오후 4 35 20" src="https://user-images.githubusercontent.com/97447841/190090797-48bbec44-aa68-424f-b253-038b163243db.png">

- 데시보드를 이용해서 데이터를 분석해 보았습니다.
- 2015년부터 2022년까지 년도별 아파트 매매량을 분석해 보았습니다.
- 2019년에 매매량이 현저히 적은걸 알 수 있습니다.그 이유는 구로차량기지가 광명으로 이전한다는 이슈 때문입니다.대표적인 혐오시설의 이전으로 인하여 매매량이 급격히 떨어진걸 알 수 있습니다.
    
- 월별 매매량을 분석해본 결과 7월이 가장 높았습니다.자녀들의 학업을 위해 여름방학이 시작되면 이사를 가는걸 알 수 있습니다.
    
- 층별 선호도를 분석해 보았습니다.광명시에서 선호하는 층수는 1층에서 5층 사이로 볼 수 있습니다.그 이유는 저층 건물들이 비교적 많은 편이라 그런것 같습니다.

### 프로젝트 후 느낀점 및 아쉬운점
<img width="700" alt="스크린샷 2022-09-14 오후 4 36 53" src="https://user-images.githubusercontent.com/97447841/190091138-25444b8e-e33b-4fc8-8277-17ae4d890637.png">

- 느낀점 
   - 프로젝트를 진행하면서 section3의 전체적인 흐름이 정리가 된거 같습니다.
    - 많이 낯설었던 flask,mongodb,cli등을 사용하는데 부담이 없어졌고 친근해 졌습니다.
- 아쉬운점
    - 머신러닝을 이용하여 예측을 하지 못해 아쉽습니다.



