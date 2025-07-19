def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("    |" * (nest - 1), end="")
    if nest > 0:
        print("    +---", end="")
    print(thisclass.__name__)
    
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest+1)
        
print_exception_tree(BaseException)


'''
Output:
BaseException
    +---BaseExceptionGroup
    |    +---ExceptionGroup
    +---Exception
    |    +---ArithmeticError
    |    |    +---FloatingPointError
    |    |    +---OverflowError
    |    |    +---ZeroDivisionError
    |    +---AssertionError
    |    +---AttributeError
    |    +---BufferError
    |    +---EOFError
    |    +---ImportError
    |    |    +---ModuleNotFoundError
    |    |    +---ZipImportError
    |    +---LookupError
    |    |    +---IndexError
    |    |    +---KeyError
    |    |    +---CodecRegistryError
    |    +---MemoryError
    |    +---NameError
    |    |    +---UnboundLocalError
    |    +---OSError
    |    |    +---BlockingIOError
    |    |    +---ChildProcessError
    |    |    +---ConnectionError
    |    |    |    +---BrokenPipeError
    |    |    |    +---ConnectionAbortedError
    |    |    |    +---ConnectionRefusedError
    |    |    |    +---ConnectionResetError
    |    |    +---FileExistsError
    |    |    +---FileNotFoundError
    |    |    +---InterruptedError
    |    |    +---IsADirectoryError
    |    |    +---NotADirectoryError
    |    |    +---PermissionError
    |    |    +---ProcessLookupError
    |    |    +---TimeoutError
    |    |    +---UnsupportedOperation
    |    |    +---itimer_error
    |    +---ReferenceError
    |    +---RuntimeError
    |    |    +---NotImplementedError
    |    |    +---RecursionError
    |    |    +---_DeadlockError
    |    |    +---BrokenBarrierError
    |    +---StopAsyncIteration
    |    +---StopIteration
    |    +---SyntaxError
    |    |    +---IndentationError
    |    |    |    +---TabError
    |    +---SystemError
    |    |    +---CodecRegistryError
    |    +---TypeError
    |    +---ValueError
    |    |    +---UnicodeError
    |    |    |    +---UnicodeDecodeError
    |    |    |    +---UnicodeEncodeError
    |    |    |    +---UnicodeTranslateError
    |    |    +---UnsupportedOperation
    |    +---Warning
    |    |    +---BytesWarning
    |    |    +---DeprecationWarning
    |    |    +---EncodingWarning
    |    |    +---FutureWarning
    |    |    +---ImportWarning
    |    |    +---PendingDeprecationWarning
    |    |    +---ResourceWarning
    |    |    +---RuntimeWarning
    |    |    +---SyntaxWarning
    |    |    +---UnicodeWarning
    |    |    +---UserWarning
    |    +---ExceptionGroup
    |    +---_OptionError
    +---GeneratorExit
    +---KeyboardInterrupt
    +---SystemExit
    '''
