import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for green and black theme and header/footer styling
st.markdown("""
    <style>
    body {
        background-color: #e5e5e5;
        color: #25D366;
    }
    .stButton>button {
        background-color: #25D366;
        color: white;
    }
    .stSidebar .stButton>button {
        background-color: #25D366;
        color: white;
    }
    .stSidebar .stFileUploader>label {
        color: #25D366;
    }
    .stTitle {
        color: #128C7E;
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #25D366;
        color: white;
    }
    .header img {
        height: 50px;
    }
    .header h1 {
        margin: 0;
        font-size: 24px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #25D366;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp Logo">
        <h1>WhatsApp Chat Analyzer</h1>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("WhatsApp Chat Analyzer")
st.sidebar.markdown("""
    Welcome to the WhatsApp Chat Analyzer! 📊
    
    Upload your exported WhatsApp chat file to get started. The app provides insights into your chat data including:
    - Key statistics
    - Activity timelines
    - Word clouds
    - Emoji analysis
    - And much more!
""")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis for", user_list)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("📈 Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(label="Total Messages", value=num_messages)
        with col2:
            st.metric(label="Total Words", value=words)
        with col3:
            st.metric(label="Media Shared", value=num_media_messages)
        with col4:
            st.metric(label="Links Shared", value=num_links)

        # Monthly Timeline
        st.title("📅 Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(timeline['time'], timeline['message'], color='green', marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Month-Year")
        plt.ylabel("Messages")
        plt.grid(True)
        st.pyplot(fig)

        # Daily Timeline
        st.title("📆 Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black', marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Messages")
        plt.grid(True)
        st.pyplot(fig)

        # Activity Map
        st.title('📊 Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation=45)
            plt.xlabel("Day")
            plt.ylabel("Messages")
            plt.grid(axis='y')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation=45)
            plt.xlabel("Month")
            plt.ylabel("Messages")
            plt.grid(axis='y')
            st.pyplot(fig)

        st.title("🗓 Weekly Activity Heatmap")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax = sns.heatmap(user_heatmap, cmap="YlGnBu", annot=True, fmt=".1f", linewidths=.5)
        plt.xlabel("Period")
        plt.ylabel("Day")
        st.pyplot(fig)

        # Group-level Analysis
        if selected_user == 'Overall':
            st.title('👥 Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation=45)
                plt.xlabel("User")
                plt.ylabel("Messages")
                plt.grid(axis='y')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # Word Cloud
        st.title("🌟 Word Cloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(df_wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Most Common Words
        st.title('🔠 Most Common Words')
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(most_common_df[0], most_common_df[1], color='teal')
        plt.xlabel("Count")
        plt.ylabel("Words")
        plt.grid(axis='x')
        st.pyplot(fig)

        # Emoji Analysis
        st.title("😊 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f%%", startangle=140)
            plt.axis('equal')
            st.pyplot(fig)

else:
    st.title("WhatsApp Chat Analyzer")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg", width=200)
    st.markdown("""
        Welcome to the WhatsApp Chat Analyzer! 📊
        
        This tool allows you to upload your WhatsApp chat export file and gain insightful analytics on your conversations. 
        Use the sidebar to upload your chat file and start exploring your chat data.
        
        ### Features
        - **Key Statistics**: Total messages, words, media shared, and links shared.
        - **Activity Timelines**: Monthly and daily chat activity.
        - **Activity Maps**: Charts of activity by day and month.
        - **Heatmaps**: User activity by day and period.
        - **User Comparison**: Compare activity among different users in group chats.
        - **Word Cloud**: Visualize the most common words.
        - **Emoji Analysis**: Breakdown of emoji usage in the chat.
        
        **Get started by uploading your WhatsApp chat file from the sidebar!**
    """)

# Footer
st.markdown("""
    <div class="footer">
        <p>Developed by Shreya Verma | © 2024 WhatsApp Chat Analyzer</p>
    </div>
    """, unsafe_allow_html=True)


