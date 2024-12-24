# 버스 예약 사이트
사용자가 좌석을 예약하고 예약 정보를 확인하는 과정을 Django restAPI 기반으로 구현했다.

## 주요 기능  
1. **버스 조회 및 예약**  
   - 출발지와 도착지, 날짜를 선택해 가능한 버스 목록과 좌석 상태 확인.  
   - 좌석 선택 후 예약 완료 처리.  

2. **예약 정보 확인**  
   - 예약 ID를 통해 예약 정보를 확인 가능.  

## 기술 스택  
- **Backend**: Python, Django  
- **Database**: SQLite3  
- **Frontend**:JavaScript Fetch API

## 파일 구조  
- `urls.py`: API 경로 설정.  
- `views.py`: 예약 처리 및 조회 로직 구현.  
- `models.py`: 데이터베이스 구조 정의 (버스 정보, 예약 정보 등). 
