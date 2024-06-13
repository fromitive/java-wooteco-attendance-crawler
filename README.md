## 아직 크루가 되지 못한 별들

출석 처리가 안되는 크루들의 이름을 모니터로 띄어주는 프로그램

## 개발도구

requirements.txt 참고

## 설치 방법

### 1. 가상환경 구성 및 pip install

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. config 디렉터리 생성

``` bash
mkdir config
```

### 3. config/credentials.json 생성

https://developers.google.com/sheets/api/quickstart/python?hl=ko를 참고하여 `credentials.json` 이름으로 api 생성

### 4. config/crew.txt 생성

예시 

```txt
포케
크루명1
크루명2
```

### 5. config/config.txt 생성
`스프레드 시트 Id`|`시트범위`

예시
https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit 스프레드 시트의 Class Data의 A2:E를 추출하고 싶으면

```txt
1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms|Class Data!A2:E
```

## 실행

``` bash
uvicorn main:app --reload
```

http://localhost:8000/static/index.html 으로 접속
