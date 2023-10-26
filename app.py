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
    for i in range(10):
        p+=1
        st.write(p)
        time.sleep(1)
        if c:
            break

def stop():
    return os.system("shutdown -a")



def shutdown():
    return os.system("shutdown /s /t 10")

def restart():
    return os.system("shutdown /r /t 10")


if c:
    stop()

if a:
    st.toast("YOUR SYSTEM WILL SHUTDOWN WITHIN 10 SEC")
    shutdown()
    uhd()
    if c:
        stop()
if b:
    time.sleep(1)
    st.toast("YOUR SYSTEM WILL RESTART WITHIN 10 SEC")
    restart()
    uhd()
    if c:
        stop()

    
