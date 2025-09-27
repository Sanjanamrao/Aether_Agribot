# # import streamlit as st
# # from PIL import Image, UnidentifiedImageError
# # import scripts.weed_detection as weed

# # st.set_page_config(page_title="🌱 Weed Detection Dashboard", layout="centered")
# # st.title("🌱 AI-Powered Weed Detection")

# # st.markdown("Upload a field image to detect whether it contains **crop** or **weed**.")

# # # File uploader
# # uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     try:
# #         # Display uploaded image
# #         image = Image.open(uploaded_file)
# #         st.image(image, caption="Uploaded Image", use_column_width=True)

# #         # Run prediction
# #         result = weed.run_demo(uploaded_file)

# #         # Show result
# #         st.success(f"Prediction: **{result['label']}**")
# #         st.info(f"Confidence Score: {result['prob']:.2f}")

# #     except UnidentifiedImageError:
# #         st.error("❌ The uploaded file is not a valid image. Please upload a .jpg or .png file.")
# #     except ValueError as ve:
# #         st.error(f"⚠️ {str(ve)}")
# #     except Exception as e:
# #         st.error(f"⚠️ An unexpected error occurred: {str(e)}")
# # else:
# #     st.warning("Please upload an image to begin detection.")


# # import streamlit as st
# # from PIL import Image, UnidentifiedImageError
# # import scripts.weed_detection as weed
# # import scripts.disease_detection as disease  # ✅ Added disease detection

# # st.set_page_config(page_title="🌱 Crop Health Dashboard", layout="centered")
# # st.title("🌱 AI-Powered Crop Health Detection")

# # st.markdown("Upload a field image to detect whether it contains **crop** or **weed**, or to identify **rice diseases**.")

# # # File uploader
# # uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# # if uploaded_file is not None:
# #     try:
# #         # Display uploaded image
# #         image = Image.open(uploaded_file)
# #         st.image(image, caption="Uploaded Image", use_column_width=True)

# #         # Tabs for separate tasks
# #         tab1, tab2 = st.tabs(["🌿 Weed Detection", "🌾 Disease Detection"])

# #         with tab1:
# #             result = weed.run_demo(uploaded_file)
# #             st.success(f"Prediction: **{result['label']}**")
# #             st.info(f"Confidence Score: {result['prob']:.2f}")

# #         with tab2:
# #             result = disease.run_demo(uploaded_file)
# #             st.success(f"Disease Prediction: **{result['label']}**")
# #             st.info(f"Confidence Score: {result['prob']:.2f}")

# #     except UnidentifiedImageError:
# #         st.error("❌ The uploaded file is not a valid image. Please upload a .jpg or .png file.")
# #     except ValueError as ve:
# #         st.error(f"⚠️ {str(ve)}")
# #     except Exception as e:
# #         st.error(f"⚠️ An unexpected error occurred: {str(e)}")
# # else:
# #     st.warning("Please upload an image to begin detection.")



# import streamlit as st
# from PIL import Image, UnidentifiedImageError
# import scripts.weed_detection as weed
# import scripts.disease_detection as disease

# st.set_page_config(page_title="🌱 AI-Powered Farming Robot Dashboard", layout="centered")
# st.title("🌱 AI-Powered Farming Robot Dashboard")

# # Sidebar task selector
# task = st.sidebar.selectbox("Choose Task", ["Weed Detection", "Disease Detection"])

# # File uploader
# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     try:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_column_width=True)

#         if task == "Weed Detection":
#             result = weed.run_demo(uploaded_file)
#             st.success(f"Prediction: **{result['label']}**")
#             st.info(f"Confidence Score: {result['prob']:.2f}")

#         elif task == "Disease Detection":
#             result = disease.run_demo(uploaded_file)
#             st.success(f"Disease Prediction: **{result['label']}**")
#             st.info(f"Confidence Score: {result['prob']:.2f}")

#     except UnidentifiedImageError:
#         st.error("❌ The uploaded file is not a valid image. Please upload a .jpg or .png file.")
#     except ValueError as ve:
#         st.error(f"⚠️ {str(ve)}")
#     except Exception as e:
#         st.error(f"⚠️ An unexpected error occurred: {str(e)}")
# else:
#     st.warning("Please upload an image to begin detection.")


# ============================================================================
# NOTICE: This Streamlit dashboard has been converted to Flask
# ============================================================================
# 
# The new Flask application is available in app.py
# 
# To run the Flask version:
# 1. Install Flask dependencies: pip install -r flask_requirements.txt
# 2. Run the application: python app.py
# 3. Open your browser to: http://localhost:5000
#
# The Flask version provides:
# - Better performance and scalability
# - Proper REST API endpoints
# - Modern responsive design with Bootstrap
# - Real-time charts with Chart.js
# - Professional UI/UX design
# - Mobile-friendly interface
# ============================================================================

import streamlit as st
from PIL import Image, UnidentifiedImageError
import scripts.weed_detection as weed
import scripts.disease_detection as disease
import scripts.gps_simulation as gps
import scripts.obstacle_avoidance as avoid
import scripts.soil_monitor as soil 

# Configure page with agriculture theme
st.set_page_config(
    page_title="Aether Agribot - Smart Farming Solutions [DEPRECATED - Use Flask version]", 
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="⚠️"
)

# Show deprecation notice
st.error("🚨 **DEPRECATED**: This Streamlit version has been replaced with a modern Flask application.")
st.info("📍 **New Flask Application**: Run `python app.py` to use the improved version with better UI/UX.")
st.warning("🔄 **Migration Complete**: All features have been ported to Flask with enhanced performance.")

# Custom CSS for modern agriculture-themed design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main {
        padding: 0rem;
        background: transparent;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        color: white;
        text-align: center;
        padding: 4rem 2rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="rgba(255,255,255,0.1)"><polygon points="0,0 1000,100 1000,0"/></svg>');
        background-size: cover;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #ffffff, #f0f8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        margin-bottom: 1rem;
        font-weight: 400;
        opacity: 0.95;
    }
    
    .hero-tagline {
        font-size: 1.3rem;
        opacity: 0.85;
        font-style: italic;
        font-weight: 300;
    }
    
    /* Section containers */
    .section-container {
        background: rgba(255, 255, 255, 0.95);
        margin: 2rem 1rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        overflow: hidden;
    }
    
    .section-header {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        padding: 2rem;
        text-align: center;
        position: relative;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 400;
    }
    
    .section-content {
        padding: 2rem;
    }
    
    /* Service cards with glassmorphism */
    .service-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .service-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.7));
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        cursor: pointer;
    }
    
    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.1), transparent);
        transition: left 0.6s;
    }
    
    .service-card:hover::before {
        left: 100%;
    }
    
    .service-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(76, 175, 80, 0.2);
        border-color: rgba(76, 175, 80, 0.3);
    }
    
    .service-icon {
        font-size: 4rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #4CAF50, #2E7D32);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }
    
    .service-title {
        color: #1a365d;
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .service-description {
        color: #4a5568;
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* Interactive elements */
    .interactive-section {
        background: linear-gradient(145deg, rgba(76, 175, 80, 0.05), rgba(46, 125, 50, 0.05));
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid rgba(76, 175, 80, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 2.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
    }
    
    /* File uploader styling */
    .stFileUploader > div > div {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(248, 250, 252, 0.9));
        border: 2px dashed rgba(76, 175, 80, 0.4);
        border-radius: 15px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div > div:hover {
        border-color: #4CAF50;
        background: linear-gradient(145deg, rgba(76, 175, 80, 0.05), rgba(46, 125, 50, 0.05));
    }
    
    /* Results styling */
    .result-container {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(46, 125, 50, 0.05) 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(76, 175, 80, 0.3);
        box-shadow: 0 5px 20px rgba(76, 175, 80, 0.1);
    }
    
    /* Metrics styling */
    .metric-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(248, 250, 252, 0.8));
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(76, 175, 80, 0.2);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        backdrop-filter: blur(10px);
    }
    
    /* Navigation tabs */
    .nav-tabs {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .nav-tab {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(248, 250, 252, 0.9));
        border: 2px solid transparent;
        border-radius: 50px;
        padding: 1rem 2rem;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: 500;
        color: #4a5568;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .nav-tab:hover {
        border-color: #4CAF50;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.2);
    }
    
    .nav-tab.active {
        background: linear-gradient(135deg, #4CAF50, #2E7D32);
        color: white;
        border-color: transparent;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero-section fade-in-up">
    <div class="hero-content">
        <div class="hero-title">🌱 AETHER AGRIBOT</div>
        <div class="hero-subtitle">Smart Agriculture Solutions</div>
        <div class="hero-tagline">Revolutionizing Farming with AI & Robotics</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Service selection tabs
st.markdown("""
<div class="nav-tabs">
    <div class="nav-tab active" onclick="showSection('weed')" id="tab-weed">🌿 Weed Detection</div>
    <div class="nav-tab" onclick="showSection('disease')" id="tab-disease">🌾 Disease Detection</div>
    <div class="nav-tab" onclick="showSection('gps')" id="tab-gps">🛰️ GPS Simulation</div>
    <div class="nav-tab" onclick="showSection('obstacle')" id="tab-obstacle">🚧 Obstacle Avoidance</div>
    <div class="nav-tab" onclick="showSection('soil')" id="tab-soil">🌡️ Soil Monitoring</div>
</div>

<script>
function showSection(sectionName) {
    // Update active tab
    document.querySelectorAll('.nav-tab').forEach(tab => tab.classList.remove('active'));
    document.getElementById('tab-' + sectionName).classList.add('active');
    
    // This would trigger Streamlit rerun in a real implementation
    // For now, we'll use Streamlit's session state
}
</script>
""", unsafe_allow_html=True)

# Session state for tab management
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = 'weed'

# Tab selector (hidden, used for functionality)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🌿", key="weed_btn", help="Weed Detection"):
        st.session_state.active_tab = 'weed'
with col2:
    if st.button("🌾", key="disease_btn", help="Disease Detection"):
        st.session_state.active_tab = 'disease'
with col3:
    if st.button("🛰️", key="gps_btn", help="GPS Simulation"):
        st.session_state.active_tab = 'gps'
with col4:
    if st.button("🚧", key="obstacle_btn", help="Obstacle Avoidance"):
        st.session_state.active_tab = 'obstacle'
with col5:
    if st.button("🌡️", key="soil_btn", help="Soil Monitoring"):
        st.session_state.active_tab = 'soil'

# Hide the button row with CSS
st.markdown("""
<style>
div[data-testid="column"] button {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# Display content based on active tab
if st.session_state.active_tab == "weed":
    st.markdown("""
    <div class="section-container fade-in-up">
        <div class="section-header">
            <div class="section-title">🌿 AI Weed Detection</div>
            <div class="section-subtitle">Advanced Computer Vision for Crop Analysis</div>
        </div>
        <div class="section-content">
    """, unsafe_allow_html=True)
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">📸 Upload Field Image</h3>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose an image for weed detection", 
            type=["jpg", "jpeg", "png"],
            help="Upload a clear image of your field for accurate detection",
            key="weed_uploader"
        )
        
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="📷 Field Image Analysis", use_column_width=True)
            except UnidentifiedImageError:
                st.error("❌ Invalid image file. Please upload a .jpg or .png file.")
                
    with col2:
        if uploaded_file is not None:
            st.markdown("""
            <div class="interactive-section">
                <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">🎯 Detection Results</h3>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                with st.spinner("🔄 Analyzing image with AI..."):
                    result = weed.run_demo(uploaded_file)
                
                # Display results in a beautiful format
                result_color = "#4CAF50" if result['label'].lower() == 'crop' else "#FF9800"
                st.markdown(f"""
                <div class="result-container">
                    <h4 style="color: {result_color}; margin-bottom: 1rem; text-align: center;">🎯 AI Prediction</h4>
                    <div style="text-align: center; margin: 1.5rem 0;">
                        <div style="font-size: 2rem; font-weight: 700; color: {result_color}; margin-bottom: 0.5rem;">
                            {result['label'].upper()}
                        </div>
                        <div style="font-size: 1.2rem; color: #666;">
                            Confidence: <strong>{result['prob']:.1%}</strong>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Recommendations based on result
                if result['label'].lower() == 'weed':
                    st.warning("⚠️ **Weeds Detected!** Consider implementing weed control measures.")
                else:
                    st.success("✅ **Healthy Crops Detected!** Your field looks good.")
                    
            except ValueError as ve:
                st.error(f"⚠️ {str(ve)}")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")
        else:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="text-align: center; color: #2E7D32; margin-bottom: 1rem;">🔬 Ready for Analysis</h4>
                <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Upload an image to see our AI weed detection in action!</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📁</div>
                        <div>JPG, JPEG, PNG</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
                        <div>High Accuracy</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
                        <div>Instant Results</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

elif st.session_state.active_tab == "disease":
    st.markdown("""
    <div class="section-container fade-in-up">
        <div class="section-header">
            <div class="section-title">🌾 Disease Detection</div>
            <div class="section-subtitle">AI-Powered Rice Disease Diagnostics</div>
        </div>
        <div class="section-content">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">🍃 Upload Leaf Sample</h3>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Choose a leaf image for disease detection", 
            type=["jpg", "jpeg", "png"], 
            key="disease_uploader",
            help="Upload a clear image of a rice leaf for disease analysis"
        )

        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="🍃 Leaf Sample Analysis", use_column_width=True)
            except UnidentifiedImageError:
                st.error("❌ Invalid image file. Please upload a .jpg or .png file.")
                
    with col2:
        if uploaded_file is not None:
            st.markdown("""
            <div class="interactive-section">
                <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">🔬 Disease Analysis</h3>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                with st.spinner("🔄 Analyzing leaf sample with AI diagnostics..."):
                    result = disease.run_demo(uploaded_file)
                
                # Display results with appropriate colors
                is_healthy = "healthy" in result['label'].lower() or "normal" in result['label'].lower()
                result_color = "#4CAF50" if is_healthy else "#E65100"
                icon = "✅" if is_healthy else "🦠"
                
                st.markdown(f"""
                <div class="result-container">
                    <h4 style="color: {result_color}; margin-bottom: 1rem; text-align: center;">{icon} Disease Analysis</h4>
                    <div style="text-align: center; margin: 1.5rem 0;">
                        <div style="font-size: 1.8rem; font-weight: 600; color: {result_color}; margin-bottom: 0.5rem;">
                            {result['label']}
                        </div>
                        <div style="font-size: 1.2rem; color: #666;">
                            Confidence: <strong>{result['prob']:.1%}</strong>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Treatment recommendations
                if is_healthy:
                    st.success("🎉 **Healthy Leaf Detected!** Your crop appears to be in good condition.")
                    st.info("💡 **Tip:** Continue regular monitoring and maintain good field hygiene.")
                else:
                    st.error(f"🚨 **Disease Detected:** {result['label']}")
                    st.warning("💊 **Recommendation:** Consult with an agricultural expert for appropriate treatment options.")
                    
            except ValueError as ve:
                st.error(f"⚠️ {str(ve)}")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {str(e)}")
        else:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="text-align: center; color: #2E7D32; margin-bottom: 1rem;">🔬 Disease Diagnostics Ready</h4>
                <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Upload a leaf image for instant disease analysis!</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
                        <div>10+ Diseases</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
                        <div>High Accuracy</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">💊</div>
                        <div>Treatment Tips</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
                        <div>Instant Results</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

elif st.session_state.active_tab == "gps":
    st.markdown("""
    <div class="section-container fade-in-up">
        <div class="section-header">
            <div class="section-title">🛰️ GPS Navigation</div>
            <div class="section-subtitle">Precision Path Planning & Field Mapping</div>
        </div>
        <div class="section-content">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">📍 Field Configuration</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # GPS coordinates input
        st.markdown("**📍 Starting Position**")
        start_lat = st.number_input("🌍 Start Latitude", value=12.9716, format="%.6f", help="Enter the latitude of your field's starting point", key="gps_lat")
        start_lon = st.number_input("🌍 Start Longitude", value=77.5946, format="%.6f", help="Enter the longitude of your field's starting point", key="gps_lon")
        
        st.markdown("**📐 Field Dimensions**")
        rows = st.slider("📏 Number of Rows", min_value=1, max_value=30, value=8, help="How many rows to cover in the field", key="gps_rows")
        cols = st.slider("📏 Number of Columns", min_value=1, max_value=40, value=15, help="How many columns to cover in the field", key="gps_cols")
        
        # Display field info
        st.markdown(f"""
        <div class="interactive-section" style="margin-top: 1.5rem;">
            <h5 style="color: #2E7D32; margin-bottom: 1rem; text-align: center;">📊 Field Summary</h5>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; text-align: center;">
                <div>
                    <div style="font-size: 1.5rem; font-weight: 600; color: #4CAF50;">{rows} × {cols}</div>
                    <div style="color: #666; font-size: 0.9rem;">Grid Coverage</div>
                </div>
                <div>
                    <div style="font-size: 1.5rem; font-weight: 600; color: #4CAF50;">~{rows * cols}</div>
                    <div style="color: #666; font-size: 0.9rem;">GPS Points</div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 1rem; color: #666;">
                <strong>Pattern:</strong> Optimized Zig-zag Movement
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        generate_path = st.button("🚀 Generate GPS Path", type="primary", key="gen_gps_path")
    
    with col2:
        if generate_path:
            st.markdown("""
            <div class="interactive-section">
                <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">🗺️ Path Generation Results</h3>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                with st.spinner("🛰️ Calculating optimal path..."):
                    result = gps.run_demo(start_lat=start_lat, start_lon=start_lon, rows=rows, cols=cols)
                
                # Success metrics in beautiful cards
                st.markdown(f"""
                <div class="result-container">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
                        <div class="metric-card">
                            <div style="font-size: 2rem; font-weight: 600; color: #4CAF50; margin-bottom: 0.5rem;">
                                {result['points_count']}
                            </div>
                            <div style="color: #666;">GPS Points Generated</div>
                        </div>
                        <div class="metric-card">
                            <div style="font-size: 1.5rem; font-weight: 600; color: #4CAF50; margin-bottom: 0.5rem;">
                                Zig-zag
                            </div>
                            <div style="color: #666;">Coverage Pattern</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.success("✅ GPS path successfully generated!")
                st.info(f"📄 Map file saved: `{result['html']}`")
                
                # Instructions
                st.markdown("""
                <div class="interactive-section">
                    <h5 style="color: #2E7D32; text-align: center; margin-bottom: 1rem;">📋 Next Steps</h5>
                    <div style="color: #666; line-height: 1.8;">
                        <div style="margin-bottom: 0.8rem;">📂 Open the generated HTML file in your browser</div>
                        <div style="margin-bottom: 0.8rem;">🗺️ Review the planned path on the interactive map</div>
                        <div style="margin-bottom: 0.8rem;">📤 Upload the GPS coordinates to your robot</div>
                        <div>🤖 Begin autonomous field coverage</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"⚠️ Path generation failed: {str(e)}")
        else:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="text-align: center; color: #2E7D32; margin-bottom: 1rem;">🗺️ Path Planning Ready</h4>
                <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Configure your field parameters and generate the optimal navigation path!</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem;">
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🛰️</div>
                        <div>Precision GPS</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
                        <div>Optimized Patterns</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                        <div>Custom Dimensions</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🗺️</div>
                        <div>Interactive Maps</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)


elif st.session_state.active_tab == "obstacle":
    st.markdown("""
    <div class="section-container fade-in-up">
        <div class="section-header">
            <div class="section-title">🚧 Obstacle Avoidance</div>
            <div class="section-subtitle">Smart Navigation & Real-time Path Adjustment</div>
        </div>
        <div class="section-content">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">⚙️ Navigation Configuration</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # GPS coordinates input
        st.markdown("**📍 Field Starting Point**")
        start_lat = st.number_input("🌍 Latitude", value=12.9716, format="%.6f", key="obs_lat", help="Starting latitude coordinate")
        start_lon = st.number_input("🌍 Longitude", value=77.5946, format="%.6f", key="obs_lon", help="Starting longitude coordinate")
        
        st.markdown("**📐 Field Coverage Area**")
        rows = st.slider("📏 Rows to Cover", min_value=1, max_value=30, value=8, key="obs_rows")
        cols = st.slider("📏 Columns to Cover", min_value=1, max_value=40, value=15, key="obs_cols")
        
        st.markdown("**🚧 Obstacle Simulation**")
        add_obstacle = st.checkbox("🔧 Include sample obstacle for testing", help="Adds a simulated obstacle to test avoidance algorithms")
        
        if add_obstacle:
            st.markdown("""
            <div class="interactive-section" style="margin-top: 1rem;">
                <div style="text-align: center; color: #FF9800;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
                    <div>Sample obstacle will be placed to demonstrate avoidance behavior</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        generate_avoidance = st.button("🤖 Generate Smart Path", type="primary", key="gen_avoid_path")
    
    with col2:
        if generate_avoidance:
            st.markdown("""
            <div class="interactive-section">
                <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">🗺️ Avoidance Results</h3>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                with st.spinner("🤖 Calculating smart avoidance path..."):
                    obstacles = None
                    if add_obstacle:
                        obstacles = [(start_lat + 0.00024, start_lon + 0.0007)]

                    result = avoid.run_demo_with_obstacles(
                        start_lat=start_lat,
                        start_lon=start_lon,
                        obstacles=obstacles,
                        rows=rows,
                        cols=cols
                    )
                
                # Display metrics in beautiful cards
                obstacles_count = len(result['obstacles']) if result['obstacles'] else 0
                st.markdown(f"""
                <div class="result-container">
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
                        <div class="metric-card">
                            <div style="font-size: 1.8rem; font-weight: 600; color: #4CAF50; margin-bottom: 0.3rem;">
                                {result['base_len']}
                            </div>
                            <div style="color: #666; font-size: 0.9rem;">Original Path</div>
                        </div>
                        <div class="metric-card">
                            <div style="font-size: 1.8rem; font-weight: 600; color: #2196F3; margin-bottom: 0.3rem;">
                                {result['new_len']}
                            </div>
                            <div style="color: #666; font-size: 0.9rem;">Adjusted Path</div>
                        </div>
                        <div class="metric-card">
                            <div style="font-size: 1.8rem; font-weight: 600; color: #FF9800; margin-bottom: 0.3rem;">
                                {obstacles_count}
                            </div>
                            <div style="color: #666; font-size: 0.9rem;">Obstacles</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.success("✅ Smart avoidance path generated successfully!")
                
                if result['obstacles']:
                    st.markdown("**🚧 Detected Obstacle Coordinates:**")
                    for i, obs in enumerate(result['obstacles'], 1):
                        st.code(f"Obstacle {i}: {obs}")
                
                # Generate and embed the interactive map
                map_path = avoid.make_map_with_obstacles(
                    base_path=result['base_path'],
                    new_path=result['new_path'],
                    obstacles=result['obstacles'],
                    start_loc=result['base_path'][0]
                )
                
                st.markdown("### 🗺️ Interactive Navigation Map")
                import streamlit.components.v1 as components
                with open(map_path, 'r', encoding='utf-8') as f:
                    map_html = f.read()
                components.html(map_html, height=500)
                
                st.info(f"📄 Map saved to: `{map_path}`")
                
                # Analysis
                if result['new_len'] > result['base_len']:
                    st.warning("⚠️ Path extended due to obstacle avoidance. Review the adjusted route.")
                else:
                    st.success("✅ Efficient path maintained with successful obstacle avoidance.")
                
            except Exception as e:
                st.error(f"⚠️ Avoidance calculation failed: {str(e)}")
        else:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="text-align: center; color: #2E7D32; margin-bottom: 1rem;">🤖 Smart Navigation Ready</h4>
                <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Configure parameters and test our intelligent obstacle avoidance!</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem;">
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🛰️</div>
                        <div>Real-time Paths</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🚧</div>
                        <div>Dynamic Detection</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔄</div>
                        <div>Route Optimization</div>
                    </div>
                    <div style="text-align: center; color: #4CAF50;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                        <div>Map Visualization</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

elif st.session_state.active_tab == "soil":
    st.markdown("""
    <div class="section-container fade-in-up">
        <div class="section-header">
            <div class="section-title">🌡️ Soil Monitoring</div>
            <div class="section-subtitle">Real-time Environmental & System Health Monitoring</div>
        </div>
        <div class="section-content">
    """, unsafe_allow_html=True)
    
    try:
        # Get sensor data
        result = soil.run_demo()
        df = result['dataframe']
        
        # Current readings section with beautiful cards
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1.5rem;">📊 Live Sensor Readings</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            moisture_color = "#4CAF50" if result['moisture_latest'] >= 40 else "#FF9800" if result['moisture_latest'] >= 20 else "#F44336"
            moisture_status = 'Optimal' if result['moisture_latest'] >= 40 else 'Moderate' if result['moisture_latest'] >= 20 else 'Low'
            st.markdown(f"""
            <div class="metric-card" style="border-left: 4px solid {moisture_color};">
                <div style="color: {moisture_color}; font-size: 2rem; margin-bottom: 0.5rem;">💧</div>
                <div style="font-size: 2.2rem; font-weight: 700; color: {moisture_color}; margin-bottom: 0.3rem;">
                    {result['moisture_latest']:.1f}%
                </div>
                <div style="color: #2E7D32; font-weight: 600; margin-bottom: 0.2rem;">Soil Moisture</div>
                <div style="color: #666; font-size: 0.9rem;">{moisture_status}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            temp_color = "#4CAF50" if 20 <= result['temp_latest'] <= 30 else "#FF9800"
            temp_status = 'Ideal Range' if 20 <= result['temp_latest'] <= 30 else 'Monitor'
            st.markdown(f"""
            <div class="metric-card" style="border-left: 4px solid {temp_color};">
                <div style="color: {temp_color}; font-size: 2rem; margin-bottom: 0.5rem;">🌡️</div>
                <div style="font-size: 2.2rem; font-weight: 700; color: {temp_color}; margin-bottom: 0.3rem;">
                    {result['temp_latest']:.1f}°C
                </div>
                <div style="color: #2E7D32; font-weight: 600; margin-bottom: 0.2rem;">Temperature</div>
                <div style="color: #666; font-size: 0.9rem;">{temp_status}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            battery_color = "#4CAF50" if result['battery_latest'] >= 50 else "#FF9800" if result['battery_latest'] >= 20 else "#F44336"
            battery_status = 'Good' if result['battery_latest'] >= 50 else 'Low' if result['battery_latest'] >= 20 else 'Critical'
            st.markdown(f"""
            <div class="metric-card" style="border-left: 4px solid {battery_color};">
                <div style="color: {battery_color}; font-size: 2rem; margin-bottom: 0.5rem;">🔋</div>
                <div style="font-size: 2.2rem; font-weight: 700; color: {battery_color}; margin-bottom: 0.3rem;">
                    {result['battery_latest']:.1f}%
                </div>
                <div style="color: #2E7D32; font-weight: 600; margin-bottom: 0.2rem;">Battery Level</div>
                <div style="color: #666; font-size: 0.9rem;">{battery_status}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Historical data chart
        st.markdown("""
        <div class="interactive-section">
            <h3 style="color: #2E7D32; text-align: center; margin-bottom: 1rem;">📈 Historical Data Trends</h3>
            <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Track sensor readings over time to identify patterns and optimize field conditions</p>
        </div>
        """, unsafe_allow_html=True)
        
        chart_data = df.set_index('time')[['soil_moisture', 'temperature', 'battery']]
        st.line_chart(chart_data)
        
        # Insights and recommendations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="color: #2E7D32; text-align: center; margin-bottom: 1rem;">🎯 Field Status</h4>
            """, unsafe_allow_html=True)
            
            # Generate recommendations based on data
            recommendations = []
            if result['moisture_latest'] < 30:
                recommendations.append("💧 Consider irrigation - soil moisture is below optimal")
            if result['temp_latest'] > 35:
                recommendations.append("🌡️ High temperature detected - monitor crop stress")
            if result['battery_latest'] < 25:
                recommendations.append("🔋 Battery low - schedule maintenance soon")
            if not recommendations:
                recommendations.append("✅ All systems operating within normal parameters")
            
            for rec in recommendations:
                st.markdown(f"• {rec}")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="interactive-section">
                <h4 style="color: #2E7D32; text-align: center; margin-bottom: 1rem;">📊 Monitoring Features</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; color: #666;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">📊</span>
                        <span>Real-time Data</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">💧</span>
                        <span>Auto Irrigation</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">🌤️</span>
                        <span>Weather Sync</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">⚠️</span>
                        <span>Smart Alerts</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">📈</span>
                        <span>Trend Analysis</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="color: #4CAF50;">📱</span>
                        <span>Mobile Alerts</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"⚠️ Monitoring system error: {str(e)}")
        st.markdown("""
        <div class="interactive-section">
            <h4 style="text-align: center; color: #2E7D32; margin-bottom: 1rem;">🌡️ Soil Monitoring System</h4>
            <p style="text-align: center; color: #666; margin-bottom: 1.5rem;">Advanced sensor network for comprehensive field monitoring!</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
                <div style="text-align: center; color: #4CAF50;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                    <div>Real-time Data</div>
                </div>
                <div style="text-align: center; color: #4CAF50;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌡️</div>
                    <div>Multi-sensor</div>
                </div>
                <div style="text-align: center; color: #4CAF50;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔋</div>
                    <div>System Health</div>
                </div>
                <div style="text-align: center; color: #4CAF50;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📈</div>
                    <div>Trend Analysis</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

