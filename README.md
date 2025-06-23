This package enables seamless integration of LiteLLM-compatible language models into LlamaIndex, making it easy to test and use any LLM supported by the LiteLLM or NRP API in your LlamaIndex workflows.


## Basic Example
```python
from sdsc_llama_index import SDSC

llm = SDSC(model="llama3-sdsc", api_key=api_key)
resp = llm.complete("Paul Graham is ")
print(resp)
``` 
