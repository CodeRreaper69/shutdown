import os
import streamlit as st
import time

st.title("SHUTDOWN")
a = st.button("SHUTDOWN")
b = st.button("RESTART")
c = st.button("STOP")
st.header("TIMER")
def uhd():
    p = 0
    for i in range(60):
        p+=1
        st.write(p)
        time.sleep(1)
        if c:
            break

def stop():
    return os.system("shutdown -a")



def shutdown():
    return os.system("shutdown -h +1")

def restart():
    return os.system("shutdown -r +1")


if c:
    stop()

if a:
    st.write("YOUR SYSTEM WILL SHUTDOWN WITHIN 60 SEC")
    shutdown()
    uhd()
    if c:
        stop()
if b:
    time.sleep(1)
    st.write("YOUR SYSTEM WILL RESTART WITHIN 60 SEC")
    restart()
    uhd()
    if c:
        stop()

    
