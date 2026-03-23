import streamlit as st
import matplotlib.pyplot as plt

st.title("초콜릿 템퍼링 온도")

# 초콜릿 종류별 템퍼링 온도 데이터
temperatures = {
    "다크 초콜릿": 32,
    "밀크 초콜릿": 30,
    "화이트 초콜릿": 29
}

st.write("초콜릿 종류별 템퍼링 온도:")
for chocolate, temp in temperatures.items():
    st.write(f"{chocolate}: {temp}°C")

# 온도 그래프 생성
fig, ax = plt.subplots()
ax.bar(temperatures.keys(), temperatures.values(), color=['brown', 'saddlebrown', 'beige'])
ax.set_ylabel("온도 (°C)")
ax.set_title("초콜릿 템퍼링 온도")
ax.set_ylim(25, 35)  # y축 범위 설정

st.pyplot(fig)
