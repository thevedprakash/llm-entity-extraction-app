import os
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import save_output

def process_pdf(input_path, output_dir):
    """
    Process the PDF and save the converted text.
    Args:
        input_path (str): Path to the uploaded PDF.
        output_dir (str): Directory to store the processed text.
    Returns:
        str: Path to the processed text file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize the PDF converter
    converter = PdfConverter(artifact_dict=create_model_dict())

    # Convert the PDF to text
    rendered = converter(input_path)

    # Save the output
    fname_base = os.path.splitext(os.path.basename(input_path))[0]
    save_output(rendered, output_dir=output_dir, fname_base=fname_base)

    # Return the path to the processed text file
    return os.path.join(output_dir, f"{fname_base}.txt")
