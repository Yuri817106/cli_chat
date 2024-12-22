from openai import OpenAI
import argparse

def chat(client, model):
    print("已進入聊天模式，輸入 'exit' 離開。")
    conversation = [
        {"role": "system", "content": "Please answer all questions in Traditional Chinese."}
    ]
    while True:
        question = input("你：")
        if question.lower() == "exit":
            print("結束聊天模式。")
            break
        conversation.append({"role": "user", "content": question})
        response = client.chat.completions.create(
            model=model,
            messages=conversation,
        )
        answer = response.choices[0].message.content
        print(f"AI：{answer}")
        conversation.append({"role": "assistant", "content": answer})

def generate(client, model):
    question = input("輸入你的問題：")
    print("正在生成...")
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Please answer all questions in Traditional Chinese."},
            {"role": "user", "content": question},
        ],
    )
    print(f"AI：{response.choices[0].message.content}")
