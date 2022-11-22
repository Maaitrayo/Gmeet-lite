import streamlit as st
from streamlit_webrtc import webrtc_streamer


col1, col2 = st.columns(2)
with col1:
    webrtc_streamer(key="example")
with col2:
    webrtc_streamer(key="example 1")
