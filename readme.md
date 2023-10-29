# TikZtract

## Description

`TikZtract` is a Python script designed to extract TikZ graphics from a LaTeX file and convert them into PNG images. The script scans the LaTeX file for TikZ environments, isolates each one into a standalone LaTeX document, and then converts them directly to PNG images using `pdflatex`.

## Features

# TikZtract

## Description

`TikZtract` is a Python script designed to extract TikZ graphics from a LaTeX file and convert them into PNG images. The script scans the LaTeX file for TikZ environments, isolates each one into a standalone LaTeX document, and then converts them directly to PNG images using `pdflatex`.

## Features

- Extracts all TikZ graphics from a given `.tex` file
- Creates standalone LaTeX documents for each extracted graphic
- Converts each standalone LaTeX document to a PNG image
- Optionally overwrites existing graphics in the output folder

## Requirements

- Python 3.x
- LaTeX distribution with `pdflatex`
- Additional LaTeX packages may be required based on the `.tex` file being processed

## Usage

Run the script from the terminal, providing the path to your `.tex` file as an argument.

```bash
python tikztract.py <path-to-tex-file>
```

The script will:

1. Check if the provided file is a `.tex` file
2. Create a `graphics` folder in the same location as the script
3. Extract TikZ graphics and convert them to PNG images inside the `graphics` folder

## Notes

- If the `graphics` folder already exists and contains graphics, the script will prompt you to confirm whether it should overwrite the existing files.
- If the `.tex` file uses additional LaTeX packages, the generated standalone files will also use them.

## License

MIT License