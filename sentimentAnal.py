import csv

import simpDataSets

# deprSent2018 = simpDataSets.depression_2018_sentiment()
# deprSent2019 = simpDataSets.depression_2019_sentiment()
# deprSentPre = simpDataSets.depression_pre_sentiment()
# deprSentPost = simpDataSets.depression_post_sentiment()
print('loading datasets')
deprSentiment = simpDataSets.all_jokes_sentiment()
averages = []
# print(deprSentiment[0][0].keys())
for lst in deprSentiment:
    pos = 0
    neu = 0
    neg = 0
    comp = 0
    lenOflst = len(lst)
    print("lengh of list: ", lenOflst)
    for dic in lst:
        # print(dic)
        # print(dic['pos'], type(dic['pos']))
        try:
            pos += dic['pos']
            neu += dic['neu']
            neg += dic['neg']
            comp += dic['compound']
        except:
            print("failed for " + str(dic))
    print('totalPOS: ', pos)
    pos /= lenOflst
    neg /= lenOflst
    neu /= lenOflst
    comp /= lenOflst
    averages.append({'pos': pos, 'neu': neu, 'neg': neg, 'compound': comp})

keys = averages[0].keys()
with open('ModifedData/JokesSentimentAverage.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(averages)

print(averages)
