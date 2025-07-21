import pytest
import copy
from topk_script import count_words_freq, swap_order, output_top_k_most_freq_words,find_k_most_freq_words

@pytest.mark.describe("count_words_freq returns a dictionary with the words frequency")
class TestCountsWordFrequency:
    @pytest.mark.it('should be pure function')
    def test_does_not_modify_given_list(self):
        given_list = ['cats','lilies']
        deep_copy_of_given_list = copy.deepcopy(given_list)
        count_words_freq(given_list)
        assert given_list == deep_copy_of_given_list
    
    @pytest.mark.it('should return a dictionary')
    def test_returns_dictionary(self):
        given_list = ['cats','lilies']
        assert isinstance(count_words_freq (given_list), dict)

    @pytest.mark.it('returns a correct dictionary if given one word list')
    def test_returns_correct_dictionary_for_one_word_list(self):
        given_list = ['cats']
        assert count_words_freq(given_list) == {'cats':1}  

    @pytest.mark.it('returns a correct dictionary for a list with many words')
    def test_returns_correct_dictionary_for_many_words_list(self):
        given_list =['cat','dig','cat','dig','nanny','roses','maybe','cat']
        assert count_words_freq(given_list) == {'nanny': 1, 'cat': 3, 'dig': 2, 'roses': 1, 'maybe': 1} 

    @pytest.mark.it('ignores non-string items in the given list')
    def test_returns_correct_dictionary_for_list_with_non_str(self):
        given_list =['cat','dig','cat','dig',8, ['a'],'roses','maybe','cat']
        assert count_words_freq(given_list) == {'cat': 3, 'dig': 2, 'roses': 1, 'maybe': 1}  
     
@pytest.mark.describe("swap_order returns a list of tuples of (-frequency_of_word_in_given_list, word)")
class TestSwapOrder:
    @pytest.mark.it('should return a list of tuples')
    def test_returns_correct_data_formats(self):
        given_list = [6,'apple', 'banana', 'apple', 'banana', 'carrot', 'carrot',2]
        freq_dict = count_words_freq(given_list)
        assert isinstance(swap_order(freq_dict), list)
        assert isinstance(swap_order(freq_dict)[0], tuple)

    @pytest.mark.it('swaps the frequency of the word with the word itself in each tuple')
    def test_returns_swap_element_in_tuple(self):
        given_list = [6,'apple', 'banana', 'apple', 'banana', 'carrot', 'carrot',2]
        freq_dict = count_words_freq(given_list)
        assert freq_dict=={'apple':2, 'banana':2, 'carrot':2}
        assert swap_order(freq_dict) == [(-2,'apple'), (-2,'banana'), (-2,'carrot')]
    

@pytest.mark.describe("find_k_most_freq_words returns the correct list")
class TestFindKWords:
    @pytest.mark.it('returns the correct number of words')
    def test_returns_correct_num_words(self):
        k=2
        given_list_1=[5,'zebra', 'apple', 'mango', 'banana', 'kiwi',2]
        assert len(find_k_most_freq_words(given_list_1, k)) == 2

        given_list_2=[5,'zebra', 'zebra','zebra','zebra','zebra','zebra','zebra']
        assert len(output_top_k_most_freq_words(given_list_2, k)) == 1





# @pytest.mark.describe("output_top_k_most_freq_words ")


  