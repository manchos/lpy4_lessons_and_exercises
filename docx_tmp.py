from docxtpl import DocxTemplate

doc = DocxTemplate("files/my_word_template.docx")
context = { 'company_name' : "World company" }
doc.render(context)
doc.save("files/generated_doc.docx")