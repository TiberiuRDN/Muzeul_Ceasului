import streamlit as st
from streamlit_carousel import carousel
from Final_Dictionary import final_dictionary, image_path
import Path_Carousel

__package__ = None
import sys
print(sys.path)


# Convert the list of dictionaries to a language-keyed dictionary
backbone_dict = {entry['language']: entry for entry in final_dictionary}

# 'RO' as the default language and initiating the st.session_state
if 'selected_language' not in st.session_state:
    st.session_state['selected_language'] = 'RO'

# Sidebar for language selection
with st.sidebar:
    for lang_code in backbone_dict.keys():
        if st.button(backbone_dict[lang_code]['language'], key=lang_code):
            st.session_state['selected_language'] = lang_code


# Access the selected entry directly
selected_entry = backbone_dict[st.session_state['selected_language']]

# Image Carousel
image_list = []
for x in image_path:
    image_list.append(Path_Carousel.carousel_function(title="", text="", img=str(x), link=""))

# Display the content
carousel(items=image_list, width=1.5)
st.title(selected_entry['title'])
if selected_entry['audio'] != 'None':
    st.audio(selected_entry['audio'])
st.write(selected_entry['intro'])





# # QR code
# qr = qrcode.make('http://192.168.0.34:8501/')
# qr.save('/Users/tiberiuradan/Desktop/QR/Demo.png')
# Remember, when deploying from github, packages needs to be stored in a folder named "requirements.txt" while for
# module import you need to store these into a "readme.txt" file
