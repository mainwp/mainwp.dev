#!/usr/bin/env node

const { BedrockAgentRuntimeClient, RetrieveCommand } = require("@aws-sdk/client-bedrock-agent-runtime");

// Configure AWS credentials
const client = new BedrockAgentRuntimeClient({
  region: "us-east-1",
  credentials: {
    accessKeyId: "AKIAXZRZVM2IGAXRIXOX",
    secretAccessKey: "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"
  }
});

async function retrieveFromAwsKb(query, knowledgeBaseId, n = 3) {
  try {
    const command = new RetrieveCommand({
      knowledgeBaseId: knowledgeBaseId,
      retrievalQuery: {
        text: query
      },
      retrievalConfiguration: {
        vectorSearchConfiguration: {
          numberOfResults: n
        }
      }
    });

    const response = await client.send(command);
    return response.retrievalResults;
  } catch (error) {
    console.error("Error retrieving from AWS Knowledge Base:", error);
    return { error: error.message };
  }
}

// Example usage
async function main() {
  const knowledgeBaseId = process.argv[2] || "test-kb-id";
  const query = process.argv[3] || "What are AWS Lambda functions?";
  const n = parseInt(process.argv[4] || "3", 10);

  console.log(`Retrieving information from AWS Knowledge Base (${knowledgeBaseId})...`);
  console.log(`Query: ${query}`);
  console.log(`Number of results: ${n}`);
  
  const results = await retrieveFromAwsKb(query, knowledgeBaseId, n);
  console.log("\nResults:");
  console.log(JSON.stringify(results, null, 2));
}

main().catch(console.error);
