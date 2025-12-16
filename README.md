# Local AI Agent (Agno + Ollama + FastAPI + uv)
Author: Hitesh Agrawal

This project is a **fully local AI agent** with **no API keys** using:

- Ollama (local LLM)
- Agno (agent framework)
- DuckDuckGo (search)
- yfinance (stock market data)
- FastAPI (interactive API)
- **uv** (fast, reproducible Python environment manager)

---

## 1. System Requirements

- macOS or Linux
- Python **>= 3.11 and < 3.14**
- Ollama installed and running
- uv installed

---

## 2. Install Ollama

```bash
brew install ollama
# or Linux
curl -fsSL https://ollama.com/install.sh | sh

#then on macos
brew services start ollama
==> Successfully started `ollama` (label: homebrew.mxcl.ollama)

```

Pull a model:
```bash
ollama pull llama3.1
#pulling manifest
#pulling 667b0c1932bc:  93% ▕████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████          ▏ 4.6 GB/4.9 GB  5.7 MB/s     59s
ollama serve
```

Verify:
```bash
ollama list
NAME               ID              SIZE      MODIFIED
llama3.1:latest    46e0c10c039e    4.9 GB    38 seconds ago

ollama run llama3.1 "hello"
Hello! How are you today? Is there something I can help you with or would you like to chat?

or 
ollama run phi3:mini ## If you have less memory
```

---

## 3. Install uv

```bash
brew install uv
✔︎ JSON API cask.jws.json                                                                                                                                                       [Downloaded   15.1MB/ 15.1MB]
✔︎ JSON API formula.jws.json                                                                                                                                                    [Downloaded   32.1MB/ 32.1MB]
Warning: uv 0.9.17 is already installed and up-to-date.
To reinstall 0.9.17, run:
  brew reinstall uv
# or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 4. Setup Python Environment (uv)

From the project root:

```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
```

Install dependencies (locked):
```bash
uv add agno fastapi uvicorn duckduckgo-search yfinance pandas
```

---

## 5. Run the Agent (FastAPI)

```bash
uv run uvicorn app:app --reload
```

Open Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 6. Example Queries

- What is QUIC protocol and why is it faster?
- Get stock price of AAPL
- Search latest news on Nvidia and summarize

---

## 7. Project Structure

```
local-ai-agent-uv/
├── pyproject.toml
├── uv.lock
├── app.py
├── agent.py
├── tools/
│   ├── search.py
│   └── finance.py
└── README.md
```

---

## 8. Notes

- No API keys required
- Runs fully locally
- uv.lock ensures reproducible installs
- Python version compatibility is enforced

---

## 9. Recommended Python Versions

- ✅ 3.12.x (recommended)
- ✅ 3.11.x
- ❌ 3.14.x (experimental, not guaranteed)

---

## 10. Sample Run Outputs


```bash
curl -N -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello, how are you?"}'
{"response":{"run_id":"4177f4da-47aa-4b83-9f53-f8a2d5914975","agent_id":"local-research-&-finance-agent","agent_name":"Local Research & Finance Agent","session_id":"bf6c2b55-674c-472f-8e62-6a1316d93162","parent_run_id":null,"workflow_id":null,"user_id":null,"input":{"input_content":"Hello, how are you?","images":null,"videos":null,"audios":null,"files":null},"content":"No function call is needed for this question.","content_type":"str","reasoning_content":null,"reasoning_steps":null,"reasoning_messages":null,"model_provider_data":null,"model":"llama3.1","model_provider":"Ollama","messages":[{"id":"229ef1b6-964c-441f-befe-2e7f2e928e51","role":"system","content":"<instructions>\n\n    Decide quickly.\n    If the question is about stock price, call get_stock_price immediately.\n    \n</instructions>\n\n<additional_information>\n- Use markdown to format your answers.\n</additional_information>","compressed_content":null,"name":null,"tool_call_id":null,"tool_calls":null,"audio":null,"images":null,"videos":null,"files":null,"audio_output":null,"image_output":null,"video_output":null,"file_output":null,"redacted_reasoning_content":null,"provider_data":null,"citations":null,"reasoning_content":null,"tool_name":null,"tool_args":null,"tool_call_error":null,"stop_after_tool_call":false,"add_to_agent_memory":true,"from_history":false,"metrics":{"input_tokens":0,"output_tokens":0,"total_tokens":0,"audio_input_tokens":0,"audio_output_tokens":0,"audio_total_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0,"reasoning_tokens":0,"timer":null,"time_to_first_token":null,"duration":null,"provider_metrics":null,"additional_metrics":null},"references":null,"created_at":1765862628,"temporary":false},{"id":"1397ebed-eba8-4252-82e9-0c8218fd8f12","role":"user","content":"Hello, how are you?","compressed_content":null,"name":null,"tool_call_id":null,"tool_calls":null,"audio":null,"images":null,"videos":null,"files":null,"audio_output":null,"image_output":null,"video_output":null,"file_output":null,"redacted_reasoning_content":null,"provider_data":null,"citations":null,"reasoning_content":null,"tool_name":null,"tool_args":null,"tool_call_error":null,"stop_after_tool_call":false,"add_to_agent_memory":true,"from_history":false,"metrics":{"input_tokens":0,"output_tokens":0,"total_tokens":0,"audio_input_tokens":0,"audio_output_tokens":0,"audio_total_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0,"reasoning_tokens":0,"timer":null,"time_to_first_token":null,"duration":null,"provider_metrics":null,"additional_metrics":null},"references":null,"created_at":1765862628,"temporary":false},{"id":"e366e152-3971-4311-850c-f2684690fdc6","role":"assistant","content":"No function call is needed for this question.","compressed_content":null,"name":null,"tool_call_id":null,"tool_calls":null,"audio":null,"images":null,"videos":null,"files":null,"audio_output":null,"image_output":null,"video_output":null,"file_output":null,"redacted_reasoning_content":null,"provider_data":null,"citations":null,"reasoning_content":null,"tool_name":null,"tool_args":null,"tool_call_error":null,"stop_after_tool_call":false,"add_to_agent_memory":true,"from_history":false,"metrics":{"input_tokens":232,"output_tokens":10,"total_tokens":242,"audio_input_tokens":0,"audio_output_tokens":0,"audio_total_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0,"reasoning_tokens":0,"timer":null,"time_to_first_token":null,"duration":null,"provider_metrics":null,"additional_metrics":null},"references":null,"created_at":1765862628,"temporary":false}],"metrics":{"input_tokens":232,"output_tokens":10,"total_tokens":242,"audio_input_tokens":0,"audio_output_tokens":0,"audio_total_tokens":0,"cache_read_tokens":0,"cache_write_tokens":0,"reasoning_tokens":0,"timer":{"start_time":1795.673326729,"end_time":1968.979878043,"elapsed_time":173.306551314},"time_to_first_token":0.00604343599979984,"duration":173.306551314,"provider_metrics":null,"additional_metrics":null},"additional_input":null,"tools":[],"images":null,"videos":null,"audio":null,"files":null,"response_audio":null,"citations":null,"references":null,"metadata":null,"session_state":{"current_session_id":"bf6c2b55-674c-472f-8e62-6a1316d93162","current_run_id":"4177f4da-47aa-4b83-9f53-f8a2d5914975"},"created_at":1765862622,"events":null,"status":"COMPLETED","requirements":null,"workflow_step_id":null}}%
```

```bash
curl -N -X POST http://127.0.0.1:8000/stream_query \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello, how are you?"}'
There is no function call required for this question.

(Note: If the response is too short or does not contain any functions to be called, it will be skipped)%
```

```bash
curl -N -X POST http://127.0.0.1:8000/stream_query \
  -H "Content-Type: application/json" \
  -d '{"prompt":"What is AAPL stock price?"}'
I've called the `get_stock_price` tool to retrieve the current stock price of AAPL.

To format my answer correctly, I will use markdown formatting as instructed.

AAPL Price: **274.11** USD
Day High: **280.05**
Day Low: **272.84**

Please note that these values are not actual stock prices and are used for demonstration purposes only.
```

---
## 11. Stop locally running Ollama agent

```bash
brew services stop ollama
```