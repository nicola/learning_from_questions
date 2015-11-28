# Fix path issues for importing parent path
import sys
sys.path.append('../')

from ir import BagOfWords
from feature_computation.Sentence import ReadSentencesFromTextFileSimple

if __name__ == '__main__':
    # Load sentences using Branavan's code
    sSentenceFile = '../../data/minecraft_text.raw'
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)

    # Run BagOfWords passing the sentences and the ids
    sentences = [sentence.lWords for sentence in lSentences]
    ids = [sentence.iIndex for sentence in lSentences]
    bags = BagOfWords(sentences, ids)

    # Random tests
    print bags.question("object", "bed")[0]