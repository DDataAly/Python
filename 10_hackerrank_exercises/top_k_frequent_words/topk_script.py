import collections
import heapq 
import pandas as pd

# Option 1 - Heap solution

def count_words_freq(given_list: list) -> dict:
    str_given_list = [item for item in given_list if isinstance(item, str)]
    freq_dict = collections.Counter(str_given_list)  
    return freq_dict

def swap_order(freq_dict: dict) -> list:
    swapped = [(-count,word) for word, count in list(freq_dict.items())]
    return swapped


def find_k_most_freq_words (swapped: list, k:int) -> list:
    return heapq.nsmallest(k,swapped)


def list_k_most_freq_words(given_list:list, k:int) ->list:
    freq_dict = count_words_freq(given_list)
    swapped = swap_order(freq_dict)
    k_most_freq_words = find_k_most_freq_words(swapped,k)
    return [word for _, word in k_most_freq_words]
    

def print_individual_words(most_freq_words:list,k:int):
    if len(most_freq_words) < k:
        print (f'Number of unique strings in the given list is less than k = {k}')
    print('Most frequent words are: ')     
    for word in most_freq_words:
        print (word)

#Option 2 - Pandas solution

def count_words_freq(given_list: list) -> dict:
    str_given_list = [item for item in given_list if isinstance(item, str)]
    freq_dict = collections.Counter(str_given_list)  
    return freq_dict


def get_top_k(freq_dict, k):
    dict_for_df = {'word': list(freq_dict.keys()),'frequency':list(freq_dict.values())}
    freq_df = pd.DataFrame(dict_for_df)
    freq_df.sort_values(by =['frequency', 'word'], ascending=[False, True], inplace =  True)
    top_k_words = freq_df['word'].head(k+1).tolist()
    return top_k_words


if __name__=='__main__':
    k = 3
    given_list = [10, 9, 'cat', 'cat', 'dog', 'dog','i','i','i', 'rose','rose','rose']
    freq_dict = count_words_freq(given_list)
    top_k_words = list_k_most_freq_words(given_list, k)  #Option 1 -comment out for Opt 2
    top_k_words = get_top_k(freq_dict,2)  #Option 2 -comment out for Opt 1
    
    print_individual_words(top_k_words,k)


