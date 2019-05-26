'''
This is a test harness for a beaufort cipher decoder
Place your function(s) here and run it.

please, name your function(s) as:
<your_name>_<suffix_you_define>
'''


def test_func(func):
    import math
    import inspect

    def score(code_lines):
        if code_lines <= 3:
            return 'A+'
        if code_lines <= 7:
            return 'A'
        if code_lines <= 12:
            return 'B'
        if code_lines <= 16:
            return 'C'
        if code_lines <= 20:
            return 'D'
        if 21 < code_lines:
            return 'F'
        else:
            return 'unknown'

    tests = [('YJTWPWAYHIXZPM', 'PYTHON', 'SPAM_SPAM_SPAM'),
             ('IJVAHZHPFGJPW_QQT', 'ARM_IS_OFF', 'TIS_BUT_A_SCRATCH'),
             ('YAQZFSX', 'CRUCIFIXION', 'FREEDOM'),
             ('GXCHVFFAJHUOPQPQLYT', 'NAUGHTY_BOY', 'HES_NOT_THE_MESSIAH'),
             ('N_PHW_AHXFVHTYKEAJSGEHWLMTD_KI_BFJJELOJL_ALAWIHWBKQNH',
              'KNIGHTS_WHO_SAY_NI',
              'YOU_MUST_CUT_DOWN_THE_MIGHTIEST_TREE___WITH_A_HERRING')
             ]
    results = []

    print(f'\n\nTesting function: {func.__name__}\n')
    print('-----------')
    for message, key, expected in tests:
        print(f'Testing: {message}')
        print(f'Key: {key}')
        try:
            result = func(message, key)
        except (ValueError, TypeError) as errmsg:
            print(f'Error raised by function: {errmsg}')
            results.append(False)
        else:
            try:
                assert result == expected
            except AssertionError:
                print(f'expected {expected}\nreceived {result}')
                print('---Failed!\n')
                results.append(False)
            else:
                print(f'Message: {result}')
                print('---Passed!\n')
                results.append(True)

        print('-----------')
    if all(results):
        print('\nAll Tests Passed!')

        func_code = inspect.getsource(func)
        func_code_lines = []
        func_code_line = []
        for char in func_code:
            if char != '\n':
                func_code_line.append(char)
            else:
                func_code_lines.append(''.join(func_code_line))
                func_code_line = []

        count = 0
        for line in func_code_lines:
            if line:
                line = line.lstrip(' ')
                if func.__name__ in line:
                    continue
                if line[0] == '#':
                    continue
                if len(line) > 1:
                    line_count = math.ceil(len(line)/72)
                    count += line_count
                if 'return' in line:
                    count -= 1

        print(f'Code Line Count: {count}')
        print(f'Rating: "{score(count)}"')

    else:
        print('\nTest Failed!')
    print('-----------\n')


if __name__ == '__main__':
    func_list = [func for name, func in globals().items()
                 if callable(func) and name[0:2] not in '__'
                 and name[0:4] not in ('exit', 'quit', 'get_', 'test')]

    for func in func_list:
        test_func(func)
