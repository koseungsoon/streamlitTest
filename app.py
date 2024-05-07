import streamlit as st

st.title("인공지능 시인 만들기")

st.header("목차")

st.subheader("1.LLM이란")
st.write("대형 언어 모델(Large language model, LLM) 또는 거대 언어 모델은 수많은 파라미터(보통 수십억 웨이트 이상)를 보유한 인공 신경망으로 구성되는 언어 모델이다.")
st.subheader("2.LLM실습")

if st.button("여기 눌러보세요"):
    st.write("Data Loading...")
    #데이터로딩 함수는 여기에

st.write("당신의 성별은?")

checkbox_btn1 = st.checkbox(' 남')
checkbox_btn2 = st.checkbox(' 여')

if checkbox_btn1:
    st.write('남성입니다')

if checkbox_btn2:
    st.write('여성입니다')


selected_item = st.radio ("오늘의저녁메뉴", ("짜장","짬뽕","볶음밥"))

if selected_item=="짜장":
        st.write("짜장면을 고르셨습니다")
elif selected_item=="짬뽕":
        st.write("짬뽕 고르셨습니다")
elif selected_item=="볶음밥":
        st.write("볶음밥 고르셨습니다")
else:
        st.write("세개중에서 골라주세요")

option = st.selectbox('Please select in selectbox!',
                        ('1학년','2학년','3학년'))

st.write('You selected:' , option)

multi_select = st.multiselect('Please select somethings in multi selectbox!(복수전공은 두개 이상 선택 가능)' ,
                            ['경영','경제','회계','화학',])

                        