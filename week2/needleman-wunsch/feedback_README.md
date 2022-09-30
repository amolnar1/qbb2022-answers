Awesome work! This all looks really good, and you nailed needleman-wunsch. A few very minor issues: first, we asked you to read in an output file name for the alignments as one of the scripts inputs. The script should then handle writing the alignments themselves to this output file. If you resubmit, don't forget to include the two alignment files (no points deducted).

Also, I see what you're going for with the `trace` array in regards to counting the number of gaps, but I think your code is accidently counting the value in the top left cell of the traceback matrix, which it shouldn't. Also you reported the same statistics for both DNA and AA, which I don't think is right. You also need to report the overall score of each alignment (-0.5)

9.5/10
