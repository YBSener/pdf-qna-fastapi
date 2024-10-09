from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache
from app.models.google_config import get_google_embeddings
import logging

logger = logging.getLogger(__name__)

set_llm_cache(InMemoryCache())


async def answer_question(question):
    try:
        embeddings = get_google_embeddings()
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(question)

        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

        return response["output_text"]
    except Exception as e:
        logger.error(f"An error from gemini api: {str(e)}")
        raise

def get_conversational_chain():
    from langchain.prompts import PromptTemplate
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in the provided context, just say,
    "answer is not available in the context". Do not provide incorrect answers.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain
