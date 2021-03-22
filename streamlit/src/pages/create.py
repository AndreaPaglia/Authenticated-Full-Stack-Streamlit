import requests
import json

import streamlit as st

PAGE_TITLE = 'Create Item'

def write():
    st.markdown(f'# {PAGE_TITLE}')

    st.markdown('## Enter item details')
    
    item = {}

    item['name'] = st.text_input(
        label='Item Name',
        value='')

    item['price'] = st.number_input(
        label='Item Price ($USD)',
    )

    create = st.button(label='Create')



if __name__=='__main__':
    write()