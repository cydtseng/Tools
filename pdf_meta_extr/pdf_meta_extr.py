import optparse
from PyPDF2 import PdfFileReader

def print_meta(file_name):
    pdf_file = PdfFileReader(open(file_name, 'rb'))
    document_info = pdf_file.getDocumentInfo()
    print('[*] Metadata for: ' + file_name)
    for meta_item in document_info:
        print('[+] ' + meta_item + ':' + document_info[meta_item])

def main():
    parser = optparse.OptionParser('usage %prog ' +\
            '-f <pdf>')
    parser.add_option('-f', dest='filename', type='string',
            help='specify pdf file name')
    (options, args) = parser.parse_args()
    file_name = options.filename
    if file_name == None:
        print(parser.usage)
        exit(0)
    else:
        print_meta(file_name)

if __name__ == '__main__':
    main()
