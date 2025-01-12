from langdetect import detect

def generate(client, model, input_text):
    response = client.chat.completions.create(
        model="llama3.1:8b",
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
        model="llama3.1:8b",
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
        model="llama3.1:8b",  # 使用適當的模型
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
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": "You are an assistant who compares the similarity of two files. Please give a number between 0% and 100% to illustrate the similarity of the two files based on the meaning of the article and the repetition of the text."},
            {"role": "user", "content": f"Text 1: {text1}\nText 2: {text2}"},
        ]
    )
    return response.choices[0].message.content

# def main():
#     # 設定 argparse
#     parser = argparse.ArgumentParser(description="AI 翻譯程式")
#     parser.add_argument("--xdd-T", type=str, help="輸入包含文字內容的文字檔名稱")
#     parser.add_argument("--xdd-S", type=str, help="輸入包含文字內容的文字檔名稱，生成摘要")
#     parser.add_argument("--xdd-C", type=str, nargs=2, help="輸入兩個文字檔名稱，生成相似度比較")
    
#     args = parser.parse_args()

#     # 處理參數
#     if args.xdd_T:
#         try:
#             # 讀取文字檔內容
#             with open(args.xdd_T, "r", encoding="utf-8") as file:
#                 input_text = file.read().strip()
#                 print(f"從檔案中讀取的內容:\n{input_text}\n")

#                 # 翻譯文字
#                 translation = translate_input(client, args.model, input_text)

#                 # 輸出翻譯結果
#                 print("\n=== 翻譯結果 ===")
#                 print(f"原文: {input_text}")
#                 print(f"翻譯: {translation}")
#                 print("================\n")
#         except FileNotFoundError:
#             print(f"錯誤: 找不到檔案 {args.xdd_T}，請確認檔案名稱是否正確。")
#         except Exception as e:
#             print(f"發生錯誤: {e}")

#     if args.xdd_S:
#         try:
#             # 讀取文字檔內容
#             with open(args.xdd_S, "r", encoding="utf-8") as file:
#                 input_text = file.read().strip()
#                 print(f"從檔案中讀取的內容:\n{input_text}\n")

#                 # 生成摘要
#                 summary = generate_summary(client, model, input_text)

#                 # 輸出摘要結果
#                 print("\n=== 摘要結果 ===")
#                 print(f"摘要: {summary}")
#                 print("================\n")
#         except FileNotFoundError:
#             print(f"錯誤: 找不到檔案 {args.xdd_S}，請確認檔案名稱是否正確。")
#         except Exception as e:
#             print(f"發生錯誤: {e}")

#     if args.xdd_C:
#         try:
#             # 讀取兩個文字檔內容
#             with open(args.xdd_C[0], "r", encoding="utf-8") as file1, open(args.xdd_C[1], "r", encoding="utf-8") as file2:
#                 text1 = file1.read().strip()
#                 text2 = file2.read().strip()
#                 print(f"文件 1 內容:\n{text1}\n")
#                 print(f"文件 2 內容:\n{text2}\n")

#                 # 比較相似度
#                 similarity = compare_similarity(text1, text2)

#                 # 輸出相似度結果
#                 print("\n=== 相似度比較結果 ===")
#                 print(f"相似度: {similarity}")
#                 print("========================\n")
#         except FileNotFoundError as e:
#             print(f"錯誤: {e}")
#         except Exception as e:
#             print(f"發生錯誤: {e}")
            
#     else:
#         # 未提供任何參數
#         print("")

# if __name__ == "__main__":
#     main()
