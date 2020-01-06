# code-sim


Code-Sim measures similarity between source code files. It uses greedy string
tiling to generate a count of matching tokens or values.
Tiling is implemented according to pseudocode of Karp-Rabin greedy string tiling algorithm, with as few changes as possible.

* First:
    * takes input for a folder containing source code files
    * reads the files and generates tokenized/non-tokenized versions
* Second:
    * generate combinations with replacement of uuids taken from file names
    * iterates through combinations and feeds file data to gst algorithm
* Finally:
    * applies distance metrics to gst result
    * inserts resulting distance metric value into pandas DataFrame
    * writes DataFrame to CSV file



tc/ -> contains tokenization defs for C code.
gst/ -> contains greedy string tiling defs.
lib/ -> contains general utility files, currently only the distance metrics
backups/ -> unused/unmaintained old code, for reference only. 

TODO: improve efficiency of tiling alg; Look at parallelizing, DP, vectorizing
operations.
