import whisper

def transcribe_wav(file_path):
    # モデルのロード (base, small, medium, largeなどがあります)
    # 精度を上げるなら 'medium' や 'large' に変更してください
    model = whisper.load_model("base")

    print(f"処理を開始します: {file_path}")
    
    # 文字起こしの実行
    result = model.transcribe(file_path, verbose=True, language='ja')

    # 結果の出力
    print("-" * 30)
    print("【文字起こし結果】")
    print(result["text"])
    
    # テキストファイルに保存
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("-" * 30)
    print("output.txt に保存しました。")

# 実行
if __name__ == "__main__":
    # ここにWAVファイルのパスを入力してください
    transcribe_wav("your_audio_file.wav")