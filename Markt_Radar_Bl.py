#!/usr/bin/env python
# coding: utf-8

# ### Markt.Radar Berufe auf BL Ebene

# In[5]:


# Bibliotheken
import pandas as pd
import numpy as np


# In[6]:


# Auflistung der Markt.Radar Berufe und der zugehöriger ID´s
Markt_Radar = {
    "Elektroingenieur" : [59],
    "Bauingenieur" : [47, 113, 114, 115, 116, 117, 118, 119],
    "Recruiter" : [81],
    "HR-Partner/Personalreferent": [81],
    "Spezialisten und Berater HR / Change Management": [81],
    "Controller (Finance)" : [82],
    "Projektkaufmann / -leiter, Berater" : [80],
    "IT-Service / Betriebsführung" : [68],
    "IT-Entwicklung" : [69],
    "IT-Anwendungs- / Anforderungsmanagement, IT-Beratung" : [67],
    "IT-Strategie, -Projektmanagement, -Security" : [66],
    "Service im Zug (Quer.)" : [78, 79, 133, 172],
    "Reiseberater" : [132],
    "Call Center Agent" : [134],
    "Elektrofachkräfte" : [58, 60], 
    #"Fahrweginstandhalter" : [57, 58, 60, 62, 88, 91, 92, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 108, 109, 110, 
    #                         111, 112, 120, 121, 122, 136, 137, 138, 162, 163],
    # Defintion orientiert sich an der Zuordnung bei den Gehaltsdaten
    "Fahrweginstandhalter" : [57, 58, 60, 62, 88, 91, 92, 136, 137, 138, 162, 163],
    #"Schienfahrzeuginstandhalter" : [57, 58, 60, 85, 86, 87, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 
    #                                105, 106, 108, 109, 110, 111, 112, 162, 163, 136, 138, 162, 163], 
    # Defintion orientiert sich an der Zuordnung bei den Gehaltsdaten
    "Schienfahrzeuginstandhalter" : [57, 58, 60, 91, 92, 136, 138, 162, 163],    
    "Servicetechniker Elektrotechnik / Telekommunikation" : [107],
    "Servicetechniker Maschinen- / Fördertechnik" : [92],
    "Servicetechniker Heizung / Klima / Lüftung / Sanitär" : [124],
    "Hausinspektor / Objektbetreuer": [123],
    "Sicherungsdienst / Ordnungsdienst" : [130], 
    "Fahrwegpfleger / Landschaftspfleger" : [169, 170, 171],
    "Gebäudereiniger / Fahrzeugreiniger" : [76],
    "Gebäudereiniger / Fahrzeugreiniger (einfach)" : [77],
    "Busfahrer (fertig / qual.)" : [128],
    "Busfahrer (Quer.)" : [126, 127, 129],
    "Triebfahrzeugführer / Lokrangierführer (Quer.)" : [56, 57, 125, 126, 127, 128, 129],
    "Triebfahrzeugführer / Lokrangierführer (fertig / qual.)" : [73],
    "Fahrdienstleiter (Quer.)" : [56, 57, 50, 150, 149, 151, 152, 153, 155, 157, 156],
    "Wagenmeister (Quer.)" : [37, 56, 57],
    "Rangierer / Zugvorbereiter (Quer.)" : [39, 70]
}


# In[7]:


# Zuordnung der Gehälter
Gehälter = {
    "Elektroingenieur" : [51],
    "Bauingenieur" : [98],
    "Recruiter" : [67],
    "HR-Partner/Personalreferent": [67],
    "Spezialisten und Berater HR / Change Management": [67],
    "Controller (Finance)" : [68],
    "Projektkaufmann / -leiter, Berater" : [66],
    "IT-Service / Betriebsführung" : [59],
    "IT-Entwicklung" : [60],
    "IT-Anwendungs- / Anforderungsmanagement, IT-Beratung" : [58],
    "IT-Strategie, -Projektmanagement, -Security" : [57],
    "Service im Zug (Quer.)" : [105],
    "Reiseberater" : [80],
    "Call Center Agent" : [81],
    "Elektrofachkräfte" : [95], 
    "Fahrweginstandhalter" : [117],
    "Schienfahrzeuginstandhalter" : [115],    
    "Servicetechniker Elektrotechnik / Telekommunikation" : [73],
    "Servicetechniker Maschinen- / Fördertechnik" : [72],
    "Servicetechniker Heizung / Klima / Lüftung / Sanitär" : [76],
    "Hausinspektor / Objektbetreuer": [75],
    "Sicherungsdienst / Ordnungsdienst" : [79], 
    "Fahrwegpfleger / Landschaftspfleger" : [125], # Updated, in aktueller Gehaltsliste noch nicht verfügbar
    "Gebäudereiniger / Fahrzeugreiniger" : [64],
    "Gebäudereiniger / Fahrzeugreiniger (einfach)" : [65],
    "Busfahrer (fertig / qual.)" : [77],
    "Busfahrer (Quer.)" : [102],
    "Triebfahrzeugführer / Lokrangierführer (Quer.)" : [91],
    "Triebfahrzeugführer / Lokrangierführer (fertig / qual.)" : [61],
    "Fahrdienstleiter (Quer.)" : [111],
    "Wagenmeister (Quer.)" : [88],
    "Rangierer / Zugvorbereiter (Quer.)" : [90]
}


# In[8]:


# Definiere Bundesländer
Bundesländer = {
    "Deutschland":[0],
    "Schleswig-Holstein":[1],
    "Hamburg":[2],
    "Niedersachsen":[3],
    "Bremen":[4],
    "Nordrhein-Westfalen":[5],
    "Hessen":[6],
    "Rheinland-Pfalz":[7],
    "Baden-Württemberg":[8],
    "Bayern":[9],
    "Saarland":[10],
    "Berlin":[11],
    "Brandenburg":[12],
    "Mecklenburg-Vorpommern":[13],
    "Sachsen":[14],
    "Sachsen-Anhalt":[15],
    "Thüringen":[16]
}


# In[9]:


# Bereinigung der Daten
def clean_data(df):
    df.replace("*", np.nan, inplace=True)
    for col in df.columns:
        if col in ["SVB ohne Azubis", "AGB"]:
            df[col] = df[col].astype("float64")
        if col in ["Arbeitslose"]:
            df[col] = df[col].astype("float64")
        if col in ["Stellen"]:
            df[col] = df[col].astype("float64")
    return df


# ## 1. Beschäftigte nach Bundesland

# ##### 1. Daten einlesen

# In[10]:


# daten laden
df_emp = pd.read_csv("Daten/202009_Besch_Laender.csv", sep=";")


# In[11]:


# erste fünf Zeilen
df_emp.head()


# In[12]:


# Anzahl der einzelnen Berufe ID´s
len(df_emp["Berufe ID"].unique())


# In[13]:


# letzter Eintrag
df_emp["Berufe ID"].max()


# In[14]:


# Datentypen
df_emp.dtypes


# In[15]:


# Bereinigung der Daten
df_emp = clean_data(df_emp)


# In[16]:


# erste fünf Zeilen
df_emp.head()


# ##### 2. Beschäftigte nach Berufe Clustern

# In[17]:


# Frauen ID
Frauen_ID = [2]


# In[18]:


# Formattierung der Daten
def format_emp_data(df, Bundesland):
    # leere liste um Ergebnisse zu speichern
    liste = []
    for key, value in Markt_Radar.items():
        # Definiere welche Zeilen bleiben sollen
        keep_gesamt = {"Berufe ID": value, "Bundesland": Bundesland}
        # Definiere welche Zeilen bleiben sollen
        keep_frauen = {"Berufe ID": value, "Bundesland": Bundesland, "Geschlecht":Frauen_ID}
        # filtere Dataframe für alle SVB´s
        df_ges = df[df[list(keep_gesamt)].isin(keep_gesamt).all(axis=1)]
        # filtere Dataframe für alle SVB´s
        df_fem = df[df[list(keep_frauen)].isin(keep_frauen).all(axis=1)]
        # Summiere SvB´s über Berufe
        ges_svb = df_ges["SVB ohne Azubis"].sum() 
        # Summiere AgB´s über Berufe
        fem_svb = df_fem["SVB ohne Azubis"].sum() 
        # AgB 
        ges_agb = df_ges["AGB"].sum()
        # fem AgB
        fem_agb = df_fem["AGB"].sum()
        # berechne Frauenquote 
        #fem_share = fem / ges 
        # erstelle liste mit allen relevanten Inhalten
        liste.append([key, ges_svb, fem_svb, ges_agb, fem_agb])
        # Konvertierung in Dataframe
        data = pd.DataFrame(liste)
        # Anp#ssung der Spaltennamen
        data.columns = ["Markt.Radar Suchbegriff", "SvB Gesamt", "SvB Frauen", "AgB Gesamt", "AgB Frauen"]
    # liste leeren
    liste.clear()
    # ausgabe Df
    return data


# In[19]:


# leere Liste um Ergebnisse zu speichern
list_of_df = []
# Beschäftigte für jedes Bundesland und jeden Beruf
for key, value in Bundesländer.items():
    # Formattierung der Daten für jeden Beruf 
    df_new = format_emp_data(df_emp, value)
    # Bundesland als Spalte ergänzen 
    df_new["Bundesland"] = key
    # index aktualisieren
    df_sorted = df_new.set_index(np.arange(1, len(df_new) + 1))
    # liste mit dataframe füllen
    list_of_df.append(df_sorted)


# In[20]:


# Zusammenführung der Dataframes 
df_all_emp = pd.concat(list_of_df)


# In[21]:


# alle außer Deutschland behalten
final_emp_bl = df_all_emp[df_all_emp["Bundesland"] != "Deutschland"]


# In[22]:


# Ausgabe der Bundesländer
final_emp_bl.Bundesland.unique()


# ##### 2. Beschäftigte Deutschland

# In[23]:


# daten laden
df_emp = pd.read_csv("Daten/202009_Besch_Deutschland.csv", sep=";")


# In[24]:


# erste fünf Zeilen
df_emp.head()


# In[25]:


# Bereinigung der Daten
df_emp = clean_data(df_emp)


# In[26]:


# ergänze Spalte Bundesland
df_emp["Bundesland"] = 0


# In[27]:


# leere Liste um Ergebnisse zu speichern
list_of_df = []
# Beschäftigte für jedes Bundesland und jeden Beruf
for key, value in Bundesländer.items():
    # Formattierung der Daten für jeden Beruf 
    df_new = format_emp_data(df_emp, value)
    # Bundesland als Spalte ergänzen 
    df_new["Bundesland"] = key
    # index aktualisieren
    df_sorted = df_new.set_index(np.arange(1, len(df_new) + 1))
    # liste mit dataframe füllen
    list_of_df.append(df_sorted)


# In[28]:


# Zusammenführung der Dataframes 
df_all_emp = pd.concat(list_of_df)


# In[29]:


# nur Deutschland behalten
df_all_emp = df_all_emp[df_all_emp["Bundesland"] == "Deutschland"]


# In[30]:


# erste fünf Zeilen
df_all_emp.head()


# In[31]:


# Zusammenführung der Beschäftigtendaten
final_emp = pd.concat([df_all_emp, final_emp_bl])


# In[32]:


# einzelne Bundesländer ausgeben
final_emp["Bundesland"].unique()


# ## 3. Arbeitslose nach Bundesländern und Deutschland

# In[33]:


# daten laden
df_alo = pd.read_csv("Daten/202009_ALO_B+Laender.csv", sep=";")


# In[34]:


# erste fünf Zeilen
df_alo.head()


# In[35]:


# Anzahl individueller Berufe
len(df_alo["Berufe ID"].unique())


# In[36]:


# letzter Berufe ID
df_alo["Berufe ID"].max()


# In[37]:


# Datentypen
df_alo.dtypes


# In[38]:


# Bereinigung der Daten
df_alo = clean_data(df_alo)


# In[39]:


# erste fünf Zeilen
df_alo.head()


# In[40]:


# Berechnung der Frauenquote für jeden DB Fokusberuf
def format_alo_data(df, Bundesland, variable="Arbeitslose",label="Alo Gesamt"):
    # leere liste um Ergebnisse zu speichern
    liste = []
    for key, value in Markt_Radar.items():
        # Definiere welche Zeilen bleiben sollen
        keep_gesamt = {"Berufe ID": value, "Bundesland": Bundesland}
        # Definiere welche Zeilen bleiben sollen
        keep_frauen = {"Berufe ID": value, "Bundesland": Bundesland, "Geschlecht":Frauen_ID}
        # filtere Dataframe für alle SVB´s
        df_ges = df[df[list(keep_gesamt)].isin(keep_gesamt).all(axis=1)]
        # filtere Dataframe für alle SVB´s
        df_fem = df[df[list(keep_frauen)].isin(keep_frauen).all(axis=1)]
        # Sämtliche Alos
        ges = df_ges[variable].sum()
        # weibliche Alos
        fem = df_fem[variable].sum() 
        # erstelle liste mit allen relevanten Inhalten
        liste.append([key, ges, fem])
        # Konvertierung in Dataframe
        data = pd.DataFrame(liste)
        # Anpassung der Spaltennamen
        data.columns = ["Markt.Radar Suchbegriff", label, "Alo Frauen"]
    # liste leeren
    liste.clear()
    # ausgabe Df
    return data


# In[41]:


# leere Liste um Ergebnisse zu speichern
list_of_df = []
# Alo für jedes Bundesland und jeden Beruf
for key, value in Bundesländer.items():
    # Formattierung der Daten 
    df_new = format_alo_data(df_alo, value)
    # Bundesland als Spalte ergänzen 
    df_new["Bundesland"] = key
    # index aktualisieren
    df_sorted = df_new.set_index(np.arange(1, len(df_new) + 1))
    # liste mit dataframe füllen
    list_of_df.append(df_sorted)


# In[42]:


# Zusammenführung der Dataframes 
df_all_alo = pd.concat(list_of_df)


# In[43]:


# erste fünf Zeilen für das Bundesland Bayern ausgeben
df_all_alo[df_all_alo["Bundesland"] == "Berlin"].head()


# ## 4. Stellenausschreibungen

# In[44]:


# daten laden
df_st = pd.read_csv("Daten/202009_SteA.csv", sep=";")


# In[45]:


# erste fünf Zeilen
df_st.head()


# In[46]:


# Anzahl individueller Berufe
len(df_st["Berufe ID"].unique())


# In[47]:


# letzter Eintrag der Berufe
df_st["Berufe ID"].max()


# In[48]:


# Datentypen
df_st.dtypes


# In[49]:


# Bereinigung der Daten
df_st = clean_data(df_st)


# In[50]:


# Berechnung der Frauenquote für jeden DB Fokusberuf
def format_st_data(df, Bundesland, variable="Stellen",label="Stellen Gesamt"):
    # leere liste um Ergebnisse zu speichern
    liste = []
    for key, value in Markt_Radar.items():
        # Definiere welche Zeilen bleiben sollen
        keep_gesamt = {"Berufe ID": value, "Bundesland": Bundesland}
        # filtere Dataframe für alle SVB´s
        df_ges = df[df[list(keep_gesamt)].isin(keep_gesamt).all(axis=1)]
        # Sämtliche Alos
        ges = df_ges[variable].sum()
        # erstelle liste mit allen relevanten Inhalten
        liste.append([key, ges])
        # Konvertierung in Dataframe
        data = pd.DataFrame(liste)
        # Anpassung der Spaltennamen
        data.columns = ["Markt.Radar Suchbegriff", label]
    # liste leeren
    liste.clear()
    # ausgabe Df
    return data


# In[51]:


# leere Liste um Ergebnisse zu speichern
list_of_df = []
# Alo für jedes Bundesland und jeden Beruf
for key, value in Bundesländer.items():
    # Formattierung der Daten 
    df_new = format_st_data(df_st, value)
    # Bundesland als Spalte ergänzen 
    df_new["Bundesland"] = key
    # index aktualisieren
    df_sorted = df_new.set_index(np.arange(1, len(df_new) + 1))
    # liste mit dataframe füllen
    list_of_df.append(df_sorted)


# In[52]:


# Zusammenführung der Dataframes 
df_all_st = pd.concat(list_of_df)


# In[53]:


# erste fünf Zeilen für das Bundesland Bayern ausgeben
df_all_st[df_all_st["Bundesland"] == "Berlin"].head()


# In[54]:


# Merge alo und Stellen
final_alo_stellen = pd.merge(df_all_st, df_all_alo, how="outer", on=["Markt.Radar Suchbegriff", "Bundesland"])


# In[55]:


# erste fünf Zeilen
final_alo_stellen.head()


# ## 5. Gehalt

# In[56]:


# daten laden
df_sal = pd.read_csv("Daten/Land Berufsgruppen Median.csv", sep=";", encoding= "unicode_escape") 


# In[57]:


# erste fünf Zeilen
df_sal.head()


# In[58]:


# Anzahl individueller Berufe / Berufsgruppen
len(df_sal["Berufe ID"].unique())


# In[66]:


# letzter Eintrag 
df_sal["Berufe ID"].max()


# In[67]:


# Datentypen
df_sal.dtypes


# In[68]:


# Formattierung der Spalte Bundesland
df_sal["Bundesland label"] = df_sal["Bundesland"].str.split(" ").str[1].str.strip()


# In[69]:


# Formattierung der Spalte Bundesland
df_sal["Bundesland"] = df_sal["Bundesland"].str.split(" ").str[0]


# In[70]:


# Formattierung der Spalte Bundesland
df_sal["Bundesland"].replace(["01", "02", "03", "04", "05", "06", "07", "08", "09"], 
                             ["1", "2", "3", "4", "5", "6", "7", "8", "9"], inplace=True)


# In[71]:


df_sal["Bundesland"] = df_sal["Bundesland"].astype("int64")


# In[72]:


# unlist values from Gehälter dictionary
l = []
for item in Gehälter.values():
    l.append(item[0])


# In[73]:


# boolean filter
mask = df_sal["Berufe ID"].isin(l)


# In[74]:


# Anpassung des Dataframes
df_new = df_sal[mask]


# In[75]:


# filter relevante Spalten
df_new = df_new[["Bundesland label", "Berufe ID", "Gehalt"]]


# In[76]:


# Umbenenung Spalten
df_new.columns = ["Bundesland", "Berufe ID", "Gehalt"]


# In[77]:


# erste fünf Zeilen
df_new.head()


# In[78]:


# Format Dataframe 
df_new.shape


# ### Deutschland Daten

# In[79]:


# daten laden
df_sal_deu = pd.read_csv("Daten/Deu Berufsgruppen Median.csv", sep=";", encoding= "unicode_escape") 


# In[80]:


# erste fünf Zeilen
df_sal_deu.head()


# In[81]:


# Anpassung des Dataframes
df_deu_new = df_sal_deu[mask]


# In[82]:


# erste fünf Zeilen
df_deu_new.head()


# In[83]:


# Zusammenführung der Bundesland und Deutschland Daten
sal = pd.concat([df_deu_new, df_new])


# In[84]:


# Prüfung des Formats
sal.shape


# In[85]:


# matching data
df_match = pd.DataFrame(Gehälter.items(), columns=["Markt.Radar Suchbegriff", "Berufe ID"])


# In[86]:


# unlist columns Berufe ID
l = []
for item in df_match["Berufe ID"]:
    l.append(item[0])


# In[87]:


# Spalte Berufe ID wieder mit ungelisteten Einträgen füllen
df_match["Berufe ID"] = l


# In[88]:


# erste fünf Zeilen
df_match.head()


# In[89]:


# Merge von alo und Kombination aus svb und agB
final_sal = pd.merge(sal, df_match, how="outer", on=["Berufe ID"])


# In[92]:


# Welche Variablen behalten
keep = ["Markt.Radar Suchbegriff", "Bundesland", "Gehalt"]


# In[93]:


# filter relevante Spalten
final_sal = final_sal[keep]


# In[95]:


# Merge alo und Stellen und Gehälter
final_alo_stellen_sal = pd.merge(final_alo_stellen, final_sal, how="outer", on=["Markt.Radar Suchbegriff", "Bundesland"])


# In[1100]:


# erste fünf Zeilen
final_alo_stellen_sal.head()


# ## 6. Merge Data

# In[96]:


# Merge von alo und Kombination aus svb und agB
final = pd.merge(final_emp, final_alo_stellen_sal, how="outer", on=["Markt.Radar Suchbegriff", "Bundesland"])


# In[97]:


# Spalten sortieren
columns = ["Markt.Radar Suchbegriff", "Bundesland", "SvB Gesamt", "SvB Frauen", "AgB Gesamt", "AgB Frauen", "Alo Gesamt", "Alo Frauen", "Stellen Gesamt", "Gehalt"]


# In[98]:


# neues Spaltenformat anwenden
final = final[columns]


# In[99]:


# Sortierung der Zeilen 
final = final.sort_values(["Bundesland", "Markt.Radar Suchbegriff"])


# In[100]:


# Anpassung des Index
final.index = np.arange(1, final.shape[0] + 1)


# In[101]:


# erste fünf Zeilen
final.head()


# In[102]:


# als Excel speichern
final.to_excel("Daten/Markt_Radar.xlsx", index=False)


# In[103]:


# Anzahl der Suchbegriffe im Markt.Radar 
len(final["Markt.Radar Suchbegriff"].unique())


# In[104]:


# Ausgabe der Suchbegriffe
final["Markt.Radar Suchbegriff"].unique()


# In[105]:


# Noch missings?
final.isna().sum()


# In[106]:


# Format des finalen Dataframes
final.shape


# In[ ]:





# In[ ]:




