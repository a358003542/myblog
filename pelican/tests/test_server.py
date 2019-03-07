import os
from shutil import rmtree
from tempfile import mkdtemp

from six import BytesIO

from pelican.server import ComplexHTTPRequestHandler
from pelican.tests.support import unittest


class MockRequest(object):
    def makefile(self, *args, **kwargs):
        return BytesIO(b"")


class MockServer(object):
    pass


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = MockServer()
        self.temp_output = mkdtemp(prefix='pelicantests.')
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_output)

    def tearDown(self):
        rmtree(self.temp_output)
        os.chdir(self.old_cwd)

    def test_get_path_that_exists(self):

        handler = ComplexHTTPRequestHandler(MockRequest(), ('0.0.0.0', 8888),
                                            self.server)
        handler.base_path = self.temp_output

        os.mknod(os.path.join(self.temp_output, 'foo.html'))
        os.mkdir(os.path.join(self.temp_output, 'foo'))
        os.mknod(os.path.join(self.temp_output, 'foo', 'index.html'))

        os.mkdir(os.path.join(self.temp_output, 'bar'))
        os.mknod(os.path.join(self.temp_output, 'bar', 'index.html'))

        os.mkdir(os.path.join(self.temp_output, 'baz'))

        for suffix in ['', '/']:
            path = handler.get_path_that_exists('foo' + suffix)
            self.assertEqual(path, 'foo.html')

            path = handler.get_path_that_exists('bar' + suffix)
            self.assertEqual(path, 'bar/index.html')

            path = handler.get_path_that_exists('baz' + suffix)
            self.assertEqual(path, 'baz/')

            path = handler.get_path_that_exists('quux' + suffix)
            self.assertIsNone(path)
