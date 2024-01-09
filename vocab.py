import pandas as pd
import numpy as np
import random
from datetime import date, datetime
from dateutil import relativedelta
import os
import scipy.stats as stats

# Register : 

# wordFrench, wordEnglish, wordPortuguese, 
# nDaysReviewed, nDaysLastReview,
# nDaysCorrect, nDaysLastCorrect,

# Configs :

# probRessample, minAmountTransfer, maxAmountRestransfer

DEFAULT_SETTINGS = {
    'vocabFile': 'defaultWords.csv',
    'initialDate': '07/01/2024',
    'trainingType': 'Portuguese2French', # Random2French, French2Random, French2Portuguese, Portuguese2French, French2English, English2French  
    'probRessample': 0.1,
    'minAmountTransfer': 2,
    'maxAmountRestransfer': 2
}

trainingTypes = {
    'Random2French': {
        'sourceLanguage': 'Random',
        'targetLanguage': 'French'
    },
    'French2Random': {
        'sourceLanguage': 'French',
        'targetLanguage': 'Random'
    },
    'French2Portuguese': {
        'sourceLanguage': 'French',
        'targetLanguage': 'Portuguese'
    },
    'Portuguese2French': {
        'sourceLanguage': 'Portuguese',
        'targetLanguage': 'French'
    },
    'French2English': {
        'sourceLanguage': 'French',
        'targetLanguage': 'English'
    },
    'English2French': {
        'sourceLanguage': 'English',
        'targetLanguage': 'French'
    }
}

trainingTypesEnum = {
    0 : 'Random2French',
    1 : 'French2Random',
    2 : 'French2Portuguese',
    3 : 'Portuguese2French',
    4 : 'French2English',
    5 : 'English2French'
}

def get_settings(settings):
    
    settings = DEFAULT_SETTINGS

    # Ask the user if it wants to use the default settings
    use_default = input('Do you want to use the default settings? (Y/N)')
    
    print('Settings: ' + str(settings))

    if use_default == 'Y':
        return settings
    else:
        # Ask user for settings (no error handling) 

        custom_vocab = input('Do you want to use a custom vocab file? (Y/N)')
        
        if custom_vocab == 'Y':
            # Ask for vocab file
            vocab_file = input('Enter the vocab file path: ')
            settings['vocabFile'] = vocab_file

        custom_date = input('Do you want to use a custom initial date? (Y/N)')

        if custom_date == 'Y':

            # Ask for initial date
            init_date = input('Enter the initial date (dd/mm/yyyy): ')
            settings['initialDate'] = init_date

        custom_training_type = input('Do you want to use a custom training type? (Y/N)')

        if custom_training_type == 'Y':
            # Ask for training type
            print("Available training types: Random2French (0), French2Random (1), French2Portuguese (2), Portuguese2French (3), French2English (4), English2French (5)")
            training_type = input('Enter the training type: ')
            settings['trainingType'] = trainingTypesEnum[int(training_type)] 
        
        custom_prob_ressample = input('Do you want to use a custom probability of ressample? (Y/N)')

        if custom_prob_ressample == 'Y':
            # Ask for probability of ressample
            prob_ressample = input('Enter the probability of ressample: ')
            settings['probRessample'] = float(prob_ressample)
        
        custom_min_amount_transfer = input('Do you want to use a custom minimum amount of transfer? (Y/N)')

        if custom_min_amount_transfer == 'Y':
            # Ask for minimum amount of transfer
            min_amount_transfer = input('Enter the minimum amount of transfer: ')
            settings['minAmountTransfer'] = int(min_amount_transfer)
        
        custom_max_amount_retransfer = input('Do you want to use a custom maximum amount of retransfer? (Y/N)')

        if custom_max_amount_retransfer == 'Y':
            # Ask for maximum amount of retransfer
            max_amount_retransfer = input('Enter the maximum amount of retransfer: ')
            settings['maxAmountRestransfer'] = int(max_amount_retransfer)

    return settings

def update_data(data, word, answer, settings):

    # Stored date format: dd/mm/yyyy
    # settings['initialDate'] = 'dd/mm/yyyy'
    init_date = datetime.strptime(settings['initialDate'], '%d/%m/%Y')
    curr_date = date.today()

    diff = relativedelta.relativedelta(curr_date, init_date) 

    # Update nDaysReviewed

    # Update nDaysLastReview

    # Update nDaysCorrect

    # Update nDaysLastCorrect

    return data

def load_data(settings):
    
    # Read csv files :
    data = {
        'vocabFile': pd.read_csv(settings['vocabFile'], sep=','),
        'trainingStats': pd.read_csv(settings['trainingStatsFile'], sep=',')
    }

    return data

def get_word(data, settings):
    return word

def ask_word(word, settings):
    return answer

def stop(data, settings):
    return True

def save_data(data):
    return data

def main():

    # Get train settings
    settings = get_settings()

    # Load data
    data = load_data(settings)

    # Update data
    data = update_data(data, word, answer, settings)

    # Start loop
    while True:

        # Get word
        word = get_word(data, settings)

        # Ask word
        answer = ask_word(word, settings)

        # Update data
        data = update_data(data, word, answer, settings)

        # Check if stop
        if stop(data, settings):
            break
    
    # Save data
    save_data(data)
