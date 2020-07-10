import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation

# 读取分词csv文件
df = pd.read_csv("data_keywords.dat", encoding='utf-8', header=None, names=['content_cutted'])
print(df.content_cutted.head())

# 关键词提取和向量转换
vectorizer = CountVectorizer(strip_accents='unicode',

                             stop_words='english',

                             max_df=0.5,

                             min_df=10)

transformer = TfidfTransformer()
print('TF-IDF处理')
tfidf = transformer.fit_transform(vectorizer.fit_transform(df.content_cutted))  # TF-IDF
print(tfidf)
print('TF-IDF完成')

# LDA主题聚类
lda = LatentDirichletAllocation(max_iter=50,

                                learning_method='online',

                                learning_offset=50.,

                                random_state=0)

print('LDA处理')
lda.fit(tfidf)
print(tfidf)
print('LDA完成')


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)

        print(" ".join([feature_names[i]

                        for i in topic.argsort()[:-n_top_words - 1:-1]]))

    print()


n_top_words = 20

tf_feature_names = vectorizer.get_feature_names()

print_top_words(lda, tf_feature_names, n_top_words)

doc = lda.transform(tfidf)
fo=open('doc.txt','a+')
for line in doc:
    fo.write(str(line))
    fo.write('\n')

