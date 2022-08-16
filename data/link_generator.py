import PyPDF2

for i in range(340, 545):
    file = open(f'{i}.pdf', 'rb')
    fileReader = PyPDF2.PdfFileReader(file)
    for j in range(fileReader.numPages):
        texts = fileReader.getPage(j).extractText().split('\n')
        for text in texts:
            if '【' in text:
                print(f'[{text}](data/{i}.pdf)  ')
