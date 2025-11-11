import 'dotenv/config';
import OpenAI from "openai";
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Simple: send the user query to two models, then ask a third model to pick the better answer.
async function askModel(model, query) {
    const res = await openai.chat.completions.create({
        model,
        messages: [{ role: "user", content: query }],
        temperature: 0.7,
        max_tokens: 600,
    });
    return res.choices[0].message.content.trim();
}

async function judge(model, query, a1, a2) {
    const res = await openai.chat.completions.create({
        model,
        messages: [
            { role: "system", content: "You are a judge. Output ONLY '1' or '2' to indicate which answer is better." },
            {
                role: "user",
                content: `Question:\n${query}\n\nAnswer 1:\n${a1}\n\nAnswer 2:\n${a2}\n\nWhich is better? Output only 1 or 2.`
            }
        ],
        temperature: 0.0,
        max_tokens: 5,
    });
    return res.choices[0].message.content.trim();
}

(async () => {
    const userQuery = process.argv.slice(2).join(" ") || "Explain JavaScript closures with a short example.";

    const modelA = "gpt-4o-mini"; // first model
    const modelB = "gpt-4o";      // second model
    const judgeModel = "gpt-4o";  // third model that picks best of the two

    const [answerA, answerB] = await Promise.all([
        askModel(modelA, userQuery),
        askModel(modelB, userQuery),
    ]);

    console.log("Answer 1 (from", modelA + "):\n", answerA, "\n");
    console.log("Answer 2 (from", modelB + "):\n", answerB, "\n");

    const choice = await judge(judgeModel, userQuery, answerA, answerB);
    const winner = choice === "1" ? answerA : choice === "2" ? answerB : "(judge did not return 1 or 2)";

    console.log("Judge chose:", choice);
    console.log("Selected answer:\n", winner);
})();
