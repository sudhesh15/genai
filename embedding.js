import 'dotenv/config';
import OpenAI from "openai";
const openai = new OpenAI();

const embedding = await openai.embeddings.create({
  model: "text-embedding-3-small",
  input: "My name is Sudhesh",
  encoding_format: "float",
});

console.log(embedding);