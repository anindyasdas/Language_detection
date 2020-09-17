# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle 
from collections import defaultdict
import os


#########################################
fasttext_dict = {'Hindi':'cc.hi.300.vec',
                 'Marathi':'cc.mr.300.vec',
                 'Nepali':'cc.ne.300.vec',
                 'Arabic':'cc.ar.300.vec',
                 'Persian':'cc.fa.300.vec',
                 'Urdu':'cc.ur.300.vec',
                 'Ukranian':'cc.uk.300.vec',
                 'Russian':'cc.ru.300.vec',
                 'Bulgarian':'cc.bg.300.vec',
                 'Macedonian':'cc.mk.300.vec',
                 'English':'cc.en.300.vec',
                 'French':'cc.fr.300.vec',
                 'German':'cc.de.300.vec',
                 'Spanish':'cc.es.300.vec',
                 'Vietnamese':'cc.vi.300.vec',
                 'Catalan':'cc.ca.300.vec',
                 'Welsh':'cc.cy.300.vec',
                 'Czech':'cc.cs.300.vec',
                 'Danish':'cc.da.300.vec',
                 'Estonian':'cc.et.300.vec',
                 'Croatian':'cc.hr.300.vec',
                 'Finnish':'cc.fi.300.vec',
                 'Hungarian':'cc.hu.300.vec',
                 'Indonesian':'cc.id.300.vec',
                 'Italian':'cc.it.300.vec',
                 'Lithuanian':'cc.lt.300.vec',
                 'Latvian':'cc.lv.300.vec',
                 'Norweignian':'cc.no.300.vec',
                 'Netherlandish':'cc.nl.300.vec',
                 'Portuguese':'cc.pt.300.vec',
                 'Polish':'cc.pl.300.vec',
                 'Somali':'cc.so.300.vec',
                 'Slovenian':'cc.sl.300.vec',
                 'Slovak':'cc.sk.300.vec',
                 'Romanian':'cc.ro.300.vec',
                 'Albanian':'cc.sq.300.vec',
                 'Swedish':'cc.sv.300.vec',
                 'Swahili':'cc.sw.300.vec',
                 'Turkish':'cc.tr.300.vec',
                 'Tagalog':'cc.tl.300.vec',
                 'Afrikaans':'cc.af.300.vec'
                 }
#################################################
Devanagari_group =['Hindi', 'Marathi', 'Nepali']
Arabic_group=['Arabic', 'Persian', 'Urdu']
Cyrillic_group=['Ukranian', 'Russian', 'Bulgarian', 'Macedonian']
Latin_group=['English', 'French', 'German', 'Spanish', 'Vietnamese', 'Catalan',
             'Welsh', 'Czech', 'Danish', 'Estonian', 'Croatian', 'Finnish', 
             'Hungarian', 'Indonesian', 'Italian', 'Lithuanian', 'Latvian',
             'Norweignian', 'Netherlandish','Portuguese', 'Polish', 'Somali',
             'Slovenian', 'Slovak', 'Romanian','Albanian', 'Swedish', 'Swahili',
             'Turkish', 'Tagalog', 'Afrikaans']

##############################################
fasttext_directory='./fasttext_languages/'
language_dict_directory ='./language_dict_directory/'
##########################################
Positional_wt=9
count_words = 70000
################################################

def create_language_group_vocab(file_name, language, lang_dict):
    
    count=0
    for line in file_name:
        if count > count_words:
            break
        if count>0:
            word = line.split()[0]
            lang_dict[language][word]=1*(1+Positional_wt*(count_words-count)/count_words)
            #lang_dict[language][word]=1
        count+=1
    return lang_dict
    
    
#language_dict = nested_dict(2,int)




def train_language_vocabularies(language_group):
    language_dict= defaultdict(dict) #two dimensional dict
    for language in eval(language_group):
        f_name= os.path.join(fasttext_directory, fasttext_dict[language])
        file_name=open(f_name, 'r', encoding='utf8')
        language_dict = create_language_group_vocab(file_name, language, language_dict)
        file_name.close()
    pkl =os.path.join(language_dict_directory, 'language_dict_%s.pkl'%language_group)
    file_save = open(pkl, 'wb') 
    pickle.dump(language_dict, file_save)
    file_save.close()
    


###########################Devanagari######################################
language_group='Devanagari_group'
train_language_vocabularies(language_group)
pkl =os.path.join(language_dict_directory, 'language_dict_%s.pkl'%language_group)
file_name = open(pkl, 'rb')
language_dict1= pickle.load(file_name)
############################Arabic###################################
language_group='Arabic_group'
train_language_vocabularies(language_group)
pkl =os.path.join(language_dict_directory, 'language_dict_%s.pkl'%language_group)
file_name = open(pkl, 'rb')
language_dict2= pickle.load(file_name)
##########################################################################   
############################Cyrillic###################################
language_group='Cyrillic_group'
train_language_vocabularies(language_group)
pkl =os.path.join(language_dict_directory, 'language_dict_%s.pkl'%language_group)
file_name = open(pkl, 'rb')
language_dict3= pickle.load(file_name)
########################################################################## 
############################Latin###################################
language_group='Latin_group'
train_language_vocabularies(language_group)
pkl =os.path.join(language_dict_directory, 'language_dict_%s.pkl'%language_group)
file_name = open(pkl, 'rb')
language_dict4= pickle.load(file_name)
##########################################################################       