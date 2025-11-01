import streamlit as st

st.title("🎯 Quiz Game")
st.write("Answer the following 5 questions:")

st.write("ques1>How many words in english Alphabets ?")
answer=st.text_input("enter the choice(26/28/25/24):")
st.write("ques2>what is the natinal flower?")
answer=st.text_input("enter the choice(lotus/sun flower/rose):")
st.write("ques3>what the total bones?")
answer=st.text_input("enter the choice(206/560/216/234):")
st.write("ques4>whatis your friend name?")
answer=st.text_input("enter the choice(Aryan/Monu/Manav/Lokesh):")
st.write("ques5>Who is the Prime Minister of India?")
answer=st.text_input("enter the choice(Rahul Gandhi/Narender Modi/Amit Shah/Adityanath Yogi):")
