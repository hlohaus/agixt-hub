try:
    import anthropic
except ImportError:
    import sys
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "anthropic"])
    import anthropic


# List of models available at https://console.anthropic.com/docs/api/reference
class ClaudeProvider:
    def __init__(
        self,
        ANTHROPIC_API_KEY: str = "",
        MAX_TOKENS: int = 75000,
        AI_MODEL: str = "claude-2",
        AI_TEMPERATURE: float = 0.7,
        **kwargs,
    ):
        self.ANTHROPIC_API_KEY = ANTHROPIC_API_KEY
        self.MAX_TOKENS = MAX_TOKENS if MAX_TOKENS else 75000
        self.AI_MODEL = AI_MODEL if AI_MODEL else "claude-v1-100k"
        self.AI_TEMPERATURE = AI_TEMPERATURE if AI_TEMPERATURE else 0.7

    async def instruct(self, prompt):
        try:
            c = anthropic.Client(api_key=self.ANTHROPIC_API_KEY)
            return c.completion(
                prompt=f"{anthropic.HUMAN_PROMPT}{prompt}{anthropic.AI_PROMPT}",
                stop_sequences=[anthropic.HUMAN_PROMPT],
                model=self.AI_MODEL,
                temperature=float(self.AI_TEMPERATURE),
                max_tokens_to_sample=self.MAX_TOKENS,
            )
        except Exception as e:
            return f"Claude Error: {e}"
