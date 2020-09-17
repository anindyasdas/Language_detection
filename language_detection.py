# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Re unicode https://www.regular-expressions.info/unicode.html
import regex as re #like re module but additional functionality
import pickle
import os
import argparse
from sklearn.metrics import classification_report, accuracy_score
import time
#######groups#############################################
Latin= re.compile(r'([\p{IsLatin}]+)', re.UNICODE)
Arabic= re.compile(r'([\p{IsArabic}]+)', re.UNICODE)
Bengali= re.compile(r'([\p{IsBengali}]+)', re.UNICODE)
Cyrillic= re.compile(r'([\p{IsCyrillic}]+)', re.UNICODE)
Devanagari= re.compile(r'([\p{IsDevanagari}]+)', re.UNICODE)
Greek= re.compile(r'([\p{IsGreek}]+)', re.UNICODE)
Gujarati= re.compile(r'([\p{IsGujarati}]+)', re.UNICODE)
Punjabi= re.compile(r'([\p{IsGurmukhi}]+)', re.UNICODE)
Hebrew= re.compile(r'([\p{IsHebrew}]+)', re.UNICODE)
Kannada= re.compile(r'([\p{IsKannada}]+)', re.UNICODE)
Malayalam=re.compile(r'([\p{IsMalayalam}]+)', re.UNICODE)
#Tagalog=re.compile(r'([\p{IsTagalog}]+)', re.UNICODE)
Tamil=re.compile(r'([\p{IsTamil}]+)', re.UNICODE)
Telugu=re.compile(r'([\p{IsTelugu}]+)', re.UNICODE)
Thai=re.compile(r'([\p{IsThai}]+)', re.UNICODE)
Chinese = re.compile(r'([\p{IsHan}]+)', re.UNICODE) #Han only
Japanese = re.compile(r'([\p{IsHan}\p{IsHira}\p{IsKatakana}]+)', re.UNICODE) #Han Hiragato and Katakana
Korean = re.compile(r'([\p{IsHan}\p{IsHangul}]+)', re.UNICODE) #Hangul and Han
##############################################################
All= re.compile(r'([^\p{IsHan}\p{IsHangul}\p{IsHira}\p{IsKatakana}\p{IsThai} \
\p{IsTelugu}\p{IsTamil}\p{IsMalayalam}\p{IsKannada}\p{IsHebrew} \
\p{IsGurmukhi}\p{IsGujarati}\p{IsGreek}\p{IsDevanagari} \
\p{IsCyrillic}\p{IsBengali}\p{IsArabic}\p{IsLatin}]+)', re.UNICODE)
###################################################################
#Data Preprocess#

re1=r'(?<=[.,:;!])(?=[^\s])'
re2='(?=[.,:;!])(?<=[^\s])'
re3=r'[\(\)\{\}\[\]\d+]'
punct= re.compile('(%s|%s)'%(re1,re2)) 
brac_dig= re.compile('%s'%re3) 
####################################################################

groups=['Latin', 'Arabic', 'Bengali', 'Cyrillic', 'Devanagari', 'Greek', 'Gujarati', 
        'Punjabi', 'Hebrew', 'Kannada', 'Malayalam', 'Tamil', 'Telugu',
        'Thai', 'Chinese', 'Japanese', 'Korean']


##################################################
dict_language_group_dictionary={}
other_language_group=['Devanagari', 'Arabic', 'Cyrillic', 'Latin']

Devanagari_group =['Hindi', 'Marathi', 'Nepali']
Arabic_group=['Arabic', 'Persian', 'Urdu']
Cyrillic_group=['Ukranian', 'Russian', 'Bulgarian', 'Macedonian']
Latin_group=['English', 'French', 'German', 'Spanish', 'Vietnamese', 'Catalan',
             'Welsh', 'Czech', 'Danish', 'Estonian', 'Croatian', 'Finnish', 
             'Hungarian', 'Indonesian', 'Italian', 'Lithuanian', 'Latvian',
             'Norweignian', 'Netherlandish','Portuguese', 'Polish', 'Somali',
             'Slovenian', 'Slovak', 'Romanian','Albanian', 'Swedish', 'Swahili',
             'Turkish', 'Tagalog', 'Afrikaans']
########################################################

language_dict_directory ='./language_dict_directory/'
Positional_wt=9 #used during training strength of the position of a word
#######################################################################

for language_group in other_language_group:
    pkl =os.path.join(language_dict_directory, 'language_dict_%s_group.pkl'%language_group)
    file_name = open(pkl, 'rb')
    dict_language_group_dictionary[language_group]= pickle.load(file_name)
########################################################################
def detect_language(selected_group, doc):
    prob_groups_1=dict()
    language_group_dictionary = dict_language_group_dictionary[selected_group]
    tokens= doc.split()
    #print(tokens)
    total_num_tokens= len(tokens)
    for language in eval(selected_group+'_group'):
        num_matched_tokens =0
        for token in tokens:
            try:
                num_matched_tokens += language_group_dictionary[language][token]
            except:
                num_matched_tokens +=0.0
        prob_groups_1[language]= num_matched_tokens/((Positional_wt+1)*total_num_tokens)
    #print(prob_groups_1)
    selected_language = max(prob_groups_1, key= lambda x: prob_groups_1[x])
    return(selected_language)


def count_charecters(d, pat):
    ch=[]
    #print(d)
    if (pat==Japanese) or (pat== Chinese) or (pat == Korean):
        mul=2
    else:
        mul=1
    for item in pat.findall(d):
        ch+=list(item)
    return len(ch)*mul

def assign_group(doc):
    #Incase of Language is Chinese , chinese japanese korean all gives max, Chinese is selected
    prob_groups=dict()
    #doc='Universität          ist schlecht'
    #doc='大學不好'
    doc_p= punct.sub(' ', doc) #Use this regex to match locations where preceding character is a dot or a comma and the next character isn't a space:
#line= re.sub(r'(?=[.,:;])(?<=[^\s])', r' ', line) # after
    doc_p= brac_dig.sub('', doc_p)#remove brackets and numbers
    #doc_wo_spaces=doc.replace(' ', '')
    doc_wo_spaces=doc_p.replace(' ', '')
    doc_wo_spaces=All.sub('', doc_wo_spaces)
    if len(doc_wo_spaces)==0: # If only special charecter on numbers return 0
        return len(doc_wo_spaces)
    num_ch=len(doc_wo_spaces)*2
    for group in groups:
        lan_ch= count_charecters(doc_wo_spaces, eval(group)) #eval() evaluates string like python expression
        prob_groups[group]= lan_ch/num_ch
    #print(prob_groups)
    selected_group = max(prob_groups, key= lambda x: prob_groups[x])
    if selected_group not in ['Latin', 'Devanagari', 'Cyrillic', 'Arabic']:
        language= selected_group
        #print('The Detected Language is:', language)
    elif selected_group== 'Devanagari':
        language = detect_language(selected_group, doc_p)
        #print('The Detected Language is:', language)
    elif selected_group== 'Arabic':
        language = detect_language(selected_group, doc_p)
        #print('The Detected Language is:', language)
    elif selected_group== 'Cyrillic':
        language = detect_language(selected_group, doc_p)
        #print('The Detected Language is:', language)
    elif selected_group== 'Latin':
        language = detect_language(selected_group, doc_p)
        #print('The Detected Language is:', language)
        #print('process language')
    return(language)
    
    



#pattern = re.compile(r'([\p{IsHan}\p{IsBopo}\p{IsHira}\p{IsKatakana}]+)', re.UNICODE) #Chinese Japanese Korean Charecters
#pattern2 = re.compile(r'([^\p{IsHan}\p{IsBopo}\p{IsHira}\p{IsKatakana}]+)', re.UNICODE) # all charecters except korean or japanese or chinese


#documents=[]


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-l', '--labels', help='Labels file name, if available')
args = parser.parse_args()
input_file = args.input
labels_file = args.labels

inp =open(input_file,'r', encoding='utf8')
otp= open('detection_results.txt','w', encoding='utf8')
print('-----------process starts---------')
start_time= time.time()
actual=[]
predicted=[]
lbl1=[]
if labels_file is not None:
    lbl =open(labels_file,'r', encoding='utf8')
    lbl1=lbl.readlines()
    lbl.close()


inp1=inp.readlines()
ip=[]
for idx1 in range(len(inp1)):
    line=inp1[idx1]
    pred= assign_group(line.strip())
    if pred !=0:
        ip.append(line.strip())
        predicted.append(pred.strip())
        print(line.strip(), '\t', pred.strip(), file=otp)
        if len(inp1)==len(lbl1):
            line2=lbl1[idx1]
            actual.append(line2.strip())
inp.close()
otp.close()
print('**********output is saved at : detection_results.txt*************' )

if(len(actual)==len(predicted)):
    print('******Accuracy and Classification report is saved at reports.txt*******')
    rpt= open('reports.txt','w')
    print('Accuracy Score:', accuracy_score(actual, predicted)*100, file=rpt)
    print(classification_report(actual, predicted),file=rpt)
    rpt.close()
    
print('################################################################')
end_time= time.time()
print('-------------process ends---------', end_time-start_time, 'seconds')

