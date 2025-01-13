from langdetect import detect

def generate(client, model, input_text):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Please answer all questions in Traditional Chinese."},
            {"role": "user", "content": input_text},
        ]
    )
    return response.choices[0].message.content

def detect_and_translate(client, model, input_text):
    language = detect(input_text)
    if language == 'zh':
        return translate_input(client, model, input_text)  # 假設 translate_input 為翻譯函數，翻譯中文到英文
    elif language == 'en':
        return translate_input(client, model, input_text)  # 假設 translate_input 為翻譯函數，翻譯英文到繁體中文
    else:
        return "Language not supported"

def translate_input(client, model, input_text):
    """
    處理翻譯請求，AI 將根據輸入的語言自動翻譯為另一語言。
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a strict translation assistant. If the input is in Chinese, translate it directly into English. If the input is in English, translate it directly into Traditional Chinese. Do not paraphrase."},
            {"role": "user", "content": input_text},
        ]
    )
    return response.choices[0].message.content

def generate_summary(client, model, input_text):
    """
    生成文件的摘要。
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant who generates a summary of the file. Please try to describe the text content you read in a short text,and only use Traditional Chinese"},
            {"role": "user", "content": input_text},
        ]
    )
    return response.choices[0].message.content

def compare_similarity(client, model, text1, text2):
    """
    使用 AI 模型比較兩段文本的相似度。
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant who compares the similarity of two files. Please give a number between 0% and 100% to illustrate the similarity of the two files based on the meaning of the article and the repetition of the text."},
            {"role": "user", "content": f"Text 1: {text1}\nText 2: {text2}"},
        ]
    )
    return response.choices[0].message.content

