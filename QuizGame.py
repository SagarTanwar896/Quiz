import streamlit as st
st.balloons()
st.write("What is first letter of alphabet? \nA) b\tB) a\t\nC) s\tD) e")
ans = st.text_input("Enter your answer....")
st.write("you have entered....",ans)
