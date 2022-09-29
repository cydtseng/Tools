import zipfile as zf
import optparse as optp
from threading import Thread

def crack(the_file, password):
    try:
        the_file.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog " +\
            "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
            help='specify a zip file')
    parser.add_option('-d', dest='dname', type='string',\
            help='specify dictionary file')
    (options, args) = parse.parse_args()

    if (options.zname == None || options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        file_to_crack = zf.ZipFile(zname)
        dict_file = open(dname)
        for line in dict_file.readlines():
            password = line.strip('\n')
            # start a new thread to crack file with diff password
            t = Thread(target=crack, args=(file_to_crack, password))
            t.start()

if __name__ == '__main__':
    main()
