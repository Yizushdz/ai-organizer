# backend/main.py
from flask import Flask, request, jsonify
import os
import argparse
import sys
import json
from typing import List, Optional
from dotenv import load_dotenv
from datetime import datetime
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    HandoffOutputItem,
    ItemHelpers,
    MessageOutputItem,
    ToolCallItem,
    ToolCallOutputItem,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled
)
from tools import (
    execute_bash,
    glob_files,
    grep_files,
    list_directory,
    read_file,
    edit_file,
    write_file,
    web_search,
    web_fetch,
    reset_approvals
)
from safe_agent import SafeAgent

# create app instance
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
BASE_URL = os.getenv("OPENAI_API_BASE") or "https://api.openai.com/v1"
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME") or "gpt-4o"
if not API_KEY:
    raise ValueError("Please set OPENAI_API_KEY in your .env file")
# Create custom client with specified base URL
client = AsyncOpenAI(
    base_url=BASE_URL, 
    api_key=API_KEY,
)
# Set as default client and configure API method
set_default_openai_client(client=client, use_for_tracing=False)
set_default_openai_api("chat_completions")
set_tracing_disabled(disabled=True)


# Endpoint for /analyze
@app.route('/analyze', methods=['POST'])
def analyze_file():
    pass

if __name__ == '__main__':
    app.run(port=5000)