# Language_detection


## Scope
This method can identify the following natural languages: **English, French, German, Spanish, Vietnamese,
Catalan,Welsh, Czech, Danish, Estonian, Croatian, Finnish, Hungarian, Indonesian, Italian,
Lithuanian, Latvian, Norweignian, Netherlandish, Portuguese, Polish, Somali, Slovenian, Slovak,
Romanian, Albanian, Swedish, Swahili, Turkish, Tagalog, Afrikaans, Arabic, Persian, Urdu,
Hindi, Marathi, Nepali, Ukranian, Russian, Bulgarian, Macedonian, Bengali, Greek, Gujarati,
Punjabi, Hebrew, Kannada, Malayalam, Tamil, Telugu, Thai, Chinese, Japanese, Korean**. This
approach assumes languages are written in their usual scripts with most of the words are spelled correctly
i.e. a Hindi or Arabic paragraph written in Latin script, will yield wrong prediction.
- This method can detect 54 natural languages in text documents with an accuracy of 99.38%.

- Documentation, Algorthm , Method discussed in : **Method_of_Language_Detection.pdf**
## Evaluating any Dataset on pretrained model
- Model weights are stored PICKLE format in  directory language_dict_directory

- Download the model weights from [language_dict_directory](https://drive.google.com/file/d/1ILi1QYFF0RlDD19wIOToSJjmQQnDjCXU/view?usp=sharing) and extract the zip to **language_dict_directory**
- Download [Input Data](https://drive.google.com/file/d/1vFod1VgJpOZw7H9-mHFDr4cKc5DaE1dC/view?usp=sharing)  
- Downloaded Input Data file **document_54.txt** is input file to be evaluated containing 53,921 paragraphs of total 54 languages (or you can use your own data file with the same format as **document_54.txt**)
- Download [Label file](https://drive.google.com/file/d/16OydexD_W6g8kB95HZHrlgpV1PgGOxXM/view?usp=sharing) (or you can use your own data file with the same format as **labels_54.txt**)
- Downloaded Label file **labels_54.txt** is corresponding  label file (Actual labels)

## Run Program ##
### If labels file available ###
`
python language_detection.py -i input_file.txt -l label_file.txt
`
eg.  `python language_detection.py -i document_54.txt -l labels_54.txt`
- Output file generated: detection_results.txt
- Classification report: reports.txt

### If labels file not available ###
`
python language_detection.py -i document.txt
`
- Output file generated: detection_results.txt
- No classification reports printed

## Training the model wights (To generate models weights instead of downloading folder *language_dict_directory*)

- Traing the model is basically creating the language_dict_directory. For details on hw this directory is created and algorithm used refer **Method_of_Language_Detection.pdf**

- Download fasttext wordvectors from [link](https://fasttext.cc/docs/en/crawl-vectors.html) and save into a folder named as *fasttext_languages*
run training_dictionary.py

`
python training_dictionary.py
`
- This will create the weight pickle files and store into *language_dict_directory*




