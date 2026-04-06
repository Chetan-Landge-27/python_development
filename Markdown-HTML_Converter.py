

import markdown

def convert_md_to_html(input_file, output_file):
    """Convert a Markdown file to HTML and save it."""
    try:
        with open(input_file, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(md_content)
        
        with open(output_file, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        
        print(f"✅ Conversion successful! Saved as {output_file}")
    
    except FileNotFoundError:
        print("⚠️ Input file not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter the Markdown file name: ").strip()
    output_file = input("Enter the output HTML file name: ").strip()
    convert_md_to_html(input_file, output_file)