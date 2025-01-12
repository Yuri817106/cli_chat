from openai import OpenAI
import argparse
import mode
import file_mode

def handle_generate(client, model, input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            input_text = file.read().strip()
            print(f"從檔案中讀取的內容:\n{input_text}\n")
            generate_from_file = file_mode.generate(client, model, input_text)
            print("\n=== 生成結果 ===")
            print(f"內容: {generate_from_file}")
            print("================\n")
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 {input_file}，請確認檔案名稱是否正確。")
    except Exception as e:
        print(f"發生錯誤: {e}")

def handle_translate(client, model, input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            input_text = file.read().strip()
            print(f"從檔案中讀取的內容:\n{input_text}\n")

            translation = file_mode.translate_input(client, model, input_text)
            print("\n=== 翻譯結果 ===")
            print(f"原文: {input_text}")
            print(f"翻譯: {translation}")
            print("================\n")
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 {input_file}，請確認檔案名稱是否正確。")
    except Exception as e:
        print(f"發生錯誤: {e}")

def handle_summary(client, model, input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            input_text = file.read().strip()
            print(f"從檔案中讀取的內容:\n{input_text}\n")

            summary = file_mode.generate_summary(client, model, input_text)
            print("\n=== 摘要結果 ===")
            print(f"摘要: {summary}")
            print("================\n")
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 {input_file}，請確認檔案名稱是否正確。")
    except Exception as e:
        print(f"發生錯誤: {e}")

def handle_compare(client, model, files):
    try:
        with open(files[0], "r", encoding="utf-8") as file1, open(files[1], "r", encoding="utf-8") as file2:
            text1 = file1.read().strip()
            text2 = file2.read().strip()
            print(f"文件 1 內容:\n{text1}\n")
            print(f"文件 2 內容:\n{text2}\n")

            similarity = file_mode.compare_similarity(client, model, text1, text2)
            print("\n=== 相似度比較結果 ===")
            print(f"相似度: {similarity}")
            print("========================\n")
    except FileNotFoundError as e:
        print(f"錯誤: {e}")
    except Exception as e:
        print(f"發生錯誤: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="llama3.1:8b", help="model name")
    parser.add_argument("--mode", type=str, choices=["chat", "generate", "translate", "summary", "compare"], required=True, help="choose mode")
    parser.add_argument("--input", type=str, help="input file for 'translate' and 'summary' modes")
    parser.add_argument("--files", type=str, nargs=2, help="two input files for 'compare' mode")
    args = parser.parse_args()

    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )

    if args.mode == "chat":
        mode.chat(client, args.model)
    elif args.mode == "generate":
        if not args.input:
            mode.generate(client, args.model)
        else:
            handle_generate(client, args.model, args.input)
    elif args.mode == "translate":
        if not args.input:
            print("錯誤: 翻譯模式需要提供 --input 參數指定輸入檔案。")
        else:
            handle_translate(client, args.model, args.input)
    elif args.mode == "summary":
        if not args.input:
            print("錯誤: 摘要模式需要提供 --input 參數指定輸入檔案。")
        else:
            handle_summary(client, args.model, args.input)
    elif args.mode == "compare":
        if not args.files or len(args.files) != 2:
            print("錯誤: 比較模式需要提供 --files 參數指定兩個檔案。")
        else:
            handle_compare(client, args.model, args.files)


if __name__ == "__main__":
    main()
