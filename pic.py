import os
from itertools import product

import fitz


class RemoveWatermark(object):
    @staticmethod
    def remove_pdfwatermark():
        if not os.path.exists(r"PDFimages"):
            os.mkdir("PDFimages")
        path = os.path.join("PDF", os.listdir("PDF")[0])
        print(path)
        pdf_file = fitz.open(path)
        page_no = 0
        for page in pdf_file:
            zoom_x = 4.0  # horizontal zoom
            zomm_y = 4.0  # vertical zoom
            mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
            pix = page.get_pixmap(matrix=mat)
            # pix = page.get_pixmap()
            for pos in product(range(pix.width), range(pix.height)):
                if sum(pix.pixel(pos[0], pos[1])) >= 600:  # 将这里的600替换成要去除的水印rgb值
                    print(pix.pixel(pos[0], pos[1]))
                    # pix.set_pixel(pos[0], pos[1], 255, 255, 255)
                    pix.set_pixel(pos[0], pos[1], (255, 255, 255, 255))
            # 将去除水印后的图片保存到根文件夹下的PDFimages文件夹中，并以页码命名
            pix.pil_save(f"./PDFimages/{page_no}.png", dpi=(30000, 30000))
            print(f"第 {page_no} 页去除完成")
            page_no += 1

    @staticmethod
    def pictopdf():
        # 设置路径为去除水印后的图片保存路径
        pic_dir = "./PDFimages"
        pdf = fitz.open()
        img_files = sorted(os.listdir(pic_dir), key=lambda x: int(str(x).split(".")[0]))
        for img in img_files:
            print("正在合成", img)
            imgdoc = fitz.open(pic_dir + "/" + img)
            pdfbytes = imgdoc.convert_to_pdf()
            imgpdf = fitz.open("pdf", pdfbytes)
            pdf.insert_pdf(imgpdf)
        pdf.save("result.pdf")  # 保存的pdf名
        pdf.close()
        for img in os.listdir("PDFimages"):
            img = os.path.join("PDFimages", img)
            os.remove(img)


def main():
    if not os.path.exists(r"PDFimages"):
        os.mkdir("PDFimages")
    list_ = os.listdir("PDFimages")
    if list_:
        for img in list_:
            img = os.path.join("PDFimages", img)
            os.remove(img)
    if not os.path.exists(r"PDF"):
        os.mkdir("PDF")
    print("请将一个PDF文件放在PDF文件夹下")
    y = input("若完成上述步骤，请输入y即可去水印，去水印的结果为result.pdf文件。。。")
    if y == "y":
        obj = RemoveWatermark()
        obj.remove_pdfwatermark()
        obj.pictopdf()


if __name__ == "__main__":
    main()
