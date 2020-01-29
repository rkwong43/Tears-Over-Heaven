from src.entities.ships.enemies.enemy import Enemy
from src.entity_id import EntityID

"""Represents a Subjugator enemy fighter."""


class Subjugator(Enemy):
    """Constructor to make the enemy.

    :param ship_size: size the ship is
    :type ship_size: int
    :param x: starting x coordinate of ship
    :type x: int
    :param y: starting y coordinate of ship
    :type y: int
    :param hp: hit points of ship
    :type hp: int
    :param end_x: ending x position
    :type end_x: int
    :param end_y: ending y position
    :type end_y: int
    :param speed: speed it moves towards the ending position
    :type speed: int
    :param fire_rate: fire rate of the enemy
    :type fire_rate: int
    :param shield: shield health
    :type shield: int
    :param fps: Frames per second
    :type fps: int
    """

    def __init__(self, ship_size, x, y, hp, end_x, end_y, speed, fire_rate, shield, fps):
        super().__init__(ship_size, x, y, hp, end_x, end_y, speed, fire_rate, shield, True, fps, EntityID.SUBJUGATOR)
        self.projectile_type = EntityID.ENEMY_MISSILE
