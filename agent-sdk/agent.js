import { Agent, run, tool } from '@openai/agents';
import { z } from 'zod';
import 'dotenv/config';

const getCurrentTime = tool({
  name: 'get_current_time',
  description: 'This tool returns the current time',
  parameters: z.object({}),
  execute: async () => {
    return { text: new Date().toString() };
  },
});

const cookingAgent = new Agent({
  name: 'cooking_agent',
  model: 'gpt-4.1-mini',
  tools: [getCurrentTime],
  instructions: 'You are a cooking assistant. Help users with cooking recipes and tips.',
});

async function main(query) {
  const response = await run(cookingAgent, query);
  console.log('History', response.history);
  console.log(response.finalOutput);
}

main("Depending on the current time, suggest me a good recipe.").catch(err => console.error('Error running agent:', err));
