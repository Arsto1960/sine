import streamlit as st
from numpy import *
from matplotlib.pyplot import *

st.title('My first sine wave')
st.markdown('''How do the amplitude, frequency and initial phase of a sine wave 
               influence its shape and sound? Let us try...''')
   
a=st.slider('Amplitude a', 0.0, 10.0, 5.0)
f=st.slider('Frequency f [Hz]', 0, 1000, 440)
phi=st.slider('Initial phase phi [rad]', -pi, pi, 0.0) 

fe=10000;
t=arange(0.0,1,1/fe) 
signal=a*sin(2*pi*f*t+phi)

fig,ax = subplots(figsize=(10,4))
title('10 ms of $a\ \sin(2 \pi f t + phi)$') 
xlim(0,0.010); ylim(-10, 10)
plot(t[0:100],signal[0:100])
xlabel('Time (seconds)')   
st.pyplot(fig)

st.audio(signal,sample_rate=fe) 

with st.expander("Open for comments"):
   st.markdown('''A sine wave is defined as:''')
   st.latex('''a \sin(2 \pi f t + phi)''') 
   st.markdown('''Its period T is given by:''')
   st.latex('''2 \pi f T = 2 \pi''')
   st.latex('''T = 1/f''')
   st.markdown('''The higher $f$, the shorter $T$, and the higher the pitch of the sound.''')
   st.markdown('''The amplitude $a$ simply changes the loudness of the sound.''')
   st.markdown('''The initial phase $phi$ delays ($phi>0$) or advances ($phi<0$) the signal; 2 $\pi$ 
                  corresponds to a one-period shift. Such a shift cannot be heard by 
                  the human ear.''')
    
