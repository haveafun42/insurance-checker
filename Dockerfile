# 파이썬 3.9 버전 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사 및 설치
COPY . .
RUN pip install streamlit google-generativeai

# Streamlit 실행 명령어
EXPOSE 8080
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080"]
