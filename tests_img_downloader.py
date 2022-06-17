import unittest
import os.path
import img_downloader
import glob
import validators


class TestImgDownloader(unittest.TestCase):
    def testFile_exists(self):
        self.assertEqual(os.path.exists('images.txt'), True)

    def testUrls_are_read(self):
        urls = ['https://pandas.pydata.org/static/img/partners/ursa_labs.svg',
                'https://pandas.pydata.org/static/img/partners/dfine.svg',
                'https://pandas.pydata.org/static/img/partners/numfocus.svg']
        self.assertEqual(img_downloader.read_img_urls('images.txt'), urls)

    def testUrls_valid(self):
        urls = img_downloader.read_img_urls('images.txt')
        for url in urls:
            self.assertEqual(validators.url(url), True)

    def testFiles_saved(self):
        files = ['ursa_labs.svg', 'dfine.svg', 'numfocus.svg']
        saved_imgs = glob.glob('*.svg')
        self.assertCountEqual(saved_imgs, files)


if __name__ == '__main__':
    unittest.main()
