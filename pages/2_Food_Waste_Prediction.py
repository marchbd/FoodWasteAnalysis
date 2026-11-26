import streamlit as st
import plotly.graph_objects as go
from prediction.pipeline import models_ready, predict_food_waste
from utils.data_loader import load_dataset
from utils.theme import apply_theme

apply_theme()

st.markdown("""<style>
/* Only the page background changes here; the two input cards retain their own styles. */
.stApp {
 background:
   radial-gradient(ellipse at 12% 8%, rgba(13,148,136,.22), transparent 34%),
   radial-gradient(ellipse at 88% 12%, rgba(234,179,8,.12), transparent 30%),
   radial-gradient(ellipse at 72% 88%, rgba(20,184,166,.12), transparent 32%),
   linear-gradient(145deg, #071a1c 0%, #0b1724 48%, #171629 100%) !important;
}
</style>""", unsafe_allow_html=True)

st.markdown("""<style>
