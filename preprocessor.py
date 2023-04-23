import pandas as pd
import zipcodes as zcode


def preprocess(data):

    df = pd.DataFrame([data])

    list_zipcode = df.ZIPCode.unique()

    dict_zip = {}
    for zipcode in list_zipcode:
        my_city_country = zcode.matching(zipcode.astype('str'))
        if len(my_city_country) == 1:  # if  zipcode is present then get county else, assign zipcode to county
            country = my_city_country[0].get('county')
        else:
            country = zipcode

        dict_zip.update({zipcode: country})

    dict_zip.update({92717: 'Orange County'})
    dict_zip.update({92634: 'Orange County'})

    df['County'] = df['ZIPCode'].map(dict_zip)

    category_col = ['SecuritiesAccount_1', 'Family', 'CDAccount_1', 'Online_1', 'CreditCard_1', 'ZIPCode',
                    'Education', 'County']
    df[category_col] = df[category_col].astype('category')

    counties = {
        'Los Angeles County': 'Los Angeles Region',
        'San Diego County': 'Southern',
        'Santa Clara County': 'Bay Area',
        'Alameda County': 'Bay Area',
        'Orange County': 'Southern',
        'San Francisco County': 'Bay Area',
        'San Mateo County': 'Bay Area',
        'Sacramento County': 'Central',
        'Santa Barbara County': 'Southern',
        'Yolo County': 'Central',
        'Monterey County': 'Bay Area',
        'Ventura County': 'Southern',
        'San Bernardino County': 'Southern',
        'Contra Costa County': 'Bay Area',
        'Santa Cruz County': 'Bay Area',
        'Riverside County': 'Southern',
        'Kern County': 'Southern',
        'Marin County': 'Bay Area',
        'San Luis Obispo County': 'Southern',
        'Solano County': 'Bay Area',
        'Humboldt County': 'Superior',
        'Sonoma County': 'Bay Area',
        'Fresno County': 'Central',
        'Placer County': 'Central',
        'Butte County': 'Superior',
        'Shasta County': 'Superior',
        'El Dorado County': 'Central',
        'Stanislaus County': 'Central',
        'San Benito County': 'Bay Area',
        'San Joaquin County': 'Central',
        'Mendocino County': 'Superior',
        'Tuolumne County': 'Central',
        'Siskiyou County': 'Superior',
        'Trinity County': 'Superior',
        'Merced County': 'Central',
        'Lake County': 'Superior',
        'Napa County': 'Bay Area',
        'Imperial County': 'Southern',
        93077: 'Southern',
        96651: 'Bay Area'
    }

    df['Regions'] = df['County'].map(counties)

    df.drop(columns=["ZIPCode", "County"],
                     inplace=True)

    df['Family_2'] = df['Family'].apply(lambda x: '1' if x == '2' else '0')
    df['Family_3'] = df['Family'].apply(lambda x: '1' if x == '3' else '0')
    df['Family_4'] = df['Family'].apply(lambda x: '1' if x == '4' else '0')

    df['Education_1'] = df['Education'].apply(lambda x: '1' if x == '1' else '0')
    df['Education_2'] = df['Education'].apply(lambda x: '1' if x == '2' else '0')
    df['Education_3'] = df['Education'].apply(lambda x: '1' if x == '3' else '0')

    df['Regions_Los Angeles Region'] = df['Regions'].apply(lambda x: '1' if x == 'Los Angeles Region' else '0')
    # df['Regions_Bay Area'] = df['Regions'].apply(lambda x: '1' if x == 'Bay Area' else '0')
    df['Regions_Southern'] = df['Regions'].apply(lambda x: '1' if x == 'Southern' else '0')
    df['Regions_Superior'] = df['Regions'].apply(lambda x: '1' if x == 'Superior' else '0')
    df['Regions_Central'] = df['Regions'].apply(lambda x: '1' if x == 'Central' else '0')

    df = df.drop(['Family','Education'],axis=1)

    df = df[['Age', 'Income', 'CCAvg', 'Mortgage', 'Family_2', 'Family_3', 'Family_4', 'Education_2', 'Education_3',
     'SecuritiesAccount_1', 'CDAccount_1', 'Online_1', 'CreditCard_1', 'Regions_Central', 'Regions_Los Angeles Region',
     'Regions_Southern', 'Regions_Superior']]


    #
    # any = pd.DataFrame({'Family': ['2','3','4'], 'Regions': ['b', 'a', 'c']})
    #

    # X_dt = pd.get_dummies(any, prefix=['Family', 'Regions'])

    # oneHotCols = X_dt.select_dtypes(exclude='number').columns.to_list()
    # X_dt = pd.get_dummies(X_dt, columns=oneHotCols, drop_first=True)
    # any_ex = pd.get_dummies(df1, prefix='Education')
    # frames = [df1, any_ex]
    #
    # result = pd.concat(frames, axis=1, join='inner')
    #
    # result = result.loc[:, ~result.columns.duplicated()]


    return df
