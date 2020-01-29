import math
import random

from src.entities.projectiles.bad_missile import BadMissile
from src.entities.projectiles.bullet import Bullet
from src.entities.projectiles.missile import Missile
from src.entities.ships.enemies.ship import Ship
from src.entity_id import EntityID
from src.model.stats.ship_stats import get_ship_stats

"""Represents an enemy ship or structure."""


class Enemy(Ship):
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
    :param move_again: determines if it continuously moves
    :type move_again: bool
    :param fps: frames per second
    :type fps: int
    :param entity_id: ID of enemy
    :type entity_id: EntityID
    """

    def __init__(self, ship_size, x, y, hp, end_x, end_y, speed, fire_rate, shield, move_again, fps, entity_id):
        super().__init__(x, y, hp, shield, ship_size, fps)
        self.entity_id = entity_id
        self.fps = fps
        stats = get_ship_stats(entity_id)
        self.projectile_damage = stats["DAMAGE"]
        self.projectile_speed = stats["PROJECTILE SPEED"] * (30 / fps)
        self.score = stats["SCORE"]
        self.projectile_type = EntityID.ENEMY_BULLET
        # fire rate in seconds
        self.fire_rate = fire_rate
        # current ticks
        self.ticks = 0
        # Determines the final moving position
        x_dif = abs(end_x - x)
        y_dif = abs(end_y - y)
        self.speed = speed
        if speed <= 0:
            speed = 1
        self.end_x = int((x_dif // speed) * speed)
        self.end_y = int((y_dif // speed) * speed)
        # Angle it is facing
        self.angle = 0
        # If it is ready to fire again
        self.ready_to_fire = True
        # Angle offset to fire in
        # If greater than 0, fires in a cone of 2 * fire_variance degrees
        self.fire_variance = 0
        # If it is done moving to its end position
        self.finished_moving = False
        # If it continues moving to a new location
        self.move_again = move_again

    """Moves the enemy to its predetermined location.
    """

    def move(self):
        if self.speed > 0:
            x_done = False
            if self.x < self.end_x - self.speed:
                self.x += self.speed
            elif self.x > self.end_x + self.speed:
                self.x -= self.speed
            else:
                x_done = True

            if self.y < self.end_y - self.speed:
                self.y += self.speed
            elif self.y > self.end_y + self.speed:
                self.y -= self.speed
            else:
                self.finished_moving = x_done

    """Represents the angle the enemy is facing.
    
    :param target: target the enemy is facing
    :type target: Ship
    """

    def rotate(self, target):
        # Rotates the ship to face the target ship
        self.angle = -math.degrees(math.atan2(target.y - self.y, target.x - self.x)) + 90

    """Fires projectiles from the enemy to the given target, at the given speed, damage, and size.

        :param target: target area
        :type target: Ship
        :param projectiles: list of projectiles to append onto
        :type projectiles: List of Projectile
        """

    def fire(self, target, projectiles):
        # Finds angle from source to target
        # If the enemy ship has any spread
        x_pos = self.x
        y_pos = self.y
        if self.size > 100:
            x_pos = self.x + ((self.size - 100) // 2)
            y_pos = self.y + ((self.size - 100) // 2)
        offset = random.randint(-self.fire_variance, self.fire_variance)
        angle = self.angle - 90 + offset
        weapon_type = self.projectile_type
        projectile = Bullet(self.projectile_speed, x_pos, y_pos,
                            angle + offset, self.projectile_damage, 100,
                            weapon_type)
        if weapon_type == EntityID.ENEMY_MISSILE:
            projectile = Missile(self.projectile_speed, x_pos, y_pos,
                                 angle, self.projectile_damage, 100,
                                 weapon_type, target)
        elif weapon_type == EntityID.BAD_MISSILE:
            projectile = BadMissile(self.projectile_speed, x_pos, y_pos,
                                    angle, self.projectile_damage, 100,
                                    EntityID.ENEMY_BULLET, target)

        projectiles.append(projectile)
