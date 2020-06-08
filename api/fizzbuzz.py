def fizzbuzz(n: int) -> str:
    # n を指定したときにfizzbuzzの文字列を返す
    if 0 >= n:
        raise ValueError
    return ','.join(_nth_fizzbuzz(i) for i in range(1, n + 1))


def _nth_fizzbuzz(n: int) -> str:
    # n番目のfizzbuzzの出力
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return f'{n}'


if __name__ == '__main__':
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(2) == '1,2'
    assert fizzbuzz(3) == '1,2,Fizz'
    assert fizzbuzz(4) == '1,2,Fizz,4'
    assert fizzbuzz(5) == '1,2,Fizz,4,Buzz'
    assert fizzbuzz(15) == '1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz'
    assert fizzbuzz(16) == '1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16'
