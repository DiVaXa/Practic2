import threading
import time

def write_words(word_count, file_name):
    with open(file_name,'w+', encoding='utf-8') as file:
        for number_word in range(1, word_count + 1):
            file.write(f'Какое-то слово №{number_word}' + '\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start_time_1 = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_1 = time.time()
thread_work_1 = round(end_time_1 - start_time_1, 3)
print(f'Время работы функций: {thread_work_1} сек')

start_time_2 = time.time()

thread1= threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time_2 = time.time()
thread_work_2 = round(end_time_2 - start_time_2, 3)
print(f'Время работы потоков: {thread_work_2} сек')