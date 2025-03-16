from langflow.load import run_flow_from_json
TWEAKS = {
  "TextInput-c3eEi": {
    "input_value": "question"
  },
  "TextInput-JaDbh": {
    "input_value": "profile"
  },
}

result = run_flow_from_json(flow="Ask AI.json",
                            input_value="message",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)