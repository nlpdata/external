Retrieved sentences for each (question, answer option) pair in three multiple-choice science question answering datasets (i.e., ARC-Easy, ARC-Challenge, and OpenBookQA) from integrated reference corpus + integrated external corpus (i.e., IRC & IEC described in [Improving Question Answering with External Knowledge](https://arxiv.org/abs/1902.00993v2)).


This is a re-implementation. As of the release date of this repository, the Allen Institute for Artificial Intelligence (AI2) disallows third parties to redistribute the ARC Corpus. Therefore, we cannot directly release a resource containing the retrieved sentences from the ARC Corpus. Instead, for all such sentences, we provide pointers to the ARC Corpus as well as a script for fetching the retrieved sentences based on the pointers and your local copy of the corpus. 


If you find this resource useful, please cite the following paper.
```
@inproceedings{pan2019improving,
  title={Improving Question Answering with External Knowledge},
  author={Pan, Xiaoman and Sun, Kai and Yu, Dian and Chen, Jianshu and 
          Ji, Heng and Cardie, Claire and Yu, Dong},
  booktitle={Proceedings of the Workshop on Machine Reading for Question Answering},
  address={Hong Kong, China},
  url={https://arxiv.org/abs/1902.00993v2},
  year={2019}
}
```

Below are the detailed instructions.

1. Clone this repository.
2. Download ```ARC-V1-Feb2018.zip``` from AI2, unzip it, and copy ```ARC_Corpus.txt``` (in the unzipped folder ```ARC-V1-Feb2018-2```) to ```data``` folder. The CRC of ```ARC_Corpus.txt``` should be ```8CFE08C6```.
3. Run ```python3 gen.py``` to generate ```arc_challenge.json```, ```arc_easy.json```, and ```openbookqa.json```. The format of these files are as follows.
```
{
 FileName-QuestionID: [
  retrieved sentences for the 1st option,
  retrieved sentences for the 2nd option,
  ...
 ], 
 ...
}
```
File names and question IDs follow ```ARC-V1-Feb2018.zip``` and ```OpenBookQA-V1-Sep2018.zip```. Retrieved sentences are splitted by "\n".
