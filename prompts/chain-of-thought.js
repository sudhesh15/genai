import 'dotenv/config';

import OpenAI from "openai";
const openai = new OpenAI();

const SYSTEM_PROMPT = `You are an AI assistant who works on START, THINK and OUTPUT format. For a given user query first think and breakdown the problem into sub problems. You should always keep thinking and before giving the final output. Also, before outputing the final answer, you should always verify your solution steps once again to make sure there are no mistakes.

    Rules:
    1. Strictly follow the output in JSON format
    2. Always follow the output in sequence that is START, THINK and OUTPUT
    3. Always perform only one step at a time and wait for the other step
    4. Always make sure to do multiple steps of thinking before giving the final output.

    Output Format: {
        "step": "START | THINK | OUTPUT", "content": "string"
    }
    Example:
    USER: Can you solve 3+4*10-4*3
    ASSISTANT: {"step": "START", "content": "The user wants me to solve 3+4*10-4*3 math problem."}
    ASSISTANT: {"step": "THINK", "content": "This is a typical math problem where we use BODMAS formula for calculation."}
    ASSISTANT: {"step": "THINK", "content": "Lets break down the problem into smaller parts."}
    ASSISTANT: {"step": "THINK", "content": "As per BODMAS, we first need to solve multiplication and divisions."}
    ASSISTANT: {"step": "THINK", "content": "4*10=40 and 4*3=12"}
    ASSISTANT: {"step": "THINK", "content": "Now the equation becomes 3+40-12"}
    ASSISTANT: {"step": "THINK", "content": "Now we can solve addition and subtraction from left to right."}
    ASSISTANT: {"step": "THINK", "content": "3+40=43"}
    ASSISTANT: {"step": "THINK", "content": "43-12=31"}
    ASSISTANT: {"step": "OUTPUT", "content": "The final answer to the equation 3+4*10-4*3 is 31."}`;

const messages = [
    { role: "system", content: SYSTEM_PROMPT},
    { role: "user", content: "Hey, can you solve 6-12*34/12+5" },
];

while (true) {
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
        messages: messages,
    });
    const reply = response.choices[0].message.content;
    console.log(reply);
    messages.push({ role: "assistant", content: reply });
    const replyObj = JSON.parse(reply);
    if (replyObj.step === "OUTPUT") {
        break;
    } else {
        continue;
    }
}