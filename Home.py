import streamlit as st

from pages import actions
from utils.page import page_group

def main():

    st.title('Todo List Manager')
    
    page = page_group("p")

    with st.sidebar:
        st.title("🎈 Todo List Manager")

        with st.expander("🧩 COMPONENTS", True):
            page.item("Actions", actions)

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Todo List Manager", page_icon="🎈", layout="wide")
    main()