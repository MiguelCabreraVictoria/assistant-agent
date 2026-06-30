# prompts/registry.py
from observability.langfuse_client import get_langfuse


class PromptRegistry:

    def __init__(self):
        self._cache = {}

    def get(self, name: str, label: str = "production"):
        key = f"{name}:{label}"

        if key in self._cache:
            return self._cache[key]

        client = get_langfuse()

        prompt_obj = client.get_prompt(name=name, label=label)

        self._cache[key] = prompt_obj.prompt

        return prompt_obj.prompt


prompt_registry = PromptRegistry()