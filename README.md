
# WhatsApp Chat Analyzer![Screenshot 2024-08-03 205619](https://github.com/user-attachments/assets/e1704d39-8ef1-481b-8a60-91713bbb3388)


A tool for analyzing WhatsApp chat data. This project allows you to upload and analyze chat exports, providing insights into chat activity, user interactions, and more. 

## Project Overview

The WhatsApp Chat Analyzer provides several functionalities to explore and visualize WhatsApp chat data:

### Features

- **Upload and Preprocess Chat Data**: Upload a WhatsApp chat export file, which is then processed to extract relevant information.
- **Statistics Analysis**: Get key statistics such as total messages, words, media shared, and links shared.
- **Timeline Analysis**: Visualize chat activity over time with monthly and daily timelines.
- **Activity Map**: View charts depicting activity by day and month.
- **Heatmap**: Analyze user activity by day and period with a heatmap.
- **User Comparison**: Compare activity among different users in group chats.
- **Word Cloud**: Generate a word cloud to visualize the most common words used in the chat.
- **Most Common Words**: Display a bar chart of the most frequently used words.
- **Emoji Analysis**: Break down the usage of emojis in the chat.

## Project Components

### Streamlit App (`app.py`)

The Streamlit app provides a web interface for:
- Uploading chat files.
- Displaying analyses and visualizations.

### Preprocessing (`preprocessor.py`)

Handles:
- Cleaning and transforming raw chat data into a structured format suitable for analysis.

### Helper Functions (`helper.py`)

Includes functions to:
- Compute statistics.
- Generate visualizations.
- Perform various analyses on the chat data.

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App**

   ```bash
   streamlit run app.py
   ```

6. **Open the App in Your Browser**

   After running the command, the app should open in your default web browser. If not, you can navigate to `http://localhost:8501` to view it.

## Usage

1. **Upload a WhatsApp Chat File**: Use the sidebar to choose and upload a file exported from WhatsApp.
2. **Select Analysis Options**: Choose the user for whom you want to view statistics and analyses.
3. **Explore Visualizations**: Use the provided visualizations to gain insights into chat activity, word usage, emoji distribution, and more.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**: Create a personal copy of the project on GitHub.
2. **Make Changes**: Implement features or fix bugs.
3. **Submit a Pull Request**: Share your changes for review and integration.



## Acknowledgments
![Screenshot 2024-08-0![Screenshot 2024-08-03 211917](https://github.com/user-attachments/assets/e9daefa7-7cdc-4f84-8b0b-e3b5fe9c16cd)
3 205619](https://github.com/user-attachments/assets/8436684d-56e0-4039-a046-6c7e618![Screenshot 2024-08-03 211800](https://github.com/user-attachments/assets/7966098a-d3a7-4d62-8275-49b752ddfe99)
94176)

- [Streamlit](h![Screenshot 2024-08-03 212018](https://github.com/user-attachments/assets/a22903a6-d385-48a0-af05-e04fd0c374ea)
ttp![Screenshot 2024-08-03 211740](https://github.com/user-att![Screenshot 2024-08-03 211957](https://github.com/user-attachments/assets/b20707b0-ffcd-4890-8491-c12e7096d19e)
achments/assets/5305d9cf-a77b-4071-8a18-dbfb4f7baaa0)
s://streamlit.io/) for the easy-to-use web framework.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for data visualization.
- [WordCloud](https://github.com/amueller/word_cloud) for generating word clouds.
- [Emoji](https://github.com/carpedm20/emoji) for emoji analysis.

