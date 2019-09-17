# text-summary-demo

### Description 

Demo project to show a text summary generator in python. The input dataset used is a collection of 8 short sports articles referenced from [here](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/)


### Requirements

The project is written using python 3 and requires the following libraries:
- NLTK (Natural Language Toolkit). Install instructions [here](https://www.nltk.org/install.html)
- numpy
- pandas

### Running the project

To run the project, use 

```
python text_summary.py [filename] [summary_ratio]
```
*article_id*: which article to use from the dataset.
*summary_ratio*: percentage of desired summarisation.

The output of the program consists of a summary of the original input text in *filename* at a rate determined by *summary_rate*. A *summary_rate* of 50% would produce a text that is half as long as the original one.
```
Input text length: [length of text in filename]
Summary length: [length of summary]
Summary: [generated summary]
```

Example: *python text_summary.py 0 15*
```
Input text length: 294
Sumary length: 17.687074829931973
Summary: 
["I think just because you're in the same sport doesn't mean that you have to be friends with everyone just because you're categorized, you're a tennis player, so you're going to get along with tennis players.", "I think everyone just thinks because we're tennis players we should be the greatest of friends."]

```

### Limitations



