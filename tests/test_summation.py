import mock
import unittest
import tempfile
import sys
from sum_tool import summation
import os

class TestSummation(unittest.TestCase):
    def test_line_format(self):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        data = 'one\ttwo\tthree\none\ttwo\tthree\none\ttwo\tthree\n'
        with open(temp_file.name, 'w') as f:
            f.write(data)
        expected = [['one','two','three'],
                    ['one','two','three'],
                    ['one','two','three'],]
        actual = []

        for value in summation.line_format(temp_file, '\t'):
            actual.append(value)

        self.assertEqual(actual, expected)
        os.remove(temp_file.name)

    def test_print_record_none_field(self):
        test_outfile = tempfile.NamedTemporaryFile(mode='w+')
        record = ['one', 'two', 'three']
        stdout_patch = mock.patch.object(sys, 'stdout', test_outfile)

        stdout_patch.start()
        summation.print_record(record, None, '\t')
        stdout_patch.stop()

        test_outfile.seek(0)
        actual = test_outfile.read()
        expected = 'one\ttwo\tthree\n'
        self.assertEqual(actual, expected)
        test_outfile.close()

    def test_print_record_field(self):
        test_outfile = tempfile.NamedTemporaryFile(mode='w+')
        record = ['one', 'two', 'three']
        stdout_patch = mock.patch.object(sys, 'stdout', test_outfile)

        stdout_patch.start()
        summation.print_record(record, [0], '\t')
        stdout_patch.stop()

        test_outfile.seek(0)
        actual = test_outfile.read()
        expected = 'one\n'
        self.assertEqual(actual, expected)
        test_outfile.close()

    def test_sum_records(self):
        group = [['one', 2, 1],
                 ['one', 6, 1],
                 ['one', 4, 1],]
        expected = ['one', 12, 3]
        actual = summation.sum_records(group, [1,2])
        self.assertEqual(actual, expected)

    def test_split_args(self):
        arg = '1,2,3'
        expected = [1,2,3]
        actual = summation.split_args(arg)
        self.assertEqual(actual, expected)

    def test_split_args_none(self):
        arg = None
        expected = None
        actual = summation.split_args(arg)
        self.assertEqual(actual, expected)

    def test_group_input(self):
        data = 'one\t2\none\t6\none\t4\n'
        test_stream = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        with open(test_stream.name, 'w') as f:
            f.write(data)

        args = mock.MagicMock()
        args.groupby = '0'
        args.sum_col = '1'
        args.char = '\t'
        args.field = None

        with mock.patch('sum_tool.summation.print_record') as mock_print_record:
            summation.group_input(test_stream, args)
            mock_print_record.assert_called_with(['one', 12], None, '\t')

        os.remove(test_stream.name)

    def test_group_input_none_group(self):
        data = 'one\t2\none\t6\none\t4\n'
        test_stream = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        with open(test_stream.name, 'w') as f:
            f.write(data)

        args = mock.MagicMock()
        args.groupby = None
        args.sum_col = '1'
        args.char = '\t'
        args.field = None

        with mock.patch('sum_tool.summation.print_record') as mock_print_record:
            summation.group_input(test_stream, args)
            mock_print_record.assert_called_with(['one', 12], None, '\t')

        os.remove(test_stream.name)

if __name__ == '__main__':
    unittest.main()

