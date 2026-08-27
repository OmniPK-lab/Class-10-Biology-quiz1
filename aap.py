import streamlit as st
import time

# Import auto-refresh component
try:
    from streamlit_autorefresh import st_autorefresh
    HAS_AUTOREFRESH = True
except ImportError:
    HAS_AUTOREFRESH = False

st.set_page_config(page_title="CBSE Class 10 Biology  Quiz ", layout="wide")
####i have kept it here

# Complete hide for menus, footers, badges, and the breakout fullscreen button
hide_streamlit_style = """
    <style>
    /* Hide top header & standard toolbar */
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    [data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    
    /* Remove embed breakout fullscreen button */
    button[title="View fullscreen"] {display: none !important;}
    [data-testid="StyledFullScreenButton"] {display: none !important;}
    
    /* Hide bottom action buttons & viewer badges */
    [data-testid="stAppViewerOffer"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    div[class*="viewerBadge"] {display: none !important;}
    div[class*="styles_viewerBadge"] {display: none !important;}
    div[class*="stAppToolbar"] {display: none !important;}
    div[class*="stActionButton"] {display: none !important;}
    div[class*="manageApp"] {display: none !important;}
    #stDecoration {display: none !important;}
    </style>
"""
####i have kept it here

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ==========================================
# SIDEBAR: TIMER & CONFIGURATION OPTIONS
# ==========================================

st.sidebar.header("⏱️ Quiz Mode & Timer")
timer_mode = st. sidebar.radio(
    "Choose Quiz Mode:",
    ["Without Timer (Practice Mode)", "With Timer (Exam Mode)"],
    disabled=st.session_state.quiz_started
)

time_limit_sec = 0
if timer_mode == "With Timer (Exam Mode)":
    time_limit_min = st.sidebar.number_input(
        "Set Time Limit (in minutes):",
        min_value=1,
        max_value=180,
        value=30,
        step=1,
        disabled=st.session_state.quiz_started
    )
    time_limit_sec = time_limit_min * 60

    # Auto-refresh every 1000ms (1 second) when quiz is running
    if HAS_AUTOREFRESH and st.session_state.quiz_started and not st.session_state.quiz_submitted:
        st_autorefresh(interval=1000, key="quiz_timer_refresh")

# Reset / Restart Quiz Button
if st.sidebar.button("🔄 Restart / Reset Quiz"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

sidebar_timer_placeholder = st.sidebar.empty()

# ==========================================
# MAIN HEADER & DUAL TIMER DISPLAY
# ==========================================

col_title, col_timer = st.columns([3, 1])

with col_title:
    st.title("CBSE Class 10 Biology Board Revision Quiz")

main_timer_placeholder = col_timer.empty()
warning_banner_placeholder = st.empty()

# Timer Logic & Execution
if timer_mode == "With Timer (Exam Mode)":
    if not st.session_state.quiz_started:
        sidebar_timer_placeholder.info("⏳ Waiting for you to start the test.")
        main_timer_placeholder.info("⏳ Press Start Test below")
    elif st.session_state.quiz_started and not st.session_state.quiz_submitted:
        elapsed_time = int(time.time() - st.session_state.start_time)
        remaining_time = time_limit_sec - elapsed_time

        if remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            time_text = f"⏳ **Time Left:** {mins:02d}:{secs:02d}"

            if remaining_time <= 60:
                warning_banner_placeholder.error("⚠️ **LAST MINUTE WARNING:** Less than 1 minute remaining!")
                sidebar_timer_placeholder.error(time_text)
                main_timer_placeholder.error(time_text)
            else:
                sidebar_timer_placeholder.warning(time_text)
                main_timer_placeholder.warning(time_text)
        else:
            sidebar_timer_placeholder.error("🚨 **Time's Up!**")
            main_timer_placeholder.error("🚨 **Time's Up!**")
            st.session_state.quiz_submitted = True
            st.rerun()
else:
    sidebar_timer_placeholder.info("ℹ️ Practice Mode active.")
    main_timer_placeholder.info("ℹ️ No time limit")

# ==========================================
# QUESTION BANK ( 75 QUESTIONS)
# ==========================================

