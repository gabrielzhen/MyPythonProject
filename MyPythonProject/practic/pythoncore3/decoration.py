#decoration practis
from functools import wraps
def function_that_create_decorator(upper_case=False):  #动态生成装饰器，以便装饰器可以使用参数
    def a_function_that_expects_a_callback(the_callback):
        print('the function that expects acallback starts!')
        @wraps(the_callback)   #继承原有函数的元数据
        def a_dynamically_defined_function(*positional_params, **keyword_params): #添加参数以便被装饰函数可以使用参数
            if upper_case:
                print('THE DYNAMICALLY DEFINED FUNCTION STARTS!')
                result=the_callback(*positional_params, **keyword_params)
                print('THE DYNAMICALLY DEFINED FUNCTION STOPS!')
            else:
                print('the dynamically defined function starts!')
                result=the_callback(*positional_params, **keyword_params)
                print('the dynamically defined function stops!')

            return result
        print('the function that expects a callback stops!')
        return a_dynamically_defined_function
    return a_function_that_expects_a_callback

@function_that_create_decorator(True)
def a_normal_function(a,b=None):
    return str(a)
 
a_normal_function('aa','bb')