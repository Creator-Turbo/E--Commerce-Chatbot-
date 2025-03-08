from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEmbeddings 
from dotenv import load_dotenv
from src.ingest import ingestdata
import os 

# Load environment variables from .env file
load_dotenv()
# Get API keys from environment variables
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')


# Store them explicitly in environment variables
os.environ['HUGGINGFACEHUB_API_TOKEN'] = HUGGINGFACEHUB_API_TOKEN

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    # PRODUCT_BOT_TEMPLATE = """
    # Your ecommercebot bot is an expert in product recommendations and customer queries.
    # It analyzes product titles and reviews to provide accurate and helpful responses.
    # Ensure your answers are relevant to the product context and refrain from straying off-topic.
    # Your responses should be concise and informative.

    # CONTEXT:
    # {context}

    # QUESTION: {question}

    # YOUR ANSWER: 
    PRODUCT_BOT_TEMPLATE = """
    Your ecommerce chatbot specializes in product recommendations and customer queries.
    Analyze product titles and reviews to provide relevant, concise, and informative answers.
    
    CONTEXT:
    {context}
    
    RESPONSE:
    """




    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

   

    llm = HuggingFaceHub(
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    model_kwargs={"temperature": 1, "max_length": 180}
   )


    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__=='__main__':
    vstore = ingestdata("done")
    chain  = generation(vstore)
    print(chain.invoke("can you tell me the best bluetooth buds?"))
    
    
    