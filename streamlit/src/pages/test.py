import requests
import json

import streamlit as st

PAGE_TITLE = 'Test Page'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.write('Test Page Loads')

if __name__=='__main__':
    write()