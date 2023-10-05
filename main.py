import re

def process_text(input_text):

    sentences = re.split(r'(?<=[.!?])\s+', input_text)
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    processed_text = ' '.join(capitalized_sentences)

    digit_count = sum(1 for char in processed_text if char.isdigit())

    punctuation_count = sum(1 for char in processed_text if char in '.,;!?')

    exclamation_count = processed_text.count('!')

    return processed_text, digit_count, punctuation_count, exclamation_count

input_text = "не важно о чем. тоже не важно! і 123, ок 5."

processed_text, digit_count, punctuation_count, exclamation_count = process_text(input_text)
print("Змінений текст:")
print(processed_text)
print("Кількість цифр у тексті:", digit_count)
print("Кількість розділових знаків у тексті:", punctuation_count)
print("Кількість знаків оклику у тексті:", exclamation_count)
