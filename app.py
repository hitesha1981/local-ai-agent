from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from agno.run.agent import RunEvent
from pydantic import BaseModel
import time

from agent import agent

app = FastAPI(title="Local AI Agent")

class Query(BaseModel):
    prompt: str

@app.post("/query")
def run_agent(query: Query):
    response = agent.run(query.prompt)
    return {"response": response}

def stream_generator(prompt: str):
    """
    Generates response chunks by running the Agno agent in streaming mode.
    """
    # The 'stream=True' flag tells Agno to yield events incrementally
    stream = agent.run(prompt, stream=True)
    
    for chunk in stream:
        # Agno yields different event types (tool_call, content, etc.)
        # We only want to stream the final textual content chunks to the client.
        if chunk.event == RunEvent.run_content:
            yield chunk.content
        # Optional: You could add logic here to yield messages about tool use
        # elif chunk.event == RunEvent.tool_call_start:
        #     yield f"\n[Agent using tool: {chunk.tool_call.name}]\n"

@app.post("/stream_query")
def stream_query(query: Query):
    """
    Endpoint to handle streaming queries to the agent.
    """
    return StreamingResponse(stream_generator(query.prompt), media_type="text/plain")