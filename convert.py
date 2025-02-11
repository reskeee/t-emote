from pydub import AudioSegment


def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format='wav')
    print(f"Файл успешно преобразован в WAV: {output_file}")

if __name__ == "__main__":
    input_path = "call.mp3"
    output_path = "call.wav"
    convert_to_wav(input_path, output_path)
