import speech_recognition as sr
from fpdf import FPDF
import os

def audio_to_text(audio_path):
    """
    Convert audio file to text using speech recognition.
    """
    recognizer = sr.Recognizer()
    text = ""
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return text

def text_to_pdf(text, output_file):
    """
    Convert the given text to a PDF and save it to an output file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add text to PDF
    pdf.multi_cell(0, 10, text)
    
    pdf.output(output_file)
    print(f"PDF saved to {output_file}")

def main():
    """
    Main function to handle user input and process the audio to PDF conversion.
    """
    audio_path = input("Enter the path to the audio file: ")
    output_file = input("Enter the output PDF file name (e.g., output.pdf): ")
    
    print("Transcribing audio to text...")
    text = audio_to_text(audio_path)
    
    if not text.strip():
        print("No text transcribed from the audio.")
        return
    
    print("Generating PDF...")
    text_to_pdf(text, output_file)
    print("Done.")

if __name__ == "__main__":
    main()