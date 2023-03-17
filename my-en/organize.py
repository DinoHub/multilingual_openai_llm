
with open('clean.my-en', 'r', encoding='utf-8') as f:
    burmese_sentence = ''
    previous = False
    for line in f:
        line = line.strip()
        if line.startswith('Burmese:'):
            burmese_sentence = line[len('Burmese:'):].strip()
            if previous:
                print(line)
            previous = True
        elif line.startswith('English:') and burmese_sentence:
            english_sentence = line[len('English:'):].strip()
            # Do something with the Burmese and English sentences, such as printing or writing to a file
            with open('gpt_burm.my', 'a', encoding='utf-8') as f_out:
                f_out.write(burmese_sentence + '\n')
            with open('gpt_burm.en', 'a', encoding='utf-8') as f_out:
                f_out.write(english_sentence + '\n')
            burmese_sentence = ''
            previous = False

        else:
            burmese_sentence = ''
            print(line)