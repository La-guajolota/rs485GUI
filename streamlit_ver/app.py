import streamlit as st
import pandas as pd
from backend.serial_parser import SerialProcessor
from backend.data_manager import DataManager
import time

st.set_page_config(page_title="Leather Measurement Interface", layout="wide")

if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DataManager()
if 'serial_processor' not in st.session_state:
    st.session_state.serial_processor = None
if 'measurement_data' not in st.session_state:
    st.session_state.measurement_data = pd.DataFrame(columns=["Lote", "Pieza", "Area", "Total_Area"])
if 'session_active' not in st.session_state:
    st.session_state.session_active = False

st.title("Leather Measurement Data Terminal")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Session Control")
    client_name = st.text_input("Client Name")
    com_port = st.text_input("COM Port", value="COM3")
    
    if st.button("Start New Session", disabled=st.session_state.session_active):
        if client_name and com_port:
            st.session_state.data_manager.create_session(client_name)
            
            processor = SerialProcessor(port=com_port)
            if processor.start_reading():
                st.session_state.serial_processor = processor
                st.session_state.session_active = True
                st.session_state.measurement_data = pd.DataFrame(columns=["Lote", "Pieza", "Area", "Total_Area"])
                st.rerun()
            else:
                st.error("Failed to open COM port.")

    if st.button("Stop Session", disabled=not st.session_state.session_active):
        if st.session_state.serial_processor:
            st.session_state.serial_processor.stop_reading()
        st.session_state.session_active = False
        st.rerun()

with col2:
    st.subheader("Live Measurement Data")
    data_placeholder = st.empty()
    
    if st.session_state.session_active:
        processor = st.session_state.serial_processor
        while not processor.data_queue.empty():
            new_entry = processor.data_queue.get()
            
            # Update dataframe
            st.session_state.measurement_data.loc[len(st.session_state.measurement_data)] = new_entry
            
            # Persist to Excel
            st.session_state.data_manager.append_data(
                new_entry['lote'], new_entry['pieza'], 
                new_entry['area'], new_entry['total_area']
            )
            
    data_placeholder.dataframe(st.session_state.measurement_data, use_container_width=True)

if st.session_state.session_active:
    time.sleep(1)
    st.rerun()