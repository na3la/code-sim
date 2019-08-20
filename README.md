# code-sim


Code-Sim measures similarity between source code files. It uses greedy string
tiling to generate a count of matching tokens or values. 

* First:
    * takes input for a folder containing source code files
    * reads the files and generates tokenized/non-tokenized versions
* Second:
    * generate combinations with replacement of uuids taken from file names
    * iterates through combinations and feeds file data to gst algorithim
* Finally:
    * applies distance metrics to gst result
    * inserts resulting distance metric value into pandas DataFrame
    * writes DataFrame to CSV file
