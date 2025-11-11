import 'dotenv/config';

import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.chat.completions.create({
  model: "gpt-4o",
    messages: [
        { role: "system", content: `You're an AI assistant expert in coding in JavaScript. You only and only know JavaScript. If user asks any question unrelated to JavaScript, do not answer` },
        { role: "user", content: "Hello, how to cook maggi?" },
    ],
});

console.log(response.choices[0].message.content);