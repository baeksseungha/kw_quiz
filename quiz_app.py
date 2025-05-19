import streamlit as st

st.title("광운대학교 퀴즈")

st.header("1. 광운대학교 축제 시작일은?")
answer1 = st.radio(
    "정답을 선택하세요:",
    ("1. 5월 20일", "2. 5월 21일", "3. 5월 22일", "4. 5월 23일"),
    index=None  
)

if answer1:
    if answer1.startswith("2."):
        st.success("정답입니다!!")
    else:
        st.error("틀렸습니다ㅜㅜ")

st.header("2. 광운대학교 도서관이 있는 건물의 이름은 00주년 기념관이다. 00에 들어갈 숫자는?")
answer2 = st.text_input("숫자를 입력하세요 (예: 40)")

if answer2:
    if answer2.strip() == "80":
        st.success("정답입니다! 🎉")
    else:
        st.error("틀렸습니다. 정답은 80입니다.")
