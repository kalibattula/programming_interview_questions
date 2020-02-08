# input : 1234
# output: one thousand two hundred thirty four

def numtowords(num):
    word = []
    dict_num = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    # print(dict_num[num%10])
    counter_dict = {2:"hundred",1:"ty",3:"thousand",4:"ten thousand"}
    counter = 0
    while(num>0):
        r = num%10
        num = num//10
        # print(r)
        if r != 0 :
            word.append(dict_num[r])
            if counter > 0:
                word.append(counter_dict[counter])
            counter+=1
    print(word)

numtowords(123)