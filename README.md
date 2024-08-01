# ai-agent-answering-pdf-related-information
The code will create an AI agent that leverages the capabilities of a large language model. This agent should be able to extract answers based on the content of a large PDF document and post the results on Slack using OpenAI LLMs


## Tech stack
- Python Argparse for CLI
- ChromaDB as vector database
- OpenAI gpt-3.5-turbo-0125

## Project Environment
The project file structure is simple, we will have four Python files 
- client.py: for defining the CLI 
- application.py: for processing, storing, and querying data. 
- messaging.py: for messaging utility
- requirements.txt: for all necessary dependant packages
Load the OpenAI API key and Slack App Auth Token (The APP, which was created to send message to a specific channel)


## Code Workflow 
- User inputs the path of the pdf and a list of queries (extra parameters added to clear vector store collection if required, value for no. words in a single chunk,Number of results to be fetched from collection)
- To store text embeddings and their metadata, we will create a collection with ChromaDB.
- As an embedding model, we are using MiniLM-L6-V2 with ONNX runtime. It is small yet capable and on top of that open-sourced.
- Next, we will define a function to verify if a provided file path belongs to a valid PDF file.
- One of the major parts of a PDF Q&A app is to get text chunks. So, we need to define a function that gets us the required chunks of text.
- We have defined a basic algorithm for getting chunks. The idea is to let users create as many words as they want in a single text chunk. And every text chunk will end with a complete sentence, even if it breaches the limit. This is a simple algorithm. You may create something on your own.
- Then a function to load texts from PDFs and create a dictionary to keep track of text chunks belonging to a single page.
- Now, we need to store the data in a ChromaDB collection. In Chromadb, the metadata field stores additional information regarding the documents. In this case, the page number of a text chunk is its metadata. After extracting metadata from each text chunk, we can store them in the collection we created earlier. This is required only when the user provides a valid file path to a PDF file.
- We will now define a function that processes user queries to fetch data from the database.
- Now, the only major thing remaining is to feed the LLM with information.
- Then the utility function combines obtained text chunks with the user queries, feeds it into the get_response() function, and returns the resulting answer strings. The json created is  list of dictionaries. 
- Finally, the response is sent a slack message via an slack app created in a defined workspace and channel.

## Possible Enhancments

- Usage of streamlit UI to enhance CLI
- Multiple pdfs as provision for better retrieval strategy
- Usage of context (RAG?) in the prompt for better answers
- Better Vector DB like Open Search?