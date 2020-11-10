import unittest
from basic.b import MathMethod
class TestMathMethod(unittest.TestCase):

    def test_add_two_positive(self):
        res=MathMethod(1,1).add()
        print("1+1的结果：",res)

    def test_add_two_zero(self):
        res=MathMethod(0,0).add()
        print("0+0的结果：",res)

    def test_add_two_nagative(self):
        res=MathMethod(-1,-2).add()
        print("-1+(-2)的结果：",res)

if __name__ == '__main__':
    unittest.main()