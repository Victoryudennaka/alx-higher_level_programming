import dis

def magic_calculation(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
        except:
            pass

        result = result + (a + b) ** i / i

    result = result + a + b

    return result

# Display the bytecode for the function
dis.dis(magic_calculation)
