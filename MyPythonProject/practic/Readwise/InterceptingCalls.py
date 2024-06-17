#https://www.bitecode.dev/p/xmas-decorations-part-3
#拦截通话示例
#第一次运行被执行，第二次执行检查缓存，
# 这种方法可以用于非常不同的场景：

#     Django, the web framework, uses it to check if a user is authenticated. If it is, the original function for the web page runs. If it isn't, the code for the login page runs instead.
#     Web 框架 Django 使用它来检查用户是否经过身份验证。如果是，则运行网页的原始功能。如果不是，则会运行登录页面的代码。

#     pydantic, the validation library, provides a decorator to check a function input. If the input matches the type hints, the original function runs. If it doesn't, pydantics raises an error instead.
#     pydantic，验证库，提供了一个装饰器来检查函数输入。如果输入与类型提示匹配，则运行原始函数。如果没有，pydantics 会引发错误。

#     call-throttle, a library to rate limit code, lets you cap a function to a number of call per seconds. If the limit is reached, the original function doesn't run at all.
#     call-throttle 是一个速率限制代码库，可让您将函数限制为每秒的调用次数。如果达到限制，则原始函数根本不会运行。

import time,functools

def basic_throttle(calls_per_second):
    def decorator(func):
        last_called=0,0
        count=0

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal last_called,count
            current_time=time.time()

            if current_time-last_called>=1:
                last_called=current_time
                count=0
            if count<calls_per_second:
                count+=1
                return func(*args,**kwargs)
            return None
        return wrapper
    return decorator