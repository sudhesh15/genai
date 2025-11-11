import 'dotenv/config';
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.chat.completions.create({
  model: "gpt-4o",
    messages: [
        { role: "system", content: `you are my coding assistant` },
        { role: "user", content: "Hello, my name is Sudhesh?" },
        { role: "assistant", content: "Hello Sudhesh! How can I assist you today?" },
        { role: "user", content: "Hello, What is my name?" },
    ],
});

console.log(response.choices[0].message.content);