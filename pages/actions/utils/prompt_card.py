import streamlit as st

def prompt_card():
    # Standard text content for the card
    default_content = "This is the standard text content for the card."

    # Display the card with the default content
    card = st.empty()  # Placeholder for the card content
    card.text(default_content)

    # Add a settings button
    if st.button("Settings"):
        # Create a popup for input parameters
        with st.form(key="settings_form"):
            # Text input for prompt
            prompt = st.text_input("Prompt")

            # Multiple selection for options
            options = st.multiselect("Options", ["Option 1", "Option 2", "Option 3"])

            # Control ticks for different names
            control_ticks = []
            for i in range(5):
                tick_name = st.text_input(f"Control Tick {i+1}")
                control_ticks.append(tick_name)

            # Confirmation button to save parameters
            if st.form_submit_button("Save"):
                # Update the card content with the new parameters
                updated_content = f"Prompt: {prompt}\nOptions: {options}\nControl Ticks: {control_ticks}"
                card.text(updated_content)

