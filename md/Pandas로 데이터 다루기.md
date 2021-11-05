# Pandas로 데이터 다루기

* 데이터를 다루기 위해 필요한 능력
  * 데이터 불러오기 / 데이터 상태 파악하기
  * Row/Column 선택하기
  * 원하는 데이터 찾기 - Query/Search
  * 집계하기 & 그룹으로 묶기
  * 합치기

* DataFrame
  * 여러 개의 column으로 구성된 2차원 형태의 자료구조
  * row와 column으로 이루어진 table 형태의 데이터 객체
  * Series도 알아보고 비교해서 차이점 확인할 것

## 1. 데이터 불러오기 / 파악하기

* `read_csv()`- url도 이용 가능
* `shape` - 행과 열의 개수를 파악한다.
* `info()` - 표의 대략적인 정보를 파악한다.
* `head()  tail()` - 맨 위 / 맨 아래 데이터를 출력해본다.
* `columns` - 칼럼 목록을 출력한다.

> * 레모네이드 판매 데이터
>
>   https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/lemonade.csv
>
> * 보스턴 집값 데이터
>
>   https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/boston.csv
>
> * 아이리스 품종 데이터
>
>   https://raw.githubusercontent.com/blackdew/ml-tensorflow/master/data/csv/iris.csv

## 2. Row/Column 선택하기

* column 선택
  * [칼럼명] - 칼럼 선택. 결과가 Series
  * [[칼럼명1, 칼럼명2, 칼럼명3]] - 칼럼 선택. 결과가 Dataframe
* row 선택
  * loc[ ] - index로 선택
  * iloc[ ] - row 위치로 선택
* row + column 선택
  * iloc[ , ] - row, column 위치로 선택

### 3. 원하는 데이터 찾기 - Query/Search

* 조건문을 통해서 Boolean **Series**를 만든다.
* 안에 Boolean Series를 넣으면 True에 해당하는 행만 반환한다.
* 이 방법을 **“Boolean Indexing”** 이라고 한다.







#### KRX 증권 데이터 라이브러리

* https://github.com/FinanceData/FinanceDataReader