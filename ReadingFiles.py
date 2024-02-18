import os
from collections import Counter
import re
import socket

def list_files(directory):
    return os.listdir(directory)

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return len(words)
    
def top_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # words = re.split(r'[\s"‘,;:’“!.”’—:]+', text)
        words = [word.lower() for word in re.split(r'\s+|[^\w\s]+', text)]
        word_counts = Counter(words)
        word_counts.pop('', None)
        top_words = word_counts.most_common(3)
        return top_words

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Paths
data_dir = '/home/data'
result_dir = '/home/output'
result_file = os.path.join(result_dir, 'result.txt')

# Create output directory if it doesn't exist
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

files = list_files(data_dir)

if_words = count_words(os.path.join(data_dir, 'IF.txt'))

limerick_words = count_words(os.path.join(data_dir, 'Limerick-1.txt'))

total_words = sum(count_words(os.path.join(data_dir, file)) for file in files)

top_words_IF = top_words(os.path.join(data_dir, 'IF.txt'))

ip_address = get_ip_address()

with open(result_file, 'w') as f:
    f.write(f"List of files: {files}\n")
    f.write(f"Total number of words in IF.txt: {if_words}\n")
    f.write(f"Total number of words in Limerick-1.txt: {limerick_words}\n")  
    f.write(f"Total number of words: {total_words}\n")
    f.write(f"Top 3 words in IF.txt: {top_words_IF}\n")
    f.write(f"IP address of the machine: {ip_address}\n")

with open(result_file, 'r') as f:
    print(f.read())

