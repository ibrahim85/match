from os import path, listdir, curdir

from nltk.corpus.reader.bracket_parse import BracketParseCorpusReader

sentences_path = path.join(path.abspath(curdir), 'Corpus/OneStopEnglishCorpus/Sentence-Aligned')
parsed_path = "/home/ms10596/PycharmProjects/match/utils/Corpus/OneStopEnglishCorpus/Processed-AllLevels-AllFiles/Parsed"
file_names = sorted(listdir(parsed_path))[1:]


def load_advanced_elementary():
    f = open(path.join(sentences_path, 'ADV-ELE.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    advanced = [i[0] for i in all if len(i) == 2]
    elementary = [i[1] for i in all if len(i) == 2]
    return advanced, elementary


def load_advanced_intermediate():
    f = open(path.join(sentences_path, 'ADV-INT.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    advanced = [i[0] for i in all if len(i) == 2]
    intermediate = [i[1] for i in all if len(i) == 2]
    return advanced, intermediate


def load_intermediate_elementary():
    f = open(path.join(sentences_path, 'ELE-INT.txt'))
    all = [i.strip().split('\n') for i in f.read().split("*******")]
    elementary = [i[0] for i in all if len(i) == 2]
    intermediate = [i[1] for i in all if len(i) == 2]
    return intermediate, elementary


def load_corpus():
    corpus = BracketParseCorpusReader(root=parsed_path, fileids=file_names[1:])
    return corpus


def corpus_to_words(corpus):
    labels_names = ['ele', 'int', 'adv']
    articles = []
    tags = []
    for i in file_names:
        articles.append(list(corpus.words(i)))
        tags.append(labels_names.index(i[-14:-11]))
    return articles, tags


def corpus_to_pos(corpus):
    labels_names = ['ele', 'int', 'adv']
    articles = []
    tags = []
    for i in file_names:
        articles.append([j[1] for j in corpus.tagged_words(i)])
        tags.append(labels_names.index(i[-14:-11]))
    return articles, tags


def detokenize(l):
    from nltk.tokenize.treebank import TreebankWordDetokenizer
    return TreebankWordDetokenizer().detokenize(l)


def opennmt_preprocessing():
    a, b = load_advanced_elementary()
    advanced_sents = open('advanced_sents.txt', mode='w')
    elementary_sents = open('elementary_sents.txt', mode='w')
    for i in range(len(a)):
        advanced_sents.write(a[i]+'\n')
        elementary_sents.write(b[i]+'\n')
    advanced_sents.close()
    elementary_sents.close()


if __name__ == '__main__':
    opennmt_preprocessing()
