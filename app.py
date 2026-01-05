import streamlit as st
from traffic_model import optimize_traffic

st.set_page_config(page_title="Traffic Flow Optimization")

st.title("Traffic Flow Optimization System")
st.write("Enter traffic density values for each direction")

ns = st.number_input("North–South Traffic Density", min_value=0, step=1)
ew = st.number_input("East–West Traffic Density", min_value=0, step=1)

if st.button("Optimize Signal"):
    result = optimize_traffic(ns, ew)
    st.success(result)

st.write("Decision is based on higher traffic density")
