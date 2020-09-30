import pandas as pd
vakiluku = pd.read_csv("vakiluku_2019.csv", index_col=0, encoding="UTF-8", names=["Alue","Tiedot","Väkiluku"])
vakiluku = vakiluku.drop(vakiluku.columns[0],axis=1)

syntyneiden_enemmyys = pd.read_csv("syntyneiden_enemmyys_2019.csv", index_col=0, encoding="UTF-8", names=["Alue","Tiedot","Syntyneiden enemmyys, henkilöä"])
syntyneiden_enemmyys = syntyneiden_enemmyys.drop(syntyneiden_enemmyys.columns[0],axis=1)

muuttotappio = pd.read_csv("muuttotappio_2019.csv", index_col=0, encoding="UTF-8", names=["Alue","Tiedot","Muuttovoitto/-tappio"])
muuttotappio = muuttotappio.drop(muuttotappio.columns[0],axis=1)

yhdistetty_taulukko = vakiluku.merge(syntyneiden_enemmyys, on="Alue")
yhdistetty_taulukko = yhdistetty_taulukko.merge(muuttotappio, on="Alue")


lajittelu_vakiluvulla = yhdistetty_taulukko.sort_values("Väkiluku",ascending=False)
lajittelu_syntyneet = yhdistetty_taulukko.sort_values("Syntyneiden enemmyys, henkilöä")
lajittelu_muuttotappio = yhdistetty_taulukko.sort_values("Muuttovoitto/-tappio", ascending=True)

vakiluku_suurin = yhdistetty_taulukko[yhdistetty_taulukko["Väkiluku"] == yhdistetty_taulukko["Väkiluku"].max()]
vakiluku_pienin = yhdistetty_taulukko[yhdistetty_taulukko["Väkiluku"] == yhdistetty_taulukko["Väkiluku"].min()]
vakiluku_keskiarvo = yhdistetty_taulukko["Väkiluku"].mean()
vakiluku_mediaani = yhdistetty_taulukko["Väkiluku"].median()

syntyneet_max = yhdistetty_taulukko[yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"] == yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"].max()]
syntyneet_min = yhdistetty_taulukko[yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"] == yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"].min()]
syntyneet_keskiarvo = yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"].mean()
syntyneet_mediaani = yhdistetty_taulukko["Syntyneiden enemmyys, henkilöä"].median()

