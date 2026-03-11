# Web UI

GeoAgent includes a Solara-based chat interface for interactive geospatial analysis with a persistent, interactive map.

## Quick Start

```bash
# Install UI dependencies
pip install "geoagent[ui]"

# Launch the UI
geoagent ui
```

Or run directly with Solara:

```bash
python -m solara run "$(python -c 'import geoagent.ui; print(geoagent.ui.PAGES_DIR)')"
```

If installed with `uv tool install`:

```bash
uv tool install "geoagent[ui]"
uv tool run --from geoagent python -m solara run \
  "$(uv tool run --from geoagent python -c 'import geoagent.ui; print(geoagent.ui.PAGES_DIR)')"
```

## Features

- **Persistent map** — layers accumulate across queries on the same interactive MapLibre map
- **Native widget rendering** — full bidirectional map interaction (zoom, pan, click)
- **Chat interface** — type natural language queries with real-time status updates
- **Provider selection** — switch between OpenAI, Anthropic, Google Gemini, or Ollama
- **OpenAI-compatible endpoint** — configure a custom base URL for any OpenAI-compatible API
- **Model selection** — choose from suggested models or enter a custom model name
- **Generated code** — toggle code display for transparency

## Using an OpenAI-Compatible Endpoint

GeoAgent UI supports any OpenAI-compatible API (e.g., a self-hosted gateway or a third-party
provider). Set the provider to **openai** and configure the base URL:

### Via environment variables (recommended)

```bash
export OPENAI_BASE_URL="https://your-openai-compatible-host/v1"
export OPENAI_API_KEY="your-api-key"
geoagent ui
```

Both `OPENAI_BASE_URL` and `OPENAI_API_BASE` are recognised; `OPENAI_BASE_URL` takes precedence.

### Via the UI

1. Launch the UI: `geoagent ui`
2. In the sidebar, select **Provider → openai**
3. A **Base URL** field appears — enter your endpoint, e.g.
   `https://your-openai-compatible-host/v1`
4. Select or type the model name (e.g. `qwen-coder-30b`)

## Selecting a Custom Model

Each provider has a list of suggested models in the **Model** dropdown. You can also
type any model name directly in the **Custom model name** field below the dropdowns.

Example models for an OpenAI-compatible endpoint:

| Model name | Description |
|---|---|
| `qwen-coder-30b` | Qwen Coder 30B |
| `glm-4.7-355b` | GLM 4.7 355B |

## Python API

You can also launch the UI programmatically:

```python
from geoagent.ui import launch_ui

launch_ui()
```

## Module Reference

::: geoagent.ui.launch_ui
