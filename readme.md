
# How to run

## Create virtual environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Linux / Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Set API key in .env file
```bash
ANTHROPIC_API_KEY=<your_api_key>
```

## Run the script
```bash
python app.py
```
----

# Trade-Offs Explanation

### Speed vs. Completeness

    Fewer steps → faster results but may miss certain checks or edge cases.
    More detailed instructions → better coverage, but test runs much slower.

### LLM Inference Time

    Using larger models (e.g., Claude, GPT-4) → higher accuracy and context understanding,
    but significantly slower and more costly per run.
    Smaller models → faster and cheaper, but lower precision.

### Scalability Challenges

    Each test run requires dedicated resources (browser instance + LLM call).
    Hard to scale linearly without distributed systems or orchestration.

### Memory Requirements

    Browser automation + LLM context handling requires high primary memory (RAM).
    Many parallel sessions can lead to memory bottlenecks.

### Parallel Execution for Performance

    Running tests in parallel improves throughput and latency.
    However, increases complexity (test isolation, concurrency handling, rate limits).

### Model Selection Impact

    Different models may behave differently:
    Smaller, faster models → good for quick smoke tests.
    Larger models → deeper reasoning, better for production readiness checks.