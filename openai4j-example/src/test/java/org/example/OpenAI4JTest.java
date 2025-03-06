package org.example;

import dev.ai4j.openai4j.OpenAiClient;
import dev.ai4j.openai4j.chat.ChatCompletionRequest;
import dev.ai4j.openai4j.chat.ChatCompletionResponse;
import org.junit.jupiter.api.Test;

class OpenAI4JTest {

    @Test
    void chatCompletion() {

        // Note: non-chat completion (CompletionRequest) is not supported in GPT-4o-mini

        String apiKey = System.getenv("OPENAI_API_KEY");

                OpenAiClient client = OpenAiClient.builder()
                .openAiApiKey(apiKey)
                .logRequests()
                .logResponses()
                .build();

        ChatCompletionRequest request = ChatCompletionRequest.builder()
                .model("gpt-4o-mini")
                .addSystemMessage("あなたは2020年代の若い詩人です")
                .addUserMessage("ChatGPTについてのボカロっぽい詩を３行で書いてください")
                .temperature(0.9)
                .build();

        ChatCompletionResponse response = client.chatCompletion(request).execute();

        System.out.println(response.choices().get(0).message().content());
    }
}
