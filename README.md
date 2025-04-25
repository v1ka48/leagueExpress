# Fantasy League Weekly Video Summary Generator

![Project Banner](https://your-project-banner-url.com/banner.png)

## 📈 Project Overview

**Fantasy League Weekly Video Summary Generator** is an automated Python-based tool designed to create humorous and engaging video summaries of your Yahoo Fantasy Sports league's weekly performance. Leveraging Yahoo's Fantasy Sports API and Synthesia's AI video generation capabilities, this tool provides personalized video updates featuring a virtual sports commentator avatar. Whether you're competing with friends, coworkers, or other enthusiasts, this tool adds a fun and dynamic twist to your fantasy league updates, keeping all members entertained and engaged.

## 🛠️ Features

1. **Connect to Yahoo Fantasy League Data**
   - **Data Retrieval**: Fetches weekly performance data from Yahoo Fantasy Sports via their API, including scores, rankings, trades, and more.
   - **Upcoming Matchups**: Retrieves data about upcoming games and matchups for the next week.

2. **Generate the Video Script**
   - **AI-Powered Script Generation**: Utilizes OpenAI's GPT-3.5 Turbo to create a funny and engaging script summarizing the week's performance.
   - **Humorous Content**: Includes jokes, banter, and playful commentary such as roasting the lowest-scoring team or hyping the top performers.
   - **Next Week's Insights**: Discusses upcoming matchups with predictions and playful trash talk.

3. **Create the Video**
   - **Synthesia Integration**: Uses Synthesia's API to convert the generated script into a video.
   - **AI Avatar Customization**: Features an AI avatar designed to look like a sports caster or athlete, delivering the script with natural speech, humor, and expression.
   - **Future Enhancements**: Plans to add visuals like team logos, scores, or funny memes to the video.

4. **Automate the Workflow**
   - **Backend System**: Allows users to connect their Yahoo Fantasy League to the platform.
   - **Automated Video Generation**: Generates and delivers personalized video summaries to users every week automatically.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 📋 Prerequisites

- **Operating System**: macOS
- **Python**: Version 3.7 or higher
- **Git**: For version control
- **API Access**:
  - **Yahoo Fantasy Sports API**: Obtain API keys by [registering your application](https://developer.yahoo.com/fantasysports/guide/)
  - **OpenAI API**: Sign up at [OpenAI](https://beta.openai.com/signup/) and obtain your API key.
  - **Synthesia API**: Sign up at [Synthesia](https://www.synthesia.io/) and obtain your API key.

### 🔧 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/fantasy-league-summary.git
   cd leagueExpress