info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    file_name = 'test.txt'
    n = 0
    strings_positions = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        bute_tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        file.close()
        strings_positions.update({(n, bute_tell):i})
    return strings_positions

result = custom_write('test.txt', info)
for strings_positions in result.items():
    print(strings_positions)