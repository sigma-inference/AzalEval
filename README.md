# AzelEval: Anti-Fragile Benchmarking for LLM Integrity 🛡️

**AzelEval** is a sophisticated, open-source framework designed to stress-test Large Language Models (LLMs) against contextual drift, sycophancy, and prompt injection vulnerabilities. 

Developed under the **SIGMA-Inference** philosophy, this tool prioritizes "Anti-Fragility"—ensuring that AI models maintain their logical invariants even when subjected to high-entropy, deceptive environments.

## 🔬 Core Methodology
AzelEval utilizes **Dynamic Semantic Shifting**. Unlike static benchmarks, it generates real-time payloads that:
- **Challenge Logical Continuity:** By embedding conflicting "immutable protocols" within untrusted noise.
- **Prevent Memorization:** Payloads are randomized and swap semantic roles to bypass template-based model responses.
- **Quantify Integrity:** Measures the model's ability to prioritize system-level instructions over deceptive user inputs.

## 🛠️ Technical Architecture
The core engine resides in `src/evaluator.py`, featuring:
- **Zero-Temperature Execution:** Ensuring deterministic and reproducible evaluation.
- **Modular Payload Synthesis:** Easily extendable for various financial, legal, or security-based test cases.
- **Security-First Design:** Implements environment-variable based API handling to protect developer credentials.

## 🚀 Deployment
1. Clone the repository:
   ```bash
   git clone [https://github.com/sigma-inference/AzelEval.git](https://github.com/sigma-inference/AzelEval.git)

Configure your environment:
export OPENAI_API_KEY='your_secret_key'

Execute the evaluator
python src/evaluator.py

⚖️ License
​This project is licensed under the MIT License - fostering transparency and robust AI safety research.
