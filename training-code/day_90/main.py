import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Speech saved to {output_file}")

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    output_file = input("Enter the output audio file name (e.g., output.mp3): ")
    
    print("Extracting text from PDF...")
    text = pdf_to_text(pdf_path)
    
    if text.strip() == "":
        print("No text found in the PDF.")
        return
    
    print("Converting text to speech...")
    text_to_speech(text, output_file)
    print("Done.")

if __name__ == "__main__":
    main()
