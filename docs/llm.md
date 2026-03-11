# LLM Provider

Multi-provider LLM abstraction supporting OpenAI, Anthropic, Google Gemini, and Ollama.

## OpenAI-Compatible Endpoints

You can point GeoAgent at any OpenAI-compatible API by passing `base_url` when using
the `openai` provider:

```python
from geoagent import GeoAgent

agent = GeoAgent(
    provider="openai",
    model="qwen-coder-30b",
    base_url="https://your-openai-compatible-host/v1",
    api_key="your-key",  # or set OPENAI_API_KEY in env
)
```

Or set the environment variable before launching:

```bash
export OPENAI_BASE_URL="https://your-openai-compatible-host/v1"
export OPENAI_API_KEY="your-api-key"
```

`get_llm` forwards all extra `**kwargs` to `langchain_openai.ChatOpenAI`, so any
parameter accepted by `ChatOpenAI` (e.g. `base_url`, `default_headers`, `timeout`)
can be passed through:

```python
from geoagent.core.llm import get_llm

llm = get_llm(
    provider="openai",
    model="qwen-coder-30b",
    base_url="https://your-openai-compatible-host/v1",
)
```

::: geoagent.core.llm
