import streamlit as st
from streamlit_elements import elements, mui, html

with elements("new_element"):

    mui.Typography("Hello world")

    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.DoubleArrow,
        "Button with multiple children"
    )

    