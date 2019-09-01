from __future__ import print_function

import argparse
import multiprocessing
import sqlite3
import sys
import time

import requests
from apiclient import discovery
from bs4 import BeautifulSoup
from httplib2 import Http
from oauth2client import client, file, tools
from PyQt5 import QtCore, QtGui, QtWidgets

from package.gui import Ui_Trade_Info

conn = sqlite3.connect('rates.db')
c = conn.cursor()


# -----Downloading list of leagues

names = []
leagues = []

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
page = requests.get('http://currency.poe.trade/', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
league = soup.find("select").get_text("chosen-results")
name = league.replace("chosen-results", '')


names.append(name.split("\n"))
for i in names:
    for l in i:
        leagues.append(l)

leagues.pop(-1)
leagues.pop(0)


class MainWindow(QtWidgets.QMainWindow, Ui_Trade_Info):
    # gui
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.action)
        self.comboBox.addItems(leagues)

    def action(self):
        cos = str(self.comboBox.currentText())
        worker(cos)


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    m = multiprocessing.Process(target=window.show())
    m.start()
    return app.exec_()

    

class exec():
    global c ,conn
    
    def clearing(self):
        # crates database if it exists delets contents
        Table = False

        if Table == False:
            try:
                c.execute('''CREATE TABLE rates (name text, 
                Chaos_to_buy_one real, 
                Orbs_for_one_chaos real, 
                Orbs_to_buy_one_chaos, 
                Chaos_for_one_orb real,
                id)''')
                print("Creating Database")
            except:
                Table = True
                print("Database Exists")

        if Table == True:
            sql = 'DELETE FROM rates'
            c.execute(sql)
            conn.commit()

    def scrapper(self, num, chosen):
        # scrapper + inserting data to database
        global headers
        
        CURRENCY_TEXTS = ["", "alteration", "fusing", "alchemy", "chaos", "gcp", "exalted", "chrome", "jewellers", "chance", "chisel", "scouring", "blessed", "regret", "regal", "divine",
                        "vaal", "wisdom", "portal", "armourers", "whetstone", "bauble", "transmutation", "augmentation", "mirror", "eternal", "coin", "dusk", "midnight", "dawn", "noon", "grief", "rage",
                        "hope", "ignorance", "silver", "ebers", "yriels", "inyas", "volkuurs", "offering", "hydra", "phoenix", "minotaur", "chimera", "apprentice sextant", "journeyman sextant",
                        "master sextant", "sacrifice set", "mortal set", "pale court set", "shaper set", "splinter of xoph", "splinter of tul", "splinter of esh", "splinter of uulnetol", "splinter of chayula",
                        "blessing of xoph", "blessing of tul", "blessing of esh", "blessing of uulnetol", "blessing of chayula", "xophs breachstone", "tuls breachstone", "eshs breachstone", "uulnetols breachstone", "chayulas breachstone"]

        page1 = requests.get(
            'http://currency.poe.trade/search?league={}&online=x&stock=&want={}&have=4'.format(chosen, num), headers=headers)
        page2 = requests.get(
            'http://currency.poe.trade/search?league={}&online=x&stock=&want=4&have={}'.format(chosen, num), headers=headers)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        rate1 = soup1.find("small")
        rate2 = rate1.find_next("small")
        rate3 = soup2.find("small")
        rate4 = rate3.find_next("small")

        text1 = rate1.get_text()
        text2 = rate2.get_text()
        text3 = rate3.get_text()
        text4 = rate4.get_text()

        name = CURRENCY_TEXTS[num]
        info1 = text1[1:].strip(" ← ⨯ ")
        info2 = text2[1:].strip(" → ⨯ ")
        info3 = text3[1:].strip(" ← ⨯ ")
        info4 = text4[1:].strip(" → ⨯ ")

        # If market is empty
        if len(info1) > 7:
            info1 = "None"
            info2 = "None"
        if len(info3) > 7:
            info3 = "None"
            info4 = "None"

        c.execute("INSERT INTO rates ('name','Chaos_to_buy_one', 'Orbs_for_one_chaos', 'Orbs_to_buy_one_chaos', 'Chaos_for_one_orb', 'id') VALUES (?, ?, ?, ?, ?, ?)",
                  ((name), (info1), (info2), (info3), (info4), (num)))
        conn.commit()

        

    # Google_api

    def sheet_update(self):
        # Cominication
        SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flags = argparse.ArgumentParser(
                parents=[tools.argparser]).parse_args()
            flow = client.flow_from_clientsecrets(
                'F:\\zGit\\poe\\client_id.json', SCOPES)
            creds = tools.run_flow(flow, store, flags)

        SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

        # cords
        FIELDS = ('Name', 'Chaos to buy one', 'orbs for one Chaos',
                  'orbs to buy one Chaos', 'Chaos for one orb', 'id')
        cxn = sqlite3.connect('rates.db')
        cur = cxn.cursor()
        rows = cur.execute('SELECT * FROM rates').fetchall()
        cxn.close()
        rows.insert(0, FIELDS)
        data = {'values': [row[:6] for row in rows]}

        # Update
        SHEETS.spreadsheets().values().update(spreadsheetId="14ayFS7HYQMTLYdenXpTizI4p-iIbr7CaxNeC6S0q6jU",
                                              range='A1', body=data, valueInputOption='RAW').execute()
        print('Wrote data to Sheet:')
        rows = SHEETS.spreadsheets().values().get(spreadsheetId="14ayFS7HYQMTLYdenXpTizI4p-iIbr7CaxNeC6S0q6jU",
                                                  range='Sheet1').execute().get('values', [])
        #for row in rows:
            #print(row)


def worker(chosen):
    # multiprocesing
    print(chosen)
    cl = multiprocessing.Process(target=exec().clearing)
    cl.start()
    cl.join()
    for i in range(1, 67):
        s = multiprocessing.Process(target=exec().scrapper, args=(i, chosen))
        s.start()
    s.join()
    exec().sheet_update()


if __name__ == "__main__":
    run()
