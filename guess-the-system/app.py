import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Guess the System", layout="centered")

st.title("🗂️ Guess the System")
st.subheader("Based on the file name, can you guess which system it came from?")

# Sample file names and their correct systems
file_pool = [
    {"filename": "AFS_Daily_Subledger.yxmd", "system": "Alteryx"},
    {"filename": "213 Transactions_Prod.txt", "system": "Prologue"},
    {"filename": "AFS GL Codes Tabling VR0053.xlsx", "system": "Alteryx"},
    {"filename": "BSX_Rollup_Export.xml", "system": "OneStream"},
    {"filename": "BL_Recon_Summary_Q1.csv", "system": "Blackline"},
    {"filename": "2295_2095 - In Process Accounts Subledger.yxmd", "system": "Alteryx"},
    {"filename": "AM_User_Permissions.sql", "system": "Prologue"},
    {"filename": "ImportMetadata_2024-12.xml", "system": "OneStream"},
    {"filename": "Blackline_Approver_Review_Report.pdf", "system": "Blackline"},
    {"filename": "CorpEntities_Export.xml", "system": "OneStream"},
]

# Random file for this round (cached so it doesn’t change on re-run)
@st.cache_data
def pick_random_file():
    return random.choice(file_pool)

selected_file = pick_random_file()

# Show file name to user
st.markdown(f"### 📄 `{selected_file['filename']}`")

# Input guess
system_guess = st.selectbox(
    "Which system is this file likely from?",
    options=["", "Alteryx", "Prologue", "Blackline", "OneStream"]
)

submit = st.button("Submit Guess")

if submit:
    correct = selected_file["system"]
    if system_guess == correct:
        st.success(f"✅ Correct! This file belongs to **{correct}**.")
    elif system_guess == "":
        st.warning("🔍 Please select a system before submitting.")
    else:
        st.error(f"❌ Nope — this file is from **{correct}**, not {system_guess}.")

# Footer
st.markdown("---")
st.caption("FinSys Edition | Guess the System 📁")
