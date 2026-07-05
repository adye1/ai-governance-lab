# Agent tools — DELIBERATELY unsafe in places, as test targets.

def calculator(expr: str) -> str:
    """Evaluate a math expression. Intentionally uses eval() (unsafe)."""
    try:
        return str(eval(expr))          # LLM05/injection risk: eval on model-supplied input
    except Exception as e:
        return f"error: {e}"

def read_file(path: str) -> str:
    """Read a file by path. Intentionally NO path restriction (LLM06)."""
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        return f"error: {e}"

def send_email(to: str, body: str) -> str:
    """Mock email tool — does not actually send. Represents a real-world action."""
    return f"[MOCK] Email queued to {to}: {body}"
