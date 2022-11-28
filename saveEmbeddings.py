import cohere
import csv
import simpDataSets
import numpy as np
import time


# jokes_2018 = simpDataSets.depression_2018()


def saveEmbeddings(emb, fileName):
    pass


years = ['2018', '2019', 'pre', 'post']

if __name__ == '__main__':
    co = cohere.Client('kOJJBI5X12Dc0ElbxkgyjqrDNV6l3ps2CNnx6BFk')
    # for i in range(len(jokes_2018)):
    year = years[0]
    for year in years[1:len(years)]:
        df = None
        if year == '2018':
            df = simpDataSets.depression_2018()
        elif year == '2019':
            df = simpDataSets.depression_2019()
        elif year == 'pre':
            df = simpDataSets.depression_pre()
        elif year == 'post':
            df = simpDataSets.depression_post()
        jokes = list(df['post'])
        print("number of jokes: " + str(len(df)))

        startTime = time.time()
        for i in range(0, len(df), 98):
            stopingPoint = 0
            if (i + 98) > len(df):
                print("final loop")
                stopingPoint = len(df)
            else:
                stopingPoint = i + 97
            smallJokes = jokes[i:stopingPoint]
            print("embing depr ", i, " to ", stopingPoint)
            emb = list(co.embed(smallJokes))

            with open(f'embedings/depr_{year}/depr_{year}_' + str(i) + '.csv', 'w') as f:
                # using csv.writer method from CSV package
                write = csv.writer(f)

                write.writerow(np.arange(len(jokes)))
                write.writerows(emb)
                # print('saved file')
            print("saved file, sleeping for 60 seconds")
            time.sleep(60)

            hours = 3
            secondsInHours = 60 * 60 * hours
            if time.time() - startTime > secondsInHours:
                print("Breaking to finish in a resonable time")
                break
