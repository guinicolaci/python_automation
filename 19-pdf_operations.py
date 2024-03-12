# import PyPDF2 as pdf
# from PyPDF2 import PdfReader

# def get_pdf_metadata(pdf_path):
#     with open(pdf_path, "rb") as f:
#         reader = PdfReader(f)
#         info = reader.metadata
#     return info

# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, "rb") as f:
#         reader = PdfReader(f)
#         results = []
#         for i in range(0, len(reader.pages)):
#             selected_page = reader.pages[i]
#             text = selected_page.extract_text()
#             results.append(text)
#         return ' '.join(results)

# print(get_pdf_metadata("files/test_pdf.pdf"))
# print(get_pdf_metadata("files/test_pdf.pdf").title)
# print(get_pdf_metadata("files/test_pdf.pdf").author)

# print(extract_text_from_pdf("files/test_pdf.pdf"))
# print(extract_text_from_pdf("files/sample.pdf"))





# import PyPDF2 as pdf
# from PyPDF2 import PdfReader

# def fetch_all_pdf_files(parent_folder:str):
#     target_files = []
#     for path, subdirs, files in os.walk(parent_folder):
#         for name in files:
#             if name.endswith(".pdf"):
#                 target_files.append(os.path.join(path,name))
#     return target_files

# def merge_pdf(list_pdfs, output_filename="files/final_pdf.pdf"):
#     merger = PdfMerger()
#     with open(output_filename, "wb") as f:
#         for file in list_pdfs:
#             merger.append(file)
#         merger.write(f)

# print(fetch_all_pdf_files("files/"))

# pdf_list = fetch_all_pdf_files("files/")
# merge_pdf(pdf_list)





# import PyPDF2 as pdf
# from PyPDF2 import PdfReader

# def rotate_pdf(pdf_path, page_num:int, rotation:int=90):
#     with open(pdf_path, "rb") as f:
#         reader = PdfReader(f)
#         writer = PdfWriter()
#         writer.add_page(reader.pages[page_num])
#         writer.pages[page_num].rotate(rotation)
#         filename = os.path.split(pdf_path)[1]
#         output_filename = f"files/{filename}_{rotation}_rotated_page.pdf"
#         with open(output_filename, "wb") as out:
#             writer.write(out)

# rotate_pdf("files/sample.pdf", 0)






# import PyPDF2 as pdf
# from PyPDF2 import PdfReader

# def extract_images_from_pdf(pdf_path):
#     with open(pdf_path, "rb") as f:
#         reader = PdfReader(f)
#         for page_num in range(0, len(reader.pages)):
#             selected_page = reader.pages[page_num]
#             for img_file_obj in selected_page.images:
#                 with open(f"files/{img_file_obj.name}", "wb") as out:
#                     out.write(img_file_obj.data)

# extract_images_from_pdf("files/test_pdf_image.pdf")







# import PyPDF2 as pdf
# from PyPDF2 import PdfReader
# from PIL import Image

# def convert_img_pdf(image_file):
#     my_image = Image.open(image_file)
#     img = my_image.convert("RGB")
#     filename = f"{os.path.splitext(image_file)[0]}.pdf"
#     img.save(filename)

# convert_img_pdf("files/IM14.jpg")