import streamlit as st
from streamlit_elements import elements, mui, html, dashboard, sync, event
from streamlit import session_state as state
from types import SimpleNamespace
from pathlib import Path

from .utils import Dashboard, PromptCard


def main():

    st.subheader('Actions')

    with st.expander("GETTING STARTED"):
        st.write((Path(__file__).parent/"README.md").read_text())
    st.title("")


    
    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            prompt_card=PromptCard(board, 0, 0, 2, 2, minW=1, minH=1),
        )
        state.w = w

        w.editor.add_tab("Card content", PromptCard.DEFAULT_CONTENT, "plaintext")
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            w.editor()
            w.player()
            w.pie(w.editor.get_content("Pie chart"))
            w.radar(w.editor.get_content("Radar chart"))
            w.card(w.editor.get_content("Card content"))
            w.data_grid(w.editor.get_content("Data grid"))



    # with elements("dashboard"):

    #     layout = [
    #         # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
    #         dashboard.Item("first_item", 0, 1, 2, 2),
    #         dashboard.Item("second_item", 0, 3, 2, 2, isDraggable=False, moved=False),
    #         dashboard.Item("third_item", 0, 5, 2, 2, isResizable=False),
    #     ]

    #     def handle_layout_change(updated_layout):
    #         # You can save the layout in a file, or do anything you want with it.
    #         # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    #         print(updated_layout)

    #     with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    #         mui.Paper("First item", key="first_item")
    #         mui.Paper("Second item (cannot drag)", key="second_item")
    #         mui.Paper("Third item (cannot resize)", key="third_item")

    # prompt_card()



if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()