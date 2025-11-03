from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPEN_MODEL_NAME"]="gpt-4-0125-preview"

llm=os.getenv("OPENAI_API_KEY")

## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video content for the topic{topic} from Yt channel',
    verbose=True,
    memory=True,
    backstory=(
    "Expert in understanding videos in AI Data Science, Machine Learning And GEN AI and providing detailed notes on the content."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_tool_creation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
)