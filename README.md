### 注意!!! 這是學校功課，一個簡單使用ollama的小工具
# 使用 Ollama 的命令行工具
這是一個基於 Python 的命令行工具，結合了 Ollama 提供的開源大模型 API，幫助用戶更高效地完成翻譯、摘要生成、文本比較等多種任務。

## 功能特色
- **聊天模式 ( Chat ):** 與 AI 聊天互動。
- **文章生成 ( Generate ):** 根據檔案內容或你輸入的內容來生成內容。
- **翻譯功能 ( Translate ):** 自動檢測輸入語言，並在繁體中文與英文間進行精準翻譯。
- **摘要生成 ( Summary ):** 根據文檔內容生成繁體中文摘要。
- **相似度比較 ( Compare ):** 比較兩份文檔的相似度，並以百分比呈現結果。

## 安裝與執行
### 先決條件
1. 安裝 Python ( 版本 3.8 或更高 )。
2. 安裝和部署 Ollama 模型並啟動 API 服務
    ```bash
    ollama pull llama3.1:8b
    ```
3. 安裝所需的 Python 套件( 我使用 Anaconda 來管理虛擬環境 )：
    ```bash
    pip install openai argparse langdetect
    ```

### Clone並執行
1. Clone此專案：
    ```bash
    git clone https://github.com/Yuri817106/cli_chat.git
    cd cli_chat
    ```

2. 執行程式：
    ```bash
    python xdd.py --model [模型名稱] --mode [模式] [其他參數]
    ```

## 使用方式
### 基本指令
- **聊天模式 (Chat):**
    ```bash
    python3 xdd.py --mode chat
    ```
- **單次生成 (Generate):**
    ```bash
    python3 xdd.py --mode generate
    python3 xdd.py --mode generate --input file.txt
    ```
- **翻譯功能 (Translate):**
    ```bash
    python3 xdd.py --mode translate --input file.txt
    ```
- **摘要生成 (Summary):**
    ```bash
    python3 xdd.py --mode summary --input file.txt
    ```
- **相似度比較 (Compare):**
    ```bash
    python3 xdd.py --mode compare --files file1.txt file2.txt
    ```

### 參數說明
- `--model`: 指定使用的模型名稱，默認為 `llama3.1:8b`。
- `--mode`: 指定使用的模式名稱。
- `--input`: 指定需要處理的單個文件。
- `--files`: 指定需要處理的兩個文件。