from PIL import Image
from collections import Counter
import matplotlib.pyplot as plt

def get_most_common_colors(image_path, num_colors=10):
    """
    Find the most common colors in the given image.
    
    :param image_path: Path to the image file.
    :param num_colors: Number of most common colors to find.
    :return: List of (color, count) tuples.
    """
    # Open the image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode if not already
        img = img.convert('RGB')
        
        # Get all pixel colors
        pixels = list(img.getdata())
        
        # Count occurrences of each color
        color_counter = Counter(pixels)
        
        # Get the most common colors
        most_common_colors = color_counter.most_common(num_colors)
        
    return most_common_colors

def plot_colors(colors):
    """
    Plot the most common colors as a bar chart.
    
    :param colors: List of (color, count) tuples.
    """
    # Create a list of color values and their counts
    color_values = [color[0] for color in colors]
    counts = [color[1] for color in colors]
    
    # Convert RGB values to hex
    hex_colors = ['#%02x%02x%02x' % color for color in color_values]
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(colors)), counts, color=hex_colors)
    plt.xticks(range(len(colors)), hex_colors, rotation=90)
    plt.xlabel('Color')
    plt.ylabel('Count')
    plt.title('Most Common Colors in Image')
    plt.show()

def main():
    """
    Main function to handle user input and process the audio to PDF conversion.
    """
    image_path = input("Enter the path to the image file: ")
    num_colors = int(input("Enter the number of most common colors to find: "))
    
    print("Finding the most common colors...")
    common_colors = get_most_common_colors(image_path, num_colors)
    
    if not common_colors:
        print("No colors found in the image.")
        return
    
    print("Most common colors found:")
    for color, count in common_colors:
        print(f"Color: {color}, Count: {count}")
    
    print("Plotting colors...")
    plot_colors(common_colors)

if __name__ == "__main__":
    main()
