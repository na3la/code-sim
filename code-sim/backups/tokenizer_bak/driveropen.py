from file_feeder import _file_feeder
from open_lex import open_lex

for x in open_lex(
        _file_feeder(
            '/home/anon/notebooks/code-sim/tokenizer/javahw1/newfixed/')):
    print(x)
