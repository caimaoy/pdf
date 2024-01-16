from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from xpdf.utils import add_suffix_to_filename


class WatermarkBuilder:
    def __init__(self, content: str):
        self.content = content
        self.rotate: int = 45
        self.n_space_between_content: int = 30
        self.alpha: float = 0.1
        self.fontsize: int = 15
        self.font: str = "FZHTJW"

        font_path = "font/FZHTJW.TTF"

        # 中文字体
        pdfmetrics.registerFont(TTFont("FZHTJW", font_path))

    def with_rotation(self, rotate: int) -> "WatermarkBuilder":
        """设置水印旋转角度"""
        self.rotate = rotate
        return self

    def with_spacing(self, n_space_between_content: int) -> "WatermarkBuilder":
        """设置水印内容之间的间距"""
        self.n_space_between_content = n_space_between_content
        return self

    def with_alpha(self, alpha: float) -> "WatermarkBuilder":
        """设置水印透明度"""
        self.alpha = alpha
        return self

    def with_fontsize(self, fontsize: int) -> "WatermarkBuilder":
        """设置水印字体大小"""
        self.fontsize = fontsize
        return self

    def with_font(self, font: str) -> "WatermarkBuilder":
        """设置水印字体"""
        self.font = font
        return self

    def build_watermark(self) -> PdfReader:
        """构建水印"""
        c = canvas.Canvas("watermark.pdf", pagesize=letter)
        c.setFont(self.font, self.fontsize)
        c.setFillAlpha(self.alpha)
        c.rotate(self.rotate)

        for i in range(20):
            c.drawCentredString(0 * cm, (20 - i * 3) * cm, (self.content + " " * self.n_space_between_content) * 300)

        c.save()
        pdf_watermark = PdfReader(open("watermark.pdf", "rb"))
        return pdf_watermark


class PDFWatermarker:
    def add_watermark(self, input_file: str, output_file: str, pdf_watermark: PdfReader) -> bool:
        """给指定的PDF文件添加水印"""
        pdf_output = PdfWriter()
        input_stream = open(input_file, "rb")
        pdf_input = PdfReader(input_stream)

        if pdf_input.is_encrypted:
            print("The PDF file is encrypted.")
            try:
                pdf_input.decrypt("")
            except Exception:
                print("Failed to decrypt with an empty password.")
                return False
            else:
                print("Decrypted successfully with an empty password.")

        page_num = len(pdf_input.pages)

        for i in range(page_num):
            page = pdf_input.pages[i]
            page.merge_page(pdf_watermark.pages[0])
            pdf_output.add_page(page)

        output_stream = open(output_file, "wb")
        pdf_output.write(output_stream)

        output_stream.close()
        input_stream.close()
        return True


# 使用
# watermark_builder = WatermarkBuilder("星本国际").with_rotation(45).with_spacing(30).with_alpha(0.1).with_fontsize(15).with_font('FZHTJW')
# pdf_watermark = watermark_builder.build_watermark()

# watermark_processor = PDFWatermarker()
# watermark_processor.add_watermark('KET基础核心词汇打卡表.pdf', 'with_watermark.pdf', pdf_watermark)

# def add_watermark(input_file: str, )


def add_default_watermark(input_file: str, content: str) -> bool:
    suffix = "_with_wartermark"
    output_file = add_suffix_to_filename(input_file, suffix)
    return add_watermark_with_output(input_file=input_file, content=content, output_file=output_file)


def add_watermark_with_output(input_file: str, content: str, output_file: str) -> bool:
    watermark_builder = WatermarkBuilder(content=content)
    pdf_watermark = watermark_builder.build_watermark()

    watermark_processor = PDFWatermarker()
    watermark_processor.add_watermark(input_file, output_file, pdf_watermark)
