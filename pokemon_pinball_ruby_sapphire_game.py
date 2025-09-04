from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PokemonPinballRSArchipelagoOptions:
    pokemon_pinball_rs_include_rare_spawns: PokemonPinballRSIncludeRareSpawns


class PokemonPinballRSGame(Game):
    name = "Pokémon Pinball: Ruby & Sapphire"
    platform = KeymastersKeepGamePlatforms.GBA

    platforms_other = [
		KeymastersKeepGamePlatforms.WIIU,
	]

    is_adult_only_or_unrated = False

    options_cls = PokemonPinballRSArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete an objective without shaking the table",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Complete an objective without losing a ball",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Complete an objective without spending anything at the Pokémon Mart",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Catch a Pokémon with aBALL Ball (or better)",
                data={
                    "BALL": (self.balls, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete the STAGE Bonus Stage",
                data={
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
			GameObjectiveTemplate(
                label="Catch a Pokémon while in the LOCATION Area",
                data={
                    "LOCATION": (self.locations, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
			GameObjectiveTemplate(
                label="Score at least SCORE,000,000 points in a single game on the TABLE Field",
                data={
                    "SCORE": (self.score_goal, 1),
					"TABLE": (self.tables, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Hatch and catch an egg Pokémon on the TABLE Field",
                data={
                    "TABLE": (self.tables, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
			GameObjectiveTemplate(
                label="Participate in the Spheal bonus stage on the TABLE Field and score BASKETS Spheal baskets",
                data={
                    "TABLE": (self.tables, 1),
                    "BASKETS": (self.basket_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
			GameObjectiveTemplate(
                label="Evolve a Pokémon on the TABLE Field",
                data={
                    "TABLE": (self.tables, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
			GameObjectiveTemplate(
                label="Catch the following Pokémon: POKEMON",
                data={
                    "POKEMON": (self.pokemon, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
        ]

    @property
    def include_rare_spawns(self) -> bool:
        return bool(self.archipelago_options.pokemon_pinball_rs_include_rare_spawns.value)

    @functools.cached_property
    def pokemon_base(self) -> List[str]:
        return [
            "Treecko",
            "Torchic",
            "Mudkip",
            "Poochyena",
            "Zigzagoon",
            "Silcoon",
            "Cascoon",
            "Lombre",
            "Nuzleaf",
            "Taillow",
            "Wingull",
            "Slakoth",
            "Abra",
            "Nincada",
            "Loudred",
            "Makuhita",
            "Goldeen",
            "Magikarp",
            "Marill",
            "Geodude",
            "Nosepass",
            "Tentacool",
			"Sableye",
			"Mawile",
			"Machop",
			"Meditite",
			"Electrike",
			"Magnemite",
			"Voltorb",
			"Volbeat",
			"Illumise",
			"Doduo",
			"Roselia",
			"Carvanha",
			"Wailmer",
			"Numel",
			"Slugma",
			"Torkoal",
			"Grimer",
			"Koffing",
			"Skarmory",
			"Vibrava",
			"Cacnea",
			"Swablu",
			"Zangoose",
			"Seviper",
			"Lunatone",
			"Solrock",
			"Barboach",
			"Corphish",
			"Baltoy",
			"Lileep",
			"Anorith",
			"Jigglypuff",
			"Feebas",
			"Castform",
			"Staryu",
			"Kecleon",
			"Duskull",
			"Tropius",
			"Absol",
			"Vulpix",
			"Pikachu",
			"Psyduck",
			"Wobbuffet",
			"Girafarig",
			"Pinsir",
			"Heracross",
			"Rhyhorn",
			"Clamperl",
			"Relicanth",
			"Luvdisc",
			"Shelgon",
			"Kyogre",
			"Groudon",
        ]

    @functools.cached_property
    def pokemon_rare(self) -> List[str]:
        return [
            "Beldum",
            "Regirock",
            "Regice",
            "Registeel",
			"Latias",
			"Latios",
			"Rayquaza",
			"Jirachi",
        ]

    def pokemon(self) -> List[str]:
        pokemon: List[str] = self.pokemon_base[:]

        if self.include_rare_spawns:
            pokemon.extend(self.pokemon_rare)

        return sorted(pokemon)

    @functools.cached_property
    def locations_base(self) -> List[str]:
        return [
            "Forest",
			"Plains",
			"City",
			"Cave",
			"Safari Zone",
			"Volcano",
			"Sea",
			"Lake",
			"Desert",
        ]

    @functools.cached_property
    def locations_rare(self) -> List[str]:
        return [
            "Ruins",
        ]

    def locations(self) -> List[str]:
        locations: List[str] = self.locations_base[:]

        if self.include_rare_spawns:
            locations.extend(self.locations_rare)

        return sorted(locations)
	
    @staticmethod
    def balls() -> List[str]:
        return [
            " Great",
            "n Ultra",
            " Master",
        ]

    @staticmethod
    def stages() -> List[str]:
	    return [
		    "Kecleon",
		    "Kecleon",
		    "Kecleon",
		    "Dusclops",
		    "Dusclops",
		    "Dusclops",
		    "Groudon",
		    "Groudon",
		    "Kyogre",
		    "Kyogre",
		    "Rayquaza",
	    ]

    @staticmethod
    def score_goal() -> List[str]:
        return [
            "100",
            "125",
            "150",
            "175",
            "200",
            "225",
            "250",
            "275",
            "300",
        ]

    @staticmethod
    def tables() -> List[str]:
        return [
            "Ruby",
            "Sapphire",
        ]

    @staticmethod
    def basket_range() -> range:
        return range(1, 6)

# Archipelago Options
class PokemonPinballRSIncludeRareSpawns(Toggle):
    """
    Whether to include specific rare spawns, such as the Ruins spawns and the Eon Twins, in Pokémon Pinbal: Ruby & Sapphire objectives.
    """

    display_name = "Pokémon Pinball: Ruby & Sapphire Include Rare Spawns"
