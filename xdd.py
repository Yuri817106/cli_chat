from openai import OpenAI
import argparse
import mode

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="llama3.1:8b", help="model name")
    parser.add_argument("--mode", type=str, choices=["chat", "generate"], required=True, help="choose mode")
    args = parser.parse_args()

    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    )

    if args.mode == "chat":
        mode.chat(client, args.model)
    elif args.mode == "generate":
        mode.generate(client, args.model)

if __name__ == "__main__":
    main()
