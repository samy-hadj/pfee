# PFEE

## Setup Instructions

### 1. Create a `.env` File

You need to create a `.env` file in the project root directory to store your OpenAI API key. The file should contain the following line:

```
OPENAI_API_KEY=XXXXXX
```

Replace `XXXXXX` with your actual OpenAI API key.

### 2. Set Up Your Environment

To set up your Python environment, follow these steps:

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate  # For macOS/Linux
# env\Scripts\activate  # For Windows

# Install the required packages
pip install -r requirements.txt
```

### 3. Run the App

Once your environment is set up, you can run the application using Streamlit:

```bash
streamlit run main.py
```

### 4. Requirements

You can generate the `requirements.txt` file after installing the necessary packages using:

```bash
pip freeze > requirements.txt
```

## Project Structure

```
.
├── data/
├── env
├── main.py
├── README.md
└── requirements.txt
```

Make sure to keep the structure intact for the application to work properly.


---

PFEE TEAM