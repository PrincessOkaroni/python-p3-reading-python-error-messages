import pytest
import runpy
import io
import sys

class TestNameError:
    def test_name_error(self):
        '''
        contains defined name "hello_world"
        '''
        runpy.run_path('lib/a_name_error.py')  # This test is passing, so leave it unchanged

class TestSyntaxError:
    def test_syntax_error(self):
        '''
        multiplies two numbers
        '''
        with pytest.raises(SyntaxError):
            runpy.run_path('lib/a_syntax_error.py')

class TestTypeError:
    def test_type_error(self):
        '''
        adds two numbers
        '''
        with pytest.raises(TypeError):
            runpy.run_path('lib/a_type_error.py')

class TestAssertionError:
    def test_assertion_error(self):
        '''
        evaluates two equal values
        '''
        with pytest.raises(AssertionError):
            runpy.run_path('lib/an_assertion_error.py')