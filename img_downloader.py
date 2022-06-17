from urllib import request
import sys


def read_img_urls(filename):
    urls = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            urls.append(line.strip('\n'))
    return urls


def save_image(urls):
    for url in urls:
        request.urlretrieve(url, url.split('/')[-1])


def main():
    # standard check on the given arguments
    if len(sys.argv) == 2:
        urls = read_img_urls(sys.argv[1])
        save_image(urls)
    elif len(sys.argv) == 1:
        print(
            'Error! The script requires path to a file'
            'with image urls! Please re-run and specify')
    else:
        print(
            'Error! The script requires exactly one'
            'parameter - path to a file with images')


if __name__ == '__main__':
    main()
