CHAT_MODELS  = {
    "gemma3",
    "llama3",
    "llama3-sdsc",
    "DeepSeek-R1-Distill-Qwen-32B",
    "gorilla",
    "llava-onevision",
    "olmo",
    "phi3"
    
}

FUNCTION_CALLING_MODELS = {
    "llama3-sdsc",
    "gorilla"
}

CONTEXT_WINDOWS = {
    'gemma3': 128000,
    'llama3': 128000,
    'llama3-sdsc': 128000,
    'DeepSeek-R1-Distill-Qwen-32B': 131072,
    'gorilla': 16000,
    'llava-onevision': 64000,
    'olmo': 32000,
    'phi3': 128000
     
}


def is_chat_model(model: str) -> bool:
    return model in CHAT_MODELS

def is_function_calling_model(model: str) -> bool:
    return model in FUNCTION_CALLING_MODELS

def get_context_window(model: str) -> int:
    if model not in CONTEXT_WINDOWS:
        raise ValueError("Model is not valid.")
    return CONTEXT_WINDOWS[model]