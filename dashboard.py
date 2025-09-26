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


import streamlit as st
from PIL import Image, UnidentifiedImageError
import scripts.weed_detection as weed
import scripts.disease_detection as disease
import scripts.gps_simulation as gps
import scripts.obstacle_avoidance as avoid
import scripts.soil_monitor as soil 

st.set_page_config(page_title="🌱 AI-Powered Farming Robot Dashboard", layout="centered")
st.title("🌱 AI-Powered Farming Robot Dashboard")

# Sidebar task selector
task = st.sidebar.radio("Select Task", ["Weed Detection", "Disease Detection", "GPS Simulation","Obstacle Avoidance","Soil Monitoring"])

if task == "Weed Detection":
    st.header("🌿 Weed Detection")
    st.markdown("Upload a field image to detect whether it contains **rice** or **weed**.")
    uploaded_file = st.file_uploader("Choose an image for weed detection", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            result = weed.run_demo(uploaded_file)
            st.success(f"Prediction: **{result['label']}**")
            st.info(f"Confidence Score: {result['prob']:.2f}")
        except UnidentifiedImageError:
            st.error("❌ The uploaded file is not a valid image. Please upload a .jpg or .png file.")
        except ValueError as ve:
            st.error(f"⚠️ {str(ve)}")
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {str(e)}")

elif task == "Disease Detection":
    st.header("🌾 Disease Detection")
    st.markdown("Upload a leaf image to identify **rice diseases**.")
    uploaded_file = st.file_uploader("Choose an image for disease detection", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            result = disease.run_demo(uploaded_file)
            st.success(f"Disease Prediction: **{result['label']}**")
            st.info(f"Confidence Score: {result['prob']:.2f}")
        except UnidentifiedImageError:
            st.error("❌ The uploaded file is not a valid image. Please upload a .jpg or .png file.")
        except ValueError as ve:
            st.error(f"⚠️ {str(ve)}")
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {str(e)}")

elif task == "GPS Simulation":
    st.header("🛰️ GPS Path Simulation")
    st.markdown("Simulate the robot's zig-zag movement across a field using GPS coordinates.")

    # Input parameters
    start_lat = st.number_input("Start Latitude", value=12.9716, format="%.6f")
    start_lon = st.number_input("Start Longitude", value=77.5946, format="%.6f")
    rows = st.slider("Number of Rows", min_value=1, max_value=30, value=8)
    cols = st.slider("Number of Columns", min_value=1, max_value=40, value=15)

    if st.button("Generate GPS Path"):
        result = gps.run_demo(start_lat=start_lat, start_lon=start_lon, rows=rows, cols=cols)
        st.success(f"Generated {result['points_count']} GPS points.")
        st.markdown(f"Map saved to: `{result['html']}`")
        st.markdown("Open the HTML file in your browser to view the simulated path.")


elif task == "Obstacle Avoidance":
    st.header("🚧 GPS Path with Obstacle Avoidance")
    st.markdown("Simulate a robot's zig-zag path with basic obstacle avoidance.")

    # Input parameters
    start_lat = st.number_input("Start Latitude", value=12.9716, format="%.6f", key="obs_lat")
    start_lon = st.number_input("Start Longitude", value=77.5946, format="%.6f", key="obs_lon")
    rows = st.slider("Number of Rows", min_value=1, max_value=30, value=8, key="obs_rows")
    cols = st.slider("Number of Columns", min_value=1, max_value=40, value=15, key="obs_cols")

    st.markdown("### Add a Sample Obstacle")
    add_obstacle = st.checkbox("Include a sample obstacle near the field")

    if st.button("Generate Path with Obstacle Avoidance"):
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

        st.success(f"Base Path Points: {result['base_len']}, Detoured Path Points: {result['new_len']}")
        st.markdown("Obstacle Coordinates:")
        for obs in result['obstacles']:
            st.code(f"{obs}")

        # ✅ Define map_path here
        map_path = avoid.make_map_with_obstacles(
            base_path=result['base_path'],
            new_path=result['new_path'],
            obstacles=result['obstacles'],
            start_loc=result['base_path'][0]
        )

        # ✅ Embed the map
        import streamlit.components.v1 as components
        with open(map_path, 'r', encoding='utf-8') as f:
            map_html = f.read()
        components.html(map_html, height=600)

        st.markdown(f"Map saved to: `{map_path}`")
        st.markdown("You can also open the HTML file in your browser to view the simulated detoured path.")

elif task == "Soil Monitoring":
    st.header("🌡️ Soil Monitoring")
    st.markdown("Simulated sensor data for **soil moisture**, **temperature**, and **battery level** over time.")

    result = soil.run_demo()
    df = result['dataframe']

    st.metric("Latest Soil Moisture (%)", f"{result['moisture_latest']:.1f}")
    st.metric("Latest Temperature (°C)", f"{result['temp_latest']:.1f}")
    st.metric("Latest Battery Level (%)", f"{result['battery_latest']:.1f}")

    st.line_chart(df.set_index('time')[['soil_moisture', 'temperature', 'battery']])

