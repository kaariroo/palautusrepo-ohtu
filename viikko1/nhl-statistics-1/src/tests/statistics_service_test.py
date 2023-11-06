import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_selfplayers_toimii(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_search_palauttaa_none_vaaralla_nimella(self):
        self.assertAlmostEqual(self.stats.search("Roope"), None)

    def test_search_palauttaa_pelaajan(self):
        nimi = self.stats.search("Semenko")

        self.assertAlmostEqual(nimi.name, "Semenko")

    def test_joukkue_on_oikean_kokoinen(self):
        team = self.stats.team("EDM")
        self.assertAlmostEqual(len(team), 3)

    def test_top_menee_oikein(self):
        top5 = self.stats.top(5)

        self.assertAlmostEqual(top5[0].name, "Gretzky")

    def test_syottajien_top_menee_oikein(self):
        top5 = self.stats.top(5, SortBy.ASSISTS)

        self.assertAlmostEqual(top5[0].name, "Gretzky")
        self.assertAlmostEqual(top5[1].name, "Yzerman")
        self.assertAlmostEqual(top5[2].name, "Lemieux")

    def test_maalaajien_top_menee_oikein(self):
        top5 = self.stats.top(5, SortBy.GOALS)

        self.assertAlmostEqual(top5[0].name, "Lemieux")
        self.assertAlmostEqual(top5[1].name, "Yzerman")
        self.assertAlmostEqual(top5[2].name, "Kurri")

    def test_outo_syote_top_menee_oikein_eli_pisteiden_mukaan(self):
        top5 = self.stats.top(5, "Hämysyöte")

        self.assertAlmostEqual(top5[0].name, "Gretzky")
        self.assertAlmostEqual(top5[1].name, "Lemieux")
        self.assertAlmostEqual(top5[2].name, "Yzerman")