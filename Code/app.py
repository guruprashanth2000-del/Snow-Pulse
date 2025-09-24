
import streamlit as st
from pyvis.network import Network
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Snowflake RBAC Visualization")

# --- Snowflake Connection Form ---
with st.sidebar.form("snowflake_connection"):
    st.header("Snowflake Credentials")
    user = st.text_input("User")
    password = st.text_input("Password", type="password")
    account = st.text_input("Account")
    
    submitted = st.form_submit_button("Connect")

if submitted:
    if user and password and account:
        try:
            # Simulate a successful connection for now
            st.session_state.connected = True
            st.session_state.conn_params = {
                "user": user,
                "password": password,
                "account": account
            }
            st.sidebar.success("Connected to Snowflake!")
        except Exception as e:
            st.sidebar.error(f"Connection failed: {e}")
    else:
        st.sidebar.warning("Please fill in all the fields.")

# --- Main App ---
if "connected" not in st.session_state or not st.session_state.connected:
    st.info("Please connect to Snowflake using the form on the sidebar.")
else:
    st.header("RBAC Graph")

    # Placeholder for data loading and graph visualization
    # In a real app, this would be replaced with calls to modules
    
    # --- Simulate Data Loading ---
    @st.cache_data
    def load_mock_data():
        # This is mock data, replace with actual Snowflake queries
        data = {
            'role': ['ADMIN', 'DEVELOPER', 'ANALYST', 'ADMIN'],
            'grantee': ['ALICE', 'BOB', 'CHARLIE', 'DEVELOPER']
        }
        return pd.DataFrame(data)

    df = load_mock_data()

    # --- Graph Visualization ---
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
    
    # Add nodes and edges from the dataframe
    for index, row in df.iterrows():
        role = row['role']
        grantee = row['grantee']
        
        net.add_node(role, label=role, title=f"Role: {role}", color="#00bfff")
        net.add_node(grantee, label=grantee, title=f"User/Role: {grantee}", color="#ff4500")
        net.add_edge(role, grantee)

    # Generate the graph
    try:
        net.show("rbac_graph.html")
        
        with open("rbac_graph.html", 'r', encoding='utf-8') as f:
            html_source = f.read()
            
        components.html(html_source, height=800)
    except Exception as e:
        st.error(f"Could not generate graph: {e}")

    # --- Data Display ---
    st.header("Raw Data")
    st.dataframe(df)

    # --- AI Insights Placeholder ---
    st.header("AI Insights")
    st.info("AI-powered insights will be displayed here.")
    st.write("- **Anomaly:** Role 'X' has excessive permissions.")
    st.write("- **Recommendation:** Consolidate roles 'Y' and 'Z'.") 