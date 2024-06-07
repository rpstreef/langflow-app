import os
import uvicorn
from langflow import load_flow_from_json

# Load environment variables
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Create a LangFlow instance
txt_rag = load_flow_from_json("./langflow/txt-rag.json")

# Create a LangServe app
app = LangServe(txt_rag)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)