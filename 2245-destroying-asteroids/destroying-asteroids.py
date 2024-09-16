class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        planet_size = mass

        for asteroid in asteroids:
            if planet_size >= asteroid:
                planet_size += asteroid
            else:
                return False
        return True
        