import 'dotenv/config';
import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { OpenAIEmbeddings } from "@langchain/openai";
import { QdrantVectorStore } from "@langchain/qdrant";

async function init() {
    const PdfFilePath = "./rag/nodejs-notes.pdf";
    const loader = new PDFLoader(PdfFilePath);

    //page by page load the pdf file
    const docs = await loader.load();

    //ready the openai embedding model
    const embeddings = new OpenAIEmbeddings({
        model: "text-embedding-3-large",
    });

    const vectorStore = await QdrantVectorStore.fromDocuments(docs, embeddings, {
        url: "http://localhost:6333",
        collectionName: "documents",
    });

    console.log("Indexing completed");
}

init();