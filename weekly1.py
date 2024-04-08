# # Downloads Qantas share price beginning 1 January 2020
# import yfinance                                           # (1)
# tic = "QAN.AX"                                            # (2)
# start = '2020-01-01'                                      # (3)
# end = None                                                # (4)
# df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
# print(df)                                                 # (6)
# df.to_csv('qan_stk_prc.csv')                              # (7)

# a = "Hi"
# if a:
#     a("There")

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for location in l:
#     if not location.startswith("Forest"):
#         print(location)

# f_suburbs = dict()
# f_suburbs["Fairfield"] = 18081
# f_suburbs["Fairfield East"] = 5273
# f_suburbs["Fairfield Heights"] = 7517
# f_suburbs["Fairfield West"] = 11575
# f_suburbs["Fairlight"] = 5840
# f_suburbs["Fiddletown"] = 233
# f_suburbs["Five Dock"] = 9356
# f_suburbs["Flemington"] = None
# f_suburbs["Forest Glen"] = None
# f_suburbs["Forest Lodge"] = 4583
# f_suburbs["Forestville"] = 8329
# f_suburbs["Freemans Reach"] = 1973
# f_suburbs["Frenchs Forest"] = 13473
# f_suburbs["Freshwater"] = 8866
#
# for SUBURB_NAME, POPULATION in f_suburbs.items():
#     if not SUBURB_NAME.startswith("Forest") and POPULATION is not None:
#         print(f"{SUBURB_NAME}: {POPULATION}")

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
# list_length = len(l)
#
# for i in range(list_length):
#     print(f"{i}: {l[i]}")

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for last_name in last_names:
    for first_name in first_names:
        for middle_name in middle_names:
            # 如果middle_name是None，则不打印中间名
            if middle_name is None:
                print(f"{first_name} {last_name}")
            else:
                print(f"{first_name} {middle_name} {last_name}")

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for first_name in first_names:
    for last_name in last_names:
        for middle_name in middle_names:
            if middle_name is None:
                print(f"{first_name}{last_name}")
            else:
                print(f"{first_name}{middle_name}{last_name}")