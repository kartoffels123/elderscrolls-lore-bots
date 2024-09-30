

# Elder Scrolls Lore Chatbot Project

This project explores the effectiveness of various implementations of vector indexes, embeddings, models, and dataset formatting over Elder Scrolls lore data. Initially based on the UESP wiki, the project has expanded to include the Imperial Library, focusing on using primary sources from the games, namely the books, to enable a chatbot that provides accurate and insightful responses.

## Goals:
1. Answer lore questions.
2. Connect documents.
3. Return books related to a topic.

## Project Structure:
- **chatgpt_assistant/**: Tools to help set up a ChatGPT assistant.
- **cleaning/**: Tools for cleaning and sorting articles into JSON format.
- **data/**: Cleaned and sorted articles as JSON.
- **demo/**: Hugging Faces demo using Meta-Llama-3-8B-Instruct. Use with "storage_bge-large-en-v1-5_Meta-Llama-3-8B-Instruct"
- **llama_index_bots/**: Tools to either run an existing llamaindex vector store or create your own from the data.
- **storage/**: Information about the llamaindex vector store.
- **old/**: Archive of old versions and files.
- **pictures/**: Visual assets related to the project.
- **venv/**: Virtual environment setup.

## Key Files:
- **LICENSE**: Project license information.
- **README.MD**: Project overview and instructions.
- **requirements.txt**: Bare minimum requirements to run the simplest programs.

## Data and Tools:
- **Data**: [Download here](https://www.mediafire.com/folder/wljfkqy6kxcpu/elderscrolls_lore_bot)
- **Information about datasets**: Detailed in the `data` directory.
- **Storage (llamaindex)**: Explained in the `storage` directory.
- **Subdirectory Requirements**: Each subdirectory (`cleaning`, `llama_index_bots`, `chatgpt_assistant`) contains specific requirements.

## Demo:
### Highest Performing Version:
#### ChatGPT-3.5-Turbo Assistant with a vector index of Imperial Library Master JSONs.

**User:** What are books related to Lorkhan?

**Lorebot:**
Here are some books related to Lorkhan that you may find interesting:

"The Lunar Lorkhan" by Fal Droon: This book explains how Tamriel's moons are the decaying body of Lorkhan[1].

"Sithis": This book explores the connection between Sithis and Lorkhan, detailing how Sithis sundered the nothing and mutated the parts, leading to a myriad of possibilities[2].

"Spirit of Nirn": Provides a brief examination of the role of Lorkhan in various pantheons, highlighting the complex views different races hold regarding Lorkhan[3].

[1] religion & legends.json  
[2] religion & legends.json  
[3] religion & legends.json

religion & legends.json refers to a Master JSON that contains ... religion & legends books. Read `chatgpt_assistant` for more information.
---

Please click on each subdirectory to have their specific purpose explained. Understanding the storage and data is critical before making a selection.
