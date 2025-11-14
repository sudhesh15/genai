import { OpenAIEmbeddings } from "@langchain/openai";
import { QdrantVectorStore } from "@langchain/qdrant";
import OpenAI from "openai";
import 'dotenv/config';

const client = new OpenAI();

async function chat() {
  const query = "What is a closure in JavaScript?";

  const embeddings = new OpenAIEmbeddings({
    model: "text-embedding-3-large",
  });

  const vectorStore = await QdrantVectorStore.fromExistingCollection(embeddings, {
    url: "http://localhost:6333",
    collectionName: "documents",
  });

  const vectorSearcher = vectorStore.asRetriever({ k: 3 });
  const relevantDocs = await vectorSearcher.invoke(query);

  const SYSTEM_PROMPT = `You are an AI assistant that helps people find information. Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know.
    Context: ${JSON.stringify(relevantDocs)}`;

  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: SYSTEM_PROMPT },
      { role: "user", content: query },
    ],
  });

  console.log("Response:", response.choices[0].message.content);
}

chat().catch((err) => {
  console.error("Error:", err);
});
