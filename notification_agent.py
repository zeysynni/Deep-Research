import os

from agents import Agent, function_tool
import requests


@function_tool
def push_notification(text: str):
    """Send a push notification using Pushover API."""
    data = {"token": os.environ.get('PUSHOVER_TOKEN'), "user": os.environ.get('PUSHOVER_USER'), "message": text}
    requests.post("https://api.pushover.net/1/messages.json", data=data, timeout=10)

INSTRUCTIONS = """You are able to send a nicely formatted summary based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one push up notification, providing the 
report converted into clean, well structured text with an appropriate subject line."""

notification_agent = Agent(
    name="Notification agent",
    instructions=INSTRUCTIONS,
    tools=[push_notification],
    model="gpt-4o-mini",
)
