def custom_write(file_name, strings):
    file_name = 'test.txt'
    n = 1
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in info:
        bute_tell = file.tell()
        file.write(f'{i}\n')
        strings_positions[(n, bute_tell)] = i
        n += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for strings_positions in result.items():
        print(strings_positions)
