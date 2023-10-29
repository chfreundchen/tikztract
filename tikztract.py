import os
import re
import subprocess
import sys

def main():
    # Check for input arguments
    if len(sys.argv) != 2:
        print("Usage: tikztract.py <filename.tex>")
        return
    
    input_file = sys.argv[1]
    
    # Check if it's a .tex file
    if not input_file.endswith(".tex"):
        print("The input file must be a .tex file.")
        return

    # Get directory path
    directory_path = os.path.dirname(input_file)
    graphics_path = os.path.join(directory_path, "graphics")

    # Check if graphics folder already exists
    if os.path.exists(graphics_path):
        files_in_graphics = os.listdir(graphics_path)
        if files_in_graphics:  # Folder is not empty
            user_input = input("Do you want to overwrite existing graphics? (Y/n): ") or 'y'
            if user_input.lower() != 'y':
                print("Aborting.")
                return
    else:
        os.mkdir(graphics_path)

    # Read .tex file
    with open(input_file, 'r') as f:
        content = f.read()

    # Find all used packages
    package_list = re.findall(r'\\usepackage\{(.*?)\}', content)
    packages = "\n".join([f"\\usepackage{{{pkg}}}" for pkg in package_list])
    
    # Find all TikZ environments
    tikz_list = re.findall(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', content, re.DOTALL)

    print(f"\n{len(tikz_list)} graphics found.\n")


    for idx, tikz_code in enumerate(tikz_list):
        print(f"Processing graphic {idx+1}...")
        standalone_content = (
            "\\documentclass[convert={density=300,outext=.png}]{standalone}\n"
            f"{packages}\n"
            "\\begin{document}\n"
            "\\begin{tikzpicture}\n"
            f"{tikz_code.strip()}\n"
            "\\end{tikzpicture}\n"
            "\\end{document}"
        )
        
        standalone_file = os.path.join(graphics_path, f"graphic_{idx}.tex")
        
        # Write standalone .tex file
        with open(standalone_file, 'w') as f:
            f.write(standalone_content)
        
        # Convert .tex to .png directly
        command = f"(cd {graphics_path} && TEXINPUTS=.:$TEXINPUTS pdflatex -interaction=nonstopmode --shell-escape {os.path.basename(standalone_file)} > /dev/null 2>&1)"
        subprocess.run(command, shell=True, env={**os.environ, 'TEXINPUTS': '.:' + os.environ.get('TEXINPUTS', '')})

        # Remove extra files
        cleanup_command = f"(cd {graphics_path} && rm graphic_{idx}.tex graphic_{idx}.aux graphic_{idx}.log graphic_{idx}.pdf)"
        subprocess.run(cleanup_command, shell=True)

if __name__ == "__main__":
    main()
