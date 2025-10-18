import streamlit as st
# st.balloons()
reset_op = st.sidebar.checkbox() 
def restartt():
  st.write("What is first letter of alphabet? \nA) b\tB) a\t\nC) s\tD) e")
  ans = st.text_input("Enter your answer....")
  st.write("you have entered....",ans)
  if ans == 'b' or ans == 'B':
    st.balloons()
  else:
    st.write("Better luck next time..")
restartt()
