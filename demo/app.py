import spaces
import gradio as gr
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import (
    StorageContext,
    load_index_from_storage, Settings, PromptHelper
)
from llama_index.core.indices.vector_store import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SentenceTransformerRerank, SimilarityPostprocessor
from llama_index.llms.huggingface import HuggingFaceLLM
import torch
PERSIST_DIR = './storage'

# Configure the settings
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5", device="cpu")

Settings.llm = HuggingFaceLLM(
    model_name="meta-llama/Meta-Llama-3-8B-Instruct",
    tokenizer_name="meta-llama/Meta-Llama-3-8B-Instruct",
    context_window=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "top_k": 50, "top_p": 0.95},
    device_map="auto",
)

storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index = load_index_from_storage(storage_context)

# prompt_helper = PromptHelper(
#     context_window=4096,
#     num_output=512,
#     chunk_overlap_ratio=0.1,
#     chunk_size_limit=None
# )

# retriever = VectorIndexRetriever(
#     index=index,
#     similarity_top_k=5,
# )

# query_engine = RetrieverQueryEngine.from_args(
#     retriever,
#     node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],
#     prompt_helper=prompt_helper
# )

rerank = SentenceTransformerRerank(
    model="BAAI/bge-reranker-large", top_n=5  # Note here
)
query_engine = index.as_query_engine(streaming=True, similarity_top_k=1, node_postprocessors=[rerank])


# def chatbot_response(message, history):
#     # Add a custom prompt template
#     prompt = f"Based on the Elder Scrolls lore, please answer the following question:\n\n{message}\n\nAnswer:"
#     response = query_engine.query(prompt)
#     return str(response)


@spaces.GPU
def chatbot_response(message, history):
    response = query_engine.query(message)
    return str(response)

iface = gr.ChatInterface(
    fn=chatbot_response,
    title="UESP Lore Chatbot: Running on top of Meta-Llama-3-8B-Instruct (currently) It works 'okay'",
    description="Github page for use case, general information, local installs, etc: https://github.com/kartoffels1234/UESP-lore",
    examples=["Who is Zaraphus?", "What is the relation between Vivec and Chim?", "What is the Lunar Lorkhan?"],
    cache_examples=True,
)

if __name__ == "__main__":
    iface.launch()
