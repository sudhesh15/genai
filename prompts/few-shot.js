import 'dotenv/config';

import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.chat.completions.create({
  model: "gpt-4o",
    messages: [
        { role: "system", content: `You're an AI assistant expert in coding in JavaScript. You only and only know JavaScript. If user asks any question unrelated to JavaScript, do not answer
            Examples: 
            Q. Hey
            A. Hey, nice to meet you, how can help you with JavaScript today? 
            
            Q. Hey, I want to learn JavaScript.
            A. Sure, I can help you with that. Here are the basics of JavaScript we  can start with.`

            //you can add more examples here or give negative examples as well, in reality few-shot prompts work better with more examples.
        },
        { role: "user", content: "Hello" },
    ],
});

console.log(response.choices[0].message.content);