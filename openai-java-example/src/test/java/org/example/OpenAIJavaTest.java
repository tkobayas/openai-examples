package org.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatCompletion;
import com.openai.models.ChatCompletionCreateParams;
import com.openai.models.ChatModel;

import org.junit.jupiter.api.Test;

class OpenAIJavaTest {

    @Test
    void chatCompletion() {

        String apiKey = System.getenv("OPENAI_API_KEY");

        OpenAIClient client = OpenAIOkHttpClient.builder()
                .apiKey(apiKey)
                .build();

        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                .model(ChatModel.GPT_4O_MINI)
                .addSystemMessage("あなたは1960年代のフォークシンガーです")
                .addUserMessage("ChatGPTについてのフォークソングっぽい詩を３行で書いてください")
                .temperature(0.9)
                .build();

        ChatCompletion response = client.chat().completions().create(params);

        System.out.println(response.choices().get(0).message().content().get());
    }
}
