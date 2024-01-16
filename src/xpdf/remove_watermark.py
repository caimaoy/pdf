import os
from itertools import product

import fitz

from xpdf.utils import add_suffix_to_filename


class RemoveWatermark:
    IMAGES_FOLDER = "PDFimages"

    def __init__(self):
        if not os.path.exists(self.IMAGES_FOLDER):
            os.makedirs(self.IMAGES_FOLDER)

    def remove_watermark_from_pdf(self, input_pdf_path):
        pdf_file = fitz.open(input_pdf_path)

        for page_no, page in enumerate(pdf_file):
            zoom_x = 4.0
            zoom_y = 4.0
            matrix = fitz.Matrix(zoom_x, zoom_y)
            pix = page.get_pixmap(matrix=matrix)

            for pos in product(range(pix.width), range(pix.height)):
                if sum(pix.pixel(pos[0], pos[1])) >= 600:
                    pix.set_pixel(pos[0], pos[1], (255, 255, 255))

            img_path = os.path.join(self.IMAGES_FOLDER, f"{page_no}.png")
            pix.pil_save(img_path, dpi=(30000, 30000))
            print(f"Page {page_no} watermark removed")

        pdf_file.close()

    def images_to_pdf(self, input_file: str, output_pdf_suffix="_result"):
        pic_dir = self.IMAGES_FOLDER
        pdf_name = add_suffix_to_filename(input_file, output_pdf_suffix)
        pdf = fitz.open()
        img_files = sorted(os.listdir(pic_dir), key=lambda x: int(x.split(".")[0]))

        for img in img_files:
            print("Composing", img)
            img_path = os.path.join(pic_dir, img)
            img_doc = fitz.open(img_path)
            pdf_bytes = img_doc.convert_to_pdf()
            img_pdf = fitz.open("pdf", pdf_bytes)
            pdf.insert_pdf(img_pdf)

        pdf.save(pdf_name)
        pdf.close()

    @staticmethod
    def clean_up():
        for img in os.listdir(RemoveWatermark.IMAGES_FOLDER):
            img_path = os.path.join(RemoveWatermark.IMAGES_FOLDER, img)
            os.remove(img_path)

    def process_and_save(self, input_pdf, output_pdf_suffix="_result"):
        self.remove_watermark_from_pdf(input_pdf)
        self.images_to_pdf(input_pdf, output_pdf_suffix)
        RemoveWatermark.clean_up()


if __name__ == "__main__":
    input_pdf_file = input("Enter the input PDF file name: ")
    output_pdf_suffix = input("Enter the output PDF suffix (default is '_result'): ")

    remover = RemoveWatermark()
    remover.process_and_save(input_pdf_file, output_pdf_suffix)
