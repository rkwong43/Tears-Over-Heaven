from src.utils.ids.projectile_id import ProjectileID
from src.utils.ids.weapon_id import WeaponID

"""Initializes all weapon stats in the game for the player.
"""
# Note: Do weapon spread as a multiple of COUNT + 1 for consistent integer rounding for spread
stats = {WeaponID.GUN: {"PROJECTILE SPEED": 20, "SPREAD": 0, "PROJECTILE TYPE": ProjectileID.FRIENDLY_BULLET,
                        "DAMAGE": 20, "RELOAD": 6, "PROJECTILE COUNT": 1, "DPS": 100,
                        "DESCRIPTION": "Fires lethal blasts of plasma in a straight line."},
         WeaponID.FLAK_CANNON: {"PROJECTILE SPEED": 10, "SPREAD": 24, "PROJECTILE TYPE": ProjectileID.FRIENDLY_FLAK,
                                "DAMAGE": 10, "RELOAD": 10, "PROJECTILE COUNT": 3, "DPS": 90,
                                "DESCRIPTION": "Fires an array of volatile plasma that detonate near enemies."},
         WeaponID.MACHINE_GUN: {"PROJECTILE SPEED": 15, "SPREAD": 10,
                                "PROJECTILE TYPE": ProjectileID.FRIENDLY_BULLET,
                                "DAMAGE": 10, "RELOAD": 3, "PROJECTILE COUNT": 1, "DPS": 100,
                                "DESCRIPTION": "Rapidly fires rounds in a spread."},
         WeaponID.SHOTGUN: {"PROJECTILE SPEED": 15, "SPREAD": 14, "PROJECTILE TYPE": ProjectileID.FRIENDLY_BULLET,
                            "DAMAGE": 5, "RELOAD": 8, "PROJECTILE COUNT": 6, "DPS": 120,
                            "DESCRIPTION": "Fires an inaccurate spread of plasma rounds."},
         WeaponID.FLAK_GUN: {"PROJECTILE SPEED": 15, "SPREAD": 5, "PROJECTILE TYPE": ProjectileID.FRIENDLY_FLAK,
                             "DAMAGE": 15, "RELOAD": 8, "PROJECTILE COUNT": 1, "DPS": 60,
                             "DESCRIPTION": "Fires an orb of explosive plasma that detonates near enemies."},
         WeaponID.MISSILE_LAUNCHER: {"PROJECTILE SPEED": 24, "SPREAD": 0,
                                     "PROJECTILE TYPE": ProjectileID.FRIENDLY_MISSILE,
                                     "DAMAGE": 30, "RELOAD": 16, "PROJECTILE COUNT": 1, "DPS": 50,
                                     "DESCRIPTION": "Launches a plasma missile that homes in on foes."},
         WeaponID.MULTI_MISSILE: {"PROJECTILE SPEED": 20, "SPREAD": 20,
                                  "PROJECTILE TYPE": ProjectileID.FRIENDLY_MISSILE,
                                  "DAMAGE": 20, "RELOAD": 16, "PROJECTILE COUNT": 4, "DPS": 40,
                                  "DESCRIPTION": "Launches an array of homing plasma missiles at enemies."},
         WeaponID.DIAMOND_DUST: {"PROJECTILE SPEED": 10, "SPREAD": 45, "PROJECTILE TYPE": ProjectileID.DIAMOND_DUST,
                                 "DAMAGE": 5, "RELOAD": 16, "PROJECTILE COUNT": 5, "DPS": 50,
                                 "DESCRIPTION": "Creates a burst of compressed plasma shards that track enemies."},
         WeaponID.RAILGUN: {"PROJECTILE SPEED": 40, "SPREAD": 0, "PROJECTILE TYPE": ProjectileID.RAILGUN_BLAST,
                            "DAMAGE": 25, "RELOAD": 32, "PROJECTILE COUNT": 1, "DPS": (25, 100),
                            "DESCRIPTION": "Generates a high-velocity blast of super-compressed plasma."},
         WeaponID.STRIKER: {"PROJECTILE SPEED": 25, "SPREAD": 0, "PROJECTILE TYPE": ProjectileID.HOMING_BULLET,
                            "DAMAGE": 8, "RELOAD": 3, "PROJECTILE COUNT": 1, "DPS": 80,
                            "DESCRIPTION": "Rapidly fires homing plasma rounds at enemies."}
         }
