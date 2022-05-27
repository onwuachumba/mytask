# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import os
BASE_DIR_=os.getcwd()
#print(BASE_DIR_)
my_working_dir="c:/Users/hp/Desktop/mytask/reading_text"
os.chdir(my_working_dir)
def read_file_content(filename):
    # [assignment] Add your code here 
    my_file=open(filename)
    read_file= my_file.read() 
    print(read_file)
    my_file.close()  
    return read_file
#read_file_content("story.txt")    


def count_words():
    text = read_file_content("story.txt")
    print(type(text))
    # [assignment] Add your code here
    count_1=text.count("As")
    count_2=text.count("would")
    my_key_1= "as"
    my_key_2="would"
    dict_count= {}
    dict_count['as']=count_1
    dict_count['would']=count_2

    print(dict_count)
    return dict_count
count_words()