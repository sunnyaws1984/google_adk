# Flight Search Agent using Google ADK

This project demonstrates how to create basic AI agent using Google's Agent Development Kit (ADK) that can help users find direct flights between cities. The agent uses Google Search to find flight information and provides intelligent responses to user queries.

## Features

- **Direct Flight Search**: Find direct flights between any two cities
- **Flight Information**: Get details about airlines, schedules, and pricing
- **Alternative Suggestions**: Receive suggestions for connecting flights when direct flights aren't available
- **Smart Query Processing**: Natural language understanding for flight requests

## Prerequisites

Before you begin, make sure you have:

1. **Python 3.8+** installed on your system
2. **Google AI Studio API Key** - Get one from [Google AI Studio](https://aistudio.google.com/apikey)
3. **Basic knowledge** of Python and command line operations

## Installation

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/dev-muhammad/flight_search_agent_adk.git
cd flight_search_agent_adk
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv flight_agent_env

# Activate virtual environment
# On macOS/Linux:
source flight_agent_env/bin/activate

# On Windows:
flight_agent_env\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Copy the example environment file and configure your API key:

```bash
cp .env.example .env
```

Get your Google AI API key from [Google AI Studio](https://aistudio.google.com/apikey) and update the `.env` file:

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

### Basic Usage

1. **Start the Agent with builtin WebUI**:

   ```bash
   adk web
   ```

2. **Interact with the Agent**:
   Once running, open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. You can ask questions like:
   - "Find direct flights from New York to London"
   - "Are there any direct flights between Tokyo and Paris?"
   - "Show me flight options from Los Angeles to Dubai"
   - "What airlines fly direct from Mumbai to Singapore?"