import random
import streamlit as st

st.title("Roll Number - Task")

# # Pick a random number from 1 to 125
# number = random.randint(1, 125)

# st.write("The random number is: ", number)

# Add a button to generate a new random number
if st.button("Shuffle"):
    number = random.randint(1, 125)
    lst = ["sing a song", "dance", "eat mayonese", "perform a dialogue", "fav pickup line"]
    task = random.choice(lst)
    st.write("Roll number: ",number)
    st.write("Task: ", task)



    
    

