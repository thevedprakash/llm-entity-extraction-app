from vllm import LLM
from vllm import SamplingParams

def load_vllm_model():
    """
    Load vLLM model with pre-defined configuration.
    """
    model = LLM(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        dtype="float16",
        tensor_parallel_size=4,
        gpu_memory_utilization=0.6,
        tokenizer_mode="mistral",
        enforce_eager=True,
    )
    return model


# Sampling Parameters
sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=300,
    top_p=0.95
)
