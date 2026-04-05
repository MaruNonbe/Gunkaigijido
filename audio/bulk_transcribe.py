import whisper
import os

def bulk_transcribe():
    # 1. モデルのロード（精度の高い 'turbo' または 'large' を推奨）
    print("モデルを読み込んでいます...")
    model = whisper.load_model("turbo")

    # 2. 音声ファイルが入っているフォルダを指定（. は現在のフォルダ）
    audio_dir = "." 
    # 対応する拡張子
    extensions = (".wav", ".mp3", ".m4a", ".mp4")

    # フォルダ内のファイルをループ処理
    for filename in os.listdir(audio_dir):
        if filename.endswith(extensions):
            file_path = os.path.join(audio_dir, filename)
            print(f"\n--- 処理中: {filename} ---")
            
            # 3. 文字起こし実行 (languageを指定しないと自動判別します)
            # 特定したい場合は language='ja' (日), 'zh' (中), 'en' (英), 'ko' (韓)
            result = model.transcribe(file_path, verbose=False)

            # 4. 結果をファイルに保存（音声ファイル名.txt）
            output_filename = os.path.splitext(filename)[0] + ".txt"
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(result["text"])
            
            print(f"完了！保存先: {output_filename}")
            print("冒頭部分:", result["text"][:50], "...")

if __name__ == "__main__":
    bulk_transcribe()