from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer

corpus=['I like great basketball game',
        'This video game is the best action game I have ever played',
        'i really really like basketball',
        'how about this movie? is the plot great?',
        'do you like RPG game?',
        'you can try this FPS game',
        'the movie is really great,so great! i enjoy the plot'
        ]

vectorizer=CountVectorizer()
vectors=vectorizer.fit_transform(corpus)
ftransformer=TfidfTransformer()
ftidf=ftransformer.fit_transform(vectors)


print('所有词条')
print(vectorizer.get_feature_names_out())
print('\n')

print(ftidf)