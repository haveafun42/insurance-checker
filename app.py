# 1단계: 필요한 라이브러리 설치 (실행 시 첫 번째 셀에 붙여넣으세요)
!pip install -q streamlit google-generativeai

# 2단계: 메인 애플리케이션 코드 (두 번째 셀에 붙여넣고 실행하세요)
import streamlit as st
import google.generativeai as genai

# 여기에 본인의 API 키를 입력하세요 (Google AI Studio에서 무료 발급 가능)
# 시연을 위해 발표 전날 API 키를 세팅하면 됩니다.
genai.configure(api_key="AIzaSyCyEiPgz4H6Dc110qZld6_A921-kdqzJyk") 

st.title("🛡️ 보험사 AI 리스크 스크리닝")
text = st.text_area("검수할 문구를 입력하세요:")

if st.button("분석 실행"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    당신은 보험사 리스크 관리 전문가입니다. 다음 문구가 보험사 홍보물로 적절한지 분석하세요.
    문구: "{text}"
    
    분석 기준:
    1. 사회적 민감도(지역/인물 비하, 혐오 표현 등)
    2. 금융소비자보호법 준수 여부
    3. 기업 품격 저해(부적절한 밈, 신조어)
    
    출력 형식:
    - 위험 등급: (빨강/노랑/초록)
    - 판단 근거: 상세 설명
    - 대체 문구: 제안
    """
    
    response = model.generate_content(prompt)
    st.write(response.text)
