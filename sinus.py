import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config & CSS for Embedding ---
st.set_page_config(
    page_title="Sine Wave Explorer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS to remove excessive padding and UI elements for clean embedding
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        /* Make the audio player slightly more compact */
        .stAudio { margin-top: -10px; }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("### 🔊 Interactive Sine Wave")
st.markdown(
    "Adjust **Amplitude**, **Frequency**, and **Phase** to see how they change the waveform and sound."
)

# --- Controls (Top Row) ---
with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Limit max to 10.0 to match original, set step for precision
        a = st.slider('Amplitude (A)', 0.0, 10.0, 5.0, 0.1)
    with col2:
        f = st.slider('Frequency (f) [Hz]', 0, 1000, 440, 1)
    with col3:
        phi = st.slider(r'Phase ($\phi$) [rad]', -np.pi, np.pi, 0.0, 0.1, format="%.2f")

# --- Calculations ---
fe = 44100  # Increased sample rate for better audio quality
duration = 1.0
t = np.arange(0.0, duration, 1/fe)
signal = a * np.sin(2 * np.pi * f * t + phi)

# --- Plotting ---
# We use a context manager to handle style without affecting global state
with plt.style.context('default'):
    fig, ax = plt.subplots(figsize=(10, 3))
    
    # Plot only 10ms (0.01s) to see the wave details clearly
    # At 44100Hz, 10ms is approx 441 samples
    samples_to_plot = int(0.01 * fe) 
    
    ax.plot(t[:samples_to_plot], signal[:samples_to_plot], color='#007aff', linewidth=2)
    
    # Visual Polish
    ax.set_title(r'Waveform Zoom (10 ms): $a \sin(2 \pi f t + \phi)$', color='gray', fontsize=10)
    ax.set_ylim(-11, 11)
    ax.set_xlim(0, 0.010)
    ax.set_xlabel('Time (seconds)', fontsize=8, color='gray')
    ax.tick_params(axis='both', colors='gray', labelsize=8)
    
    # Transparency for embedding
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    ax.grid(True, alpha=0.2, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_color('gray')

# --- Layout: Plot + Audio + Info ---
row1_col1, row1_col2 = st.columns([3, 1])

with row1_col1:
    st.pyplot(fig, use_container_width=True)

with row1_col2:
    st.markdown("#### 🎧 Listen")
    # Normalize audio by max slider value (10.0) so 'a' controls volume
    # without clipping the browser audio driver.
    st.audio(signal / 10.0, sample_rate=fe)
    
    st.info(
        f"**T:** {1/f:.4f} s\n\n"
        f"**$\lambda$:** {343/f:.2f} m"
    )

# --- Theory Expander ---
with st.expander("📚 The Math Behind the Sound"):
    st.markdown(r"""
    A sine wave is mathematically defined as:
    $$ y(t) = a \sin(2 \pi f t + \phi) $$
    
    * **Frequency ($f$):** Determines the **pitch**. The period is $T = 1/f$.
        Higher $f$ $\rightarrow$ Shorter $T$ $\rightarrow$ Higher pitch.
    * **Amplitude ($a$):** Determines the **loudness**.
    * **Phase ($\phi$):** Shifts the wave in time. 
        A shift of $2\pi$ is one full cycle. While visually obvious, 
        constant phase shifts are generally **inaudible** to the human ear.
    """)



