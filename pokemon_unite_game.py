from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PokemonUniteArchipelagoOptions:
    pokemon_unite_pokemon_owned: PokemonUnitePokemonOwned


class PokemonUniteGame(Game):
    # Largely a fork of the League of Legends implementation (Proposed by @qwiskyy on Discord)

    name = "Pokémon Unite"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = PokemonUniteArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Cannot equip the following Held Items: ITEMS",
                data={
                    "ITEMS": (self.held_items, 3),
                },
            ),
            GameObjectiveTemplate(
                label="Cannot equip the following Battle Items: ITEMS",
                data={
                    "ITEMS": (self.battle_items, 2),
                },
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a match as POKEMON",
                data={
                    "POKEMON": (self.pokemon_pool, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a match as POKEMON with one of the following Held Items equipped: ITEMS",
                data={
                    "POKEMON": (self.pokemon_pool, 1),
                    "ITEMS": (self.held_items, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a match as POKEMON with the following Battle Item: ITEM",
                data={
                    "POKEMON": (self.pokemon_pool, 1),
                    "ITEM": (self.battle_items, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a match as a Pokémon with the following role: ROLE",
                data={
                    "ROLE": (self.roles, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a match as a Pokémon with the ROLE role with all of the following Held Items equipped: ITEMS",
                data={
                    "ROLE": (self.roles, 1),
                    "ITEMS": (self.held_items, 3),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def held_items() -> List[str]:
        return [
            "Muscle Band",
            "Scope Lens",
            "Shell Bell",
            "Wise Glasses",
            "Focus Band",
            "Energy Amplifier",
            "Float Stone",
            "Buddy Barrier",
            "Score Shield",
            "Aeos Cookie",
            "Attack Weight",
            "Sp. Atk Specs",
            "Leftovers",
            "Exp. Share",
            "Assault Vest",
            "Rocky Helmet",
            "Razor Claw",
            "Choice Specs",
            "Weakness Policy",
            "Rapid-Fire Scarf",
            "Drain Crown",
            "Slick Spoon",
            "Resuce Hood",
            "Curse Bangle",
            "Curse Incense",
            "Resonant Guard",
            "Charging Charm",
            "Accel Bracer",
            "Drive Lens",
            "Amulet Coin",
            "Choice Scarf",
        ]

    @staticmethod
    def battle_items() -> List[str]:
        return [
            "Potion",
            "X Attack",
            "X Speed",
            "Fluffy Tail",
            "Eject Button",
            "Slow Smoke",
            "Full Heal",
            "Goal-Getter",
            "Shedinja Doll",
            "Goal Hacker",
        ]

    def pokemon_pool(self) -> List[str]:
        return sorted(self.archipelago_options.pokemon_unite_pokemon_owned.value)
    
    #@staticmethod
    #def roles() -> List[str]:
        #return [
            #"Attacker",
            #"All-Rounder",
            #"Speedster",
            #"Defender",
            #"Supporter",
        #]
    
    @functools.cached_property
    def attacker_pokemon(self) -> List[str]:
        return [
            "Venusaur",
            "Pikachu",
            "Alolan Raichu",
            "Alolan Ninetales",
            "Mewtwo Y",
            "Mew",
            "Espeon",
            "Gardevoir",
            "Latios",
            "Glaceon",
            "Chandelure",
            "Delphox",
            "Greninja",
            "Sylveon",
            "Decidueye",
            "Cinderace",
            "Inteleon",
            "Cramorant",
            "Duraludon",
            "Dragapult",
            "Amarouge",
            "Miraidon",
        ]
    
    @functools.cached_property
    def all_rounder_pokemon(self) -> List[str]:
        return [
            "Charizard",
            "Machamp",
            "Gyardos",
            "Dragonite",
            "Mewtwo X",
            "Azumarill",
            "Scizor",
            "Suicune",
            "Tyranitar",
            "Blaziken",
            "Metagross",
            "Empoleon",
            "Garchomp",
            "Lucario",
            "Aegislash",
            "Tsareena",
            "Mimikyu",
            "Dhelmise",
            "Buzzwole",
            "Falinks",
            "Zacian",
            "Urshifu",
            "Pawmot"
            "Ceruledge",
            "Tinkaton",
        ]
    
    @functools.cached_property
    def speedster_pokemon(self) -> List[str]:
        return [
            "Galarian Rapidash",
            "Dodrio",
            "Gengar",
            "Absol",
            "Leafeon",
            "Darkrai",
            "Zoroark",
            "Talonflame",
            "Zeraora",
            "Meowscarada",
        ]
    
    @functools.cached_property
    def defender_pokemon(self) -> List[str]:
        return [
            "Blastoise",
            "Slowbro",
            "Lapras",
            "Vaporeon",
            "Snorlax",
            "Umbreon",
            "Ho-Oh",
            "Mamoswine",
            "Crustle",
            "Goodra",
            "Trevenant",
            "Greedent",
        ]

    @functools.cached_property
    def supporter_pokemon(self) -> List[str]:
        return [
            "Clefable",
            "Wigglytuff",
            "Psyduck",
            "Mr. Mime",
            "Blissey",
            "Sableye",
            "Latias",
            "Hoopa",
            "Comfey",
            "Eldegoss",
            "Alcremie",
        ]

    def roles(self) -> List[str]:
        roles: List[str] = list()
        #pokemon_pool = self.pokemon_pool

        for pokemon in self.attacker_pokemon:
            if pokemon in self.pokemon_pool():
                roles.append("Attacker")
                break

        for pokemon in self.all_rounder_pokemon:
            if pokemon in self.pokemon_pool():
                roles.append("All-Rounder")
                break

        for pokemon in self.speedster_pokemon:
            if pokemon in self.pokemon_pool():
                roles.append("Speedster")
                break

        for pokemon in self.defender_pokemon:
            if pokemon in self.pokemon_pool():
                roles.append("Defender")
                break

        for pokemon in self.supporter_pokemon:
            if pokemon in self.pokemon_pool():
                roles.append("Supporter")
                break

        return sorted(roles)

# Archipelago Options
class PokemonUnitePokemonOwned(OptionSet):
    """
    Indicates which Pokémon the player owns in Pokémon Unite and wants to play.
    """

    display_name = "Pokémon Unite Pokémon Owned"
    valid_keys = [
            "Venusaur",
            "Charizard",
            "Blastoise",
            "Pikachu",
            "Alolan Raichu",
            "Clefable",
            "Alolan Ninetales",
            "Wigglytuff",
            "Psyduck",
            "Machamp",
            "Galarian Rapidash",
            "Slowbro",
            "Dodrio",
            "Gengar",
            "Mr. Mime",
            "Gyarados",
            "Lapras",
            "Vaporeon",
            "Snorlax",
            "Dragonite",
            "Mewtwo X",
            "Mewtwo Y",
            "Mew",
            "Azumarill",
            "Espeon",
            "Umbreon",
            "Scizor",
            "Blissey",
            "Suicune",
            "Tyranitar",
            "Ho-Oh",
            "Blaziken",
            "Gardevoir",
            "Sableye",
            "Absol",
            "Metagross",
            "Latias",
            "Latios",
            "Empoleon",
            "Garchomp",
            "Lucario",
            "Leafeon",
            "Glaceon",
            "Mamoswine",
            "Darkrai",
            "Crustle",
            "Zoroark",
            "Chandelure",
            "Delphox",
            "Greninja",
            "Talonflame",
            "Aegislash",
            "Sylveon",
            "Goodra",
            "Trevenant",
            "Hoopa",
            "Decidueye",
            "Tsareena",
            "Comfey",
            "Mimikyu",
            "Dhelmise",
            "Buzzwole",
            "Zeraora",
            "Cinderace",
            "Inteleon",
            "Greedent",
            "Eldegoss",
            "Cramorant",
            "Alcremie",
            "Falinks",
            "Duraludon",
            "Dragapult",
            "Zacian",
            "Urshifu",
            "Meowscarada",
            "Pawmot",
            "Armarouge",
            "Ceruledge",
            "Tinkaton",
            "Miraidon",
        ]

    default = valid_keys
