from src.utils.config import Config
from src.api.client import testClient

fixtures = {
    "fixtures": [
        {
            "home": "Manchester City",
            "away": "Liverpool",
            "competition": "Premier League",
            "time": "2025-01-18 17:30",
            "stadium": "Etihad Stadium"
        },
        {
            "home": "Real Madrid",
            "away": "Barcelona",
            "competition": "La Liga",
            "time": "2025-02-02 20:00",
            "stadium": "Santiago Bernabéu"
        },
        {
            "home": "Bayern Munich",
            "away": "Borussia Dortmund",
            "competition": "Bundesliga",
            "time": "2025-03-09 18:30",
            "stadium": "Allianz Arena"
        },
        {
            "home": "Juventus",
            "away": "Inter Milan",
            "competition": "Serie A",
            "time": "2025-01-26 21:45",
            "stadium": "Allianz Stadium"
        },
        {
            "home": "Paris Saint-Germain",
            "away": "Olympique Marseille",
            "competition": "Ligue 1",
            "time": "2025-02-15 21:00",
            "stadium": "Parc des Princes"
        },
        {
            "home": "Ajax",
            "away": "PSV Eindhoven",
            "competition": "Eredivisie",
            "time": "2025-02-23 16:45",
            "stadium": "Johan Cruyff Arena"
        },
        {
            "home": "Benfica",
            "away": "Porto",
            "competition": "Primeira Liga",
            "time": "2025-03-01 21:15",
            "stadium": "Estádio da Luz"
        },
        {
            "home": "Sporting KC",
            "away": "LA Galaxy",
            "competition": "MLS",
            "time": "2025-04-05 19:30",
            "stadium": "Children’s Mercy Park"
        },
        {
            "home": "River Plate",
            "away": "Boca Juniors",
            "competition": "Primera División",
            "time": "2025-03-16 18:00",
            "stadium": "Monumental"
        },
        {
            "home": "Celtic",
            "away": "Rangers",
            "competition": "Scottish Premiership",
            "time": "2025-01-31 12:30",
            "stadium": "Celtic Park"
        }
    ]
}

premier_league_standings = {
    "competition": "Premier League",
    "season": "2024/25",
    "updated": "2025-01-15",
    "table": [
        {"pos": 1, "team": "Manchester City", "played": 20, "won": 15, "drawn": 3, "lost": 2, "gf": 48, "ga": 17, "gd": 31, "points": 48},
        {"pos": 2, "team": "Liverpool", "played": 20, "won": 14, "drawn": 4, "lost": 2, "gf": 44, "ga": 18, "gd": 26, "points": 46},
        {"pos": 3, "team": "Arsenal", "played": 20, "won": 13, "drawn": 4, "lost": 3, "gf": 40, "ga": 19, "gd": 21, "points": 43},
        {"pos": 4, "team": "Aston Villa", "played": 20, "won": 12, "drawn": 4, "lost": 4, "gf": 38, "ga": 24, "gd": 14, "points": 40},
        {"pos": 5, "team": "Tottenham Hotspur", "played": 20, "won": 12, "drawn": 3, "lost": 5, "gf": 41, "ga": 30, "gd": 11, "points": 39},
        {"pos": 6, "team": "Manchester United", "played": 20, "won": 10, "drawn": 5, "lost": 5, "gf": 31, "ga": 25, "gd": 6, "points": 35},
        {"pos": 7, "team": "Newcastle United", "played": 20, "won": 9, "drawn": 4, "lost": 7, "gf": 34, "ga": 28, "gd": 6, "points": 31},
        {"pos": 8, "team": "Brighton", "played": 20, "won": 8, "drawn": 6, "lost": 6, "gf": 33, "ga": 30, "gd": 3, "points": 30},
        {"pos": 9, "team": "Chelsea", "played": 20, "won": 8, "drawn": 5, "lost": 7, "gf": 32, "ga": 29, "gd": 3, "points": 29},
        {"pos": 10, "team": "West Ham United", "played": 20, "won": 8, "drawn": 5, "lost": 7, "gf": 30, "ga": 29, "gd": 1, "points": 29},
        {"pos": 11, "team": "Brentford", "played": 20, "won": 7, "drawn": 5, "lost": 8, "gf": 28, "ga": 29, "gd": -1, "points": 26},
        {"pos": 12, "team": "Wolves", "played": 20, "won": 7, "drawn": 4, "lost": 9, "gf": 26, "ga": 29, "gd": -3, "points": 25},
        {"pos": 13, "team": "Crystal Palace", "played": 20, "won": 6, "drawn": 6, "lost": 8, "gf": 22, "ga": 27, "gd": -5, "points": 24},
        {"pos": 14, "team": "Everton", "played": 20, "won": 6, "drawn": 5, "lost": 9, "gf": 21, "ga": 26, "gd": -5, "points": 23},
        {"pos": 15, "team": "Bournemouth", "played": 20, "won": 6, "drawn": 5, "lost": 9, "gf": 24, "ga": 33, "gd": -9, "points": 23},
        {"pos": 16, "team": "Fulham", "played": 20, "won": 5, "drawn": 6, "lost": 9, "gf": 22, "ga": 31, "gd": -9, "points": 21},
        {"pos": 17, "team": "Nottingham Forest", "played": 20, "won": 5, "drawn": 5, "lost": 10, "gf": 20, "ga": 30, "gd": -10, "points": 20},
        {"pos": 18, "team": "Luton Town", "played": 20, "won": 4, "drawn": 5, "lost": 11, "gf": 19, "ga": 31, "gd": -12, "points": 17},
        {"pos": 19, "team": "Burnley", "played": 20, "won": 3, "drawn": 4, "lost": 13, "gf": 18, "ga": 35, "gd": -17, "points": 13},
        {"pos": 20, "team": "Sheffield United", "played": 20, "won": 2, "drawn": 4, "lost": 14, "gf": 14, "ga": 40, "gd": -26, "points": 10}
    ]
}

def test_setup():
    try:
        # Initialize Config
        cfg = Config()
        print("✅ Configuration module loaded.")

        # Test Reading YAML
        url = cfg.get("api.base_url")
        print(f"✅ Read from YAML: Base URL is '{url}'")

        # Test Reading API Key (Securely)
        key = cfg.get_api_key()
        print(f"✅ API Key found: {key[:4]}****************")


    except Exception as e:
        print(f"\n❌ ERROR: {e}")

    try:
        test_client = testClient(fixtures, premier_league_standings)
        print(test_client.get_fixtures())
        print(test_client.get_standings())

    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    test_setup()