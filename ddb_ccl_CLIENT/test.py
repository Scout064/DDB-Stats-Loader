import json
input_data = {'ddb_char_array': {'Name': 'Irlibras Stargazer', 'currentHP': '24', 'maxHP': '24'}}
##,{'ddb_char_array': {'Name': 'Valeria Moonfallow', 'currentHP': '19', 'maxHP': '30'}}
request_data = [input_data]
globals()["Player1"] = {}
globals()["Player2"] = {}
globals()["Player3"] = {}
globals()["Player4"] = {}
globals()["Player5"] = {}
globals()["Player6"] = {}
globals()["Player7"] = {}
globals()["Player8"] = {}
## next data digestion
for item in request_data:
    new_dict={}
    new_dict['Name']=item.get('ddb_char_array').get('Name')
    new_dict['currentHP']=item.get('ddb_char_array').get('currentHP')
    new_dict['maxHP']=item.get('ddb_char_array').get('maxHP')
    globals()["player_dict"] = [new_dict]
## create unique global var for each name
    PlayerID = new_dict['Name'].replace(" ", "_")
    globals()[f"{PlayerID}"] = new_dict['Name']
## take player ID and extract data
##    print(globals()[f"{PlayerID}"])
    for item in player_dict:
        globals()[f"{PlayerID}_dict"] = {}
        globals()[f"{PlayerID}_dict"]['currentHP']=item.get('currentHP')
        globals()[f"{PlayerID}_dict"]['maxHP']=item.get('maxHP') 
        print(globals()[f"{PlayerID}_dict"])
    print(globals())
    

    ## create unique ID for each name
    ##playerID = hashlib.md5()
    ##playerID.update(merged_dict['Name'].encode('utf-8'))
    ##PlayerID_str = str(int(playerID.hexdigest(), 16))[0:12]
    ##print(PlayerID_str)
    