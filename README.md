
# Sentiment analysis of customer reviews (Ukrainian)

### Get started

Create anaconda environmentfor the project:

`conda create --name <env> --file requirements.txt`



### Content

1. [Tool testing](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/01-tools-testing)
2. [Data collections](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/02-data-collections)
3. [Data preparation](https://github.com/OleksandrKosovan/sentiment-analysis-uk)
4. [Visualizations](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/04-statistics-visualizations)
5. [ML modeling](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/05-modeling)
6. [Scientific publications](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/06-scientific-work)
7. [Final script](https://github.com/OleksandrKosovan/sentiment-analysis-uk/tree/master/07-final-approach)

### Results

I made master's thesis and few publication based on this reseacrh.

Results of machine learning modeling.


**TF-IDF & Lematization results**

| №   | Model name             | precision | recall | accuracy | f1-score |
|-----|------------------------|-----------|--------|----------|----------|
| 1.  | BernoulliNB            | 0.55      | 0.55   | 0.55     | 0.54     |
| 2.  | Decision Tree          | 0.59      | 0.59   | 0.62     | 0.59     |
| 3.  | Extra Tree             | 0.68      | 0.70   | 0.70     | 0.67     |
| 4.  | KNN                    | 0.65      | 0.68   | 0.68     | 0.65     |
| 5.  | Linear SVC             | 0.73      | 0.73   | 0.73     | 0.69     |
| 6.  | Logistic Regression CV | 0.74      | 0.75   | 0.75     | 0.74     |
| 7.  | MLP                    | 0.73      | 0.73   | 0.73     | 0.73     |
| 8.  | Random Forest          | 0.68      | 0.69   | 0.69     | 0.68     |
| 9.  | Ridge                  | 0.73      | 0.74   | 0.74     | 0.72     |
| 10. | Ridge CV               | 0.73      | 0.74   | 0.74     | 0.72     |
| 11. | SVC                    | 0.44      | 0.66   | 0.66     | 0.53     |
| 12. | GBC                    | 0.72      | 0.73   | 0.73     | 0.72     |
| 13. | Linear SVC 2           | 0.73      | 0.74   | 0.74     | 0.73     |
| 14. | Logistic Regression    | 0.74      | 0.71   | 0.71     | 0.64     |
| 15. | SGDC                   | 0.73      | 0.74   | 0.74     | 0.73     |
| 16. | Perceptron             | 0.67      | 0.34   | 0.34     | 0.18     |
| 17. | PAC                    | 0.72      | 0.72   | 0.72     | 0.72     |

**TF-IDF & Stemming results**

|     |                        |           |        |          |          |
|-----|------------------------|-----------|--------|----------|----------|
| №   | Model name             | precision | recall | accuracy | f1-score |
| 1.  | BernoulliNB            | 0.55      | 0.52   | 0.52     | 0.52     |
| 2.  | Decision Tree          | 0.62      | 0.62   | 0.62     | 0.62     |
| 3.  | Extra Tree             | 0.67      | 0.68   | 0.68     | 0.62     |
| 4.  | KNN                    | 0.60      | 0.63   | 0.63     | 0.60     |
| 5.  | Linear SVC             | 0.71      | 0.63   | 0.63     | 0.50     |
| 6.  | Logistic Regression CV | 0.71      | 0.72   | 0.72     | 0.71     |
| 7.  | MLP                    | 0.71      | 0.72   | 0.72     | 0.70     |
| 8.  | Random Forest          | 0.68      | 0.68   | 0.68     | 0.64     |
| 9.  | Ridge                  | 0.69      | 0.69   | 0.69     | 0.65     |
| 10. | Ridge CV               | 0.69      | 0.69   | 0.69     | 0.65     |
| 11. | SVC                    | 0.68      | 0.65   | 0.65     | 0.54     |
| 12. | GBC                    | 0.70      | 0.71   | 0.71     | 0.70     |
| 13. | Linear SVC 2           | 0.71      | 0.71   | 0.71     | 0.69     |
| 14. | Logistic Regression    | 0.67      | 0.65   | 0.65     | 0.54     |
| 15. | SGDC                   | 0.68      | 0.67   | 0.67     | 0.61     |
| 16. | Perceptron             | 0.68      | 0.67   | 0.67     | 0.59     |
| 17. | PAC                    | 0.69      | 0.53   | 0.53     | 0.51     |

**TF-IDF & Lematization and bigram results**

|     |                        |           |        |          |          |
|-----|------------------------|-----------|--------|----------|----------|
| №   | Model name             | precision | recall | accuracy | f1-score |
| 1.  | BernoulliNB            | 0.74      | 0.72   | 0.72     | 0.72     |
| 2.  | Decision Tree          | 0.67      | 0.67   | 0.67     | 0.67     |
| 3.  | Extra Tree             | 0.73      | 0.73   | 0.73     | 0.70     |
| 4.  | KNN                    | 0.71      | 0.70   | 0.70     | 0.66     |
| 5.  | Linear SVC             | 0.80      | 0.80   | 0.80     | 0.78     |
| 6.  | Logistic Regression CV | 0.81      | 0.81   | 0.81     | 0.81     |
| 7.  | MLP                    | 0.78      | 0.79   | 0.79     | 0.78     |
| 8.  | Random Forest          | 0.72      | 0.73   | 0.73     | 0.71     |
| 9.  | Ridge                  | 0.80      | 0.80   | 0.80     | 0.79     |
| 10. | Ridge CV               | 0.80      | 0.80   | 0.80     | 0.79     |
| 11. | SVC                    | 0.41      | 0.64   | 0.64     | 0.50     |
| 12. | GBC                    | 0.79      | 0.79   | 0.79     | 0.78     |
| 13. | Linear SVC 2           | 0.80      | 0.80   | 0.80     | 0.80     |
| 14. | Logistic Regression    | 0.79      | 0.76   | 0.76     | 0.73     |
| 15. | SGDC                   | 0.81      | 0.81   | 0.81     | 0.80     |
| 16. | Perceptron             | 0.80      | 0.79   | 0.79     | 0.78     |
| 17. | PAC                    | 0.80      | 0.80   | 0.80     | 0.80     |


**TF-IDF & Stemming and bigram results**


|     |                        |           |        |          |          |
|-----|------------------------|-----------|--------|----------|----------|
| №   | Model name             | precision | recall | accuracy | f1-score |
| 1.  | BernoulliNB            | 0.66      | 0.64   | 0.64     | 0.64     |
| 2.  | Decision Tree          | 0.64      | 0.64   | 0.64     | 0.64     |
| 3.  | Extra Tree             | 0.76      | 0.71   | 0.71     | 0.67     |
| 4.  | KNN                    | 0.62      | 0.64   | 0.64     | 0.56     |
| 5.  | Linear SVC             | 0.79      | 0.77   | 0.77     | 0.75     |
| 6.  | Logistic Regression CV | 0.79      | 0.79   | 0.79     | 0.79     |
| 7.  | MLP                    | 0.77      | 0.78   | 0.78     | 0.77     |
| 8.  | Random Forest          | 0.75      | 0.73   | 0.73     | 0.70     |
| 9.  | Ridge                  | 0.77      | 0.76   | 0.76     | 0.75     |
| 10. | Ridge CV               | 0.77      | 0.76   | 0.76     | 0.75     |
| 11. | SVC                    | 0.79      | 0.76   | 0.76     | 0.74     |
| 12. | GBC                    | 0.78      | 0.78   | 0.78     | 0.77     |
| 13. | Linear SVC 2           | 0.78      | 0.78   | 0.78     | 0.77     |
| 14. | Logistic Regression    | 0.75      | 0.70   | 0.70     | 0.64     |
| 15. | SGDC                   | 0.79      | 0.77   | 0.77     | 0.75     |
| 16. | Perceptron             | 0.75      | 0.58   | 0.58     | 0.56     |
| 17. | PAC                    | 0.79      | 0.78   | 0.78     | 0.77     |

**Difference between text preparation approaches**

| Text preparation approach | Avg. f1-score | < 0,7 | >=0,7<0,8 | >=0,8 |
|---------------------------|---------------|-------|-----------|-------|
| Lematization              | 0,65          | 9     | 8         | 0     |
| Stemming                  | 0,61          | 14    | 3         | 0     |
| Lematization & bigram     | 0,74          | 3     | 10        | 4     |
| Stemming & bigram         | 0,71          | 6     | 11        | 0     |

**Avg. results per ML model**

| №   | Model name             | Avg. F1-score |
|-----|------------------------|---------------|
| 1.  | BernoulliNB            | 0,61          |
| 2.  | Decision Tree          | 0,63          |
| 3.  | Extra Tree             | 0,67          |
| 4.  | KNN                    | 0,62          |
| 5.  | Linear SVC             | 0,68          |
| 6.  | Logistic Regression CV | 0,76          |
| 7.  | MLP                    | 0,75          |
| 8.  | Random Forest          | 0,68          |
| 9.  | Ridge                  | 0,73          |
| 10. | Ridge CV               | 0,73          |
| 11. | SVC                    | 0,58          |
| 12. | GBC                    | 0,74          |
| 13. | Linear SVC 2           | 0,75          |
| 14. | Logistic Regression    | 0,64          |
| 15. | SGDC                   | 0,72          |
| 16. | Perceptron             | 0.65          |
| 17. | PAC                    | 0.79          |


### Conclusion

This paper solves the problem of building an intelligent system for analyzing the tone of customer reviews of online stores in Ukrainian. The following results were obtained within the work:

The analysis of modern literary sources and existing solutions is carried out. Among the domestic studies, those related to natural language processing, text vectorization, analysis of the tonality of Ukrainian and English texts have been studied. The basic concepts, approaches and complexities of sentiment analysis are described.

A database of reviews on online shopping services in Ukrainian has been collected. As a result, 1113 (36.7%) positive and 1923 (63.3%) negative responses were received. A statistical study of the most commonly used words in different categories of reviews. Recommendations for collecting text data from other sites and platforms are described.

Text data were prepared based on several approaches, resulting in four sets of vectors transformed by lemmatization, stemming, and bigram use. Each step of language processing was described.
68 models based on 17 machine learning algorithms and four word processing approaches were developed and evaluated. The comparative characteristics of the received estimations are carried out and the best approaches are chosen.

The expediency and ways of implementing the results of work in the practice of enterprises, institutions that use online stores to achieve their goals are described. Two variants of software architecture for implementation and self-maintenance of the developed intelligent system are created.

The main ways to improve existing approaches, models and concepts such as data collection, new model recommendations for testing are indicated.
