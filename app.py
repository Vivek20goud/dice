import streamlit as st
import random as r

st.title("🎲 Dice Game")

# Instructions
st.write("**Roll the dice!**")
st.write("Enter a number between 1 and 6. Press 'Roll' to play!")

# Initialize session state variables
if "cp" not in st.session_state:
    st.session_state.cp = 0  # Computer's score
if "ip" not in st.session_state:
    st.session_state.ip = 0  # User's score
if "last_winner" not in st.session_state:
    st.session_state.last_winner = "Roll the dice!"  # Default message
if "reset_clicked" not in st.session_state:
    st.session_state.reset_clicked = False  # Track if reset was clicked

# Reset function
def reset_game():
    if st.session_state.cp > st.session_state.ip:
        st.session_state.last_winner = "🏆 **Computer won the game!**"
    elif st.session_state.cp < st.session_state.ip:
        st.session_state.last_winner = "🎉 **You won the game!**"
    elif st.session_state.cp == 0 and st.session_state.ip == 0:
        st.session_state.last_winner = "Roll the dice!"  # No winner if game never started
    else:
        st.session_state.last_winner = "🤝 **It's a draw!**"

    # Reset scores
    st.session_state.cp = 0
    st.session_state.ip = 0
    st.session_state.reset_clicked = True  # Mark reset as clicked

# Display last winner or default message
st.success(st.session_state.last_winner)

# User Input
user_input = st.number_input("Enter a number (1-6):", min_value=1, max_value=6, step=1)

if st.button("Roll!"):
    computer_choice = r.randint(1, 6)

    st.write(f"🎲 **Computer:** {computer_choice} | **You:** {user_input}")

    # Determine winner
    if computer_choice > user_input:
        st.write("😢 Computer won this round!")
        st.session_state.cp += 1
    elif computer_choice < user_input:
        st.write("🎉 You won this round!")
        st.session_state.ip += 1
    else:
        st.write("😐 It's a draw!")

# Display Score
st.subheader("Scoreboard")
st.write(f" **Computer:** {st.session_state.cp} |  **You:** {st.session_state.ip}")

# Reset button
if st.button("Reset Game"):
    reset_game()
