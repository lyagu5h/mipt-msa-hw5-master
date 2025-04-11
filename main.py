import requests
import time
import tracemalloc

tracemalloc.start()

start = time.perf_counter()

def get_text(url):
    response = requests.get(url)
    return response.text

def clean_text(text):
    cleaned_text = ''
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned_text += ch.lower()
        else:
            cleaned_text += ' '
    return cleaned_text.split()

def count_word_frequencies(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
    
def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]

    raw_text = get_text(url)
    cleaned_text = clean_text(raw_text)
    freq = count_word_frequencies(cleaned_text)

    for word in words:
        if word in freq:
            print(f"{word}: {freq[word]}")

    
if __name__ == "__main__":
    main()

end = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения6: {end - start:0.4f} секунд")
print(f"Текущая память: {current / 10**6} МБ")
print(f"Пик памяти: {peak / 10**6} МБ")