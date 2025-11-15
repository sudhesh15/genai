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

const codingAgent = new Agent({
  name: 'coding_agent',
  model: 'gpt-4.1-mini',
  instructions: 'You are a coding assistant. Help users with coding questions and problems.',
});

const gatewayAgent = new Agent({
  name: 'gateway_agent',
  instructions: `You are a gateway agent that routes user queries to the appropriate specialized agent.`,
  handoffs: [codingAgent, cookingAgent],
});

async function main(query) {
  const response = await run(gatewayAgent, query);
  console.log('History', response.history);
  console.log(response.finalOutput);
}

main("How to prepare masala chai").catch(err => console.error('Error running agent:', err));
