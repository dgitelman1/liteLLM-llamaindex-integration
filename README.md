```python
from sdsc_llama_index import SDSC

llm = SDSC(model="llama3-sdsc", api_key=api_key)
resp = llm.complete("Paul Graham is ")
print(resp)
``` 
