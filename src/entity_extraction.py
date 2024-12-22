from src.model_loader import sampling_params

def extract_entities(model, text, prompt):
    """
    Extract entities using the vLLM model with a given prompt.
    """
    formatted_prompt = prompt.format(text=text)
    outputs = model.generate(formatted_prompt, sampling_params)
    return outputs[0].outputs[0].text.strip()
