
def tweets(num_of_input):
    list_of_cases = []

    for i in range(num_of_input):
        num_test_cases = int(input())
        test_case_list = []
        for j in range(num_test_cases):
            test_case_list.append(input().split(' ')[0])
        list_of_cases.append(test_case_list)

    list_dict = []
    for case in list_of_cases:
        dict_name_count = {}
        for test in case:
            dict_name_count[test] = case.count(test)
        list_dict.append(dict_name_count)
        
    for ls_dict in list_dict:
        for ele in sorted(ls_dict):
            if max(ls_dict.values()) == ls_dict[ele]:
                return ele,ls_dict[ele]

if __name__ == "__main__":
    n = int(input())
    print(tweets(n))


'''
i/p

1
4

sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4


o/p

('sachin', 2)

'''
