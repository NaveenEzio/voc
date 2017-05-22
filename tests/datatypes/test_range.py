from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class RangeTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = range(0, 5)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[3] = ", x[3])
            print("x[-1] = ", x[-1])
            try:
                print("x[5] = ", x[5])
            except IndexError as err:
                print(err)
            """)

    def test_step(self):
        self.assertCodeExecution("""
            x = range(0, 5, 2)
            print("x[0] = ", x[0])
            print("x[1] = ", x[1])
            print("x[-1] = ", x[-1])
            print("x[-3] = ", x[-3])
            try:
                print("x[3] = ", x[3])
            except IndexError as err:
                print(err)
            try:
                print("x[5] = ", x[5])
            except IndexError as err:
                print(err)
            try:
                print("x[-4] = ", x[-4])
            except IndexError as err:
                print(err)

            y = range(7, 1, -3)
            print("y[0] = ", y[0])
            print("y[1] = ", y[1])
            print("y[-2] = ", y[-2])
            """)

    def test_zero_step(self):
        self.assertCodeExecution("""
            try:
                range(0, 5, 0)
            except ValueError as err:
                print(err)
        """)

    def test_len_empty(self):
        self.assertCodeExecution("""
            print(len(range(5, 5)))
        """)

    def test_len_positive_step(self):
        self.assertCodeExecution("""
            print(len(range(5, 0, 1)))
        """)

    def test_len_negative_step(self):
        self.assertCodeExecution("""
            print(len(range(0, 5, -1)))
        """)

    def test_multiple_iterators(self):
        self.assertCodeExecution("""
            r = range(0, 10)
            print(list(r))
            print(list(r))
        """)

    def test_iterator_iterator(self):
        self.assertCodeExecution("""
            r = range(0, 10)
            i = iter(r)
            print(next(i))
            print(next(iter(i)))
            print(r)
        """)


class UnaryRangeOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'range'


class BinaryRangeOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [



        'test_direct_eq_range',
        'test_direct_ne_range',

        'test_eq_class',
        'test_eq_range',

        'test_ge_class',

        'test_gt_class',

        'test_le_class',


        'test_lt_class',

        'test_modulo_complex',

        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_list',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_ne_class',
        'test_ne_range',




        'test_subscr_bool',
        'test_subscr_bytearray',
        'test_subscr_bytes',
        'test_subscr_class',
        'test_subscr_complex',
        'test_subscr_dict',
        'test_subscr_float',
        'test_subscr_frozenset',
        'test_subscr_list',
        'test_subscr_None',
        'test_subscr_NotImplemented',
        'test_subscr_range',
        'test_subscr_set',
        'test_subscr_slice',
        'test_subscr_str',
        'test_subscr_tuple',



    ]


class InplaceRangeOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'range'

    not_implemented = [




        'test_modulo_complex',







    ]
