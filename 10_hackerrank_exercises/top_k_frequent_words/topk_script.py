import collections
import heapq

def count_words_freq(given_list: list) -> dict:
    str_given_list = [item for item in given_list if isinstance(item, str)]
    freq_dict = collections.Counter(str_given_list)  
    return freq_dict

def swap_order(freq_dict: dict) -> list:
    swapped = [(-count,word) for word, count in list(freq_dict.items())]
    return swapped


def find_k_most_freq_words (swapped: list, k:int) -> list:
    return heapq.nsmallest(k,swapped)


def output_top_k_most_freq_words(given_list:list, k:int) ->list:
    freq_dict = count_words_freq(given_list)
    swapped = swap_order(freq_dict)
    k_most_freq_words = find_k_most_freq_words(swapped,k)
    return [word for _, word in k_most_freq_words]
    

def print_individual_words(most_freq_words:list):
    for word in most_freq_words:
        print (word)





