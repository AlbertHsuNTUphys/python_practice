import copy

class Planet:
    def __init__(self, name, coord, mass):
        self.name = name
        self.coord = coord
        self.mass = mass

    def __str__(self):
        return f'Planet - {self.name}' 

    def __add__(self, other):
        mx = self.mass
        my = other.mass
        # print(self.coord)
        # print(other.coord)
        cm_coord = tuple([ (a*mx+b*my)/(mx+my) for a, b in zip(self.coord, other.coord)])
        # print(cm_coord)
        return Planet(self.name+other.name, cm_coord, mx+my)

    def __lt__(self, other):
        return (self.coord[0]**2 + self.coord[1]**2 + self.coord[2]**2) < (other.coord[0]**2 + other.coord[1]**2 + other.coord[2]**2)
    
class PlanetSystem:
    def __init__(self, list_of_planets):
        self.planets = copy.deepcopy(list_of_planets)

    def add(self, planet):
        self.planets.append(planet)
    
    def delete(self, planetName):
        for i in range(len(self.planets)):
            if self.planets[i].name == planetName:
                target = i 
                break
        self.planets.pop(target)

    def __iter__(self):
        return iter(sorted(self.planets))

if __name__ == "__main__":
    earth = Planet("Earth",(0,0,0),1)
    venus = Planet("Venus",(1,1,1),0.8)
    mercury = Planet("Mercury",(2,2,2),0.5)
    moon =  Planet("Moon",(0,0,1),0.01)
 
    # solar_system = PlanetSystem([mercury, earth, venus])
    # for p in solar_system:
        # print(p)
    new_planet = mercury + moon
    solar_system = PlanetSystem([venus,earth])
    solar_system.add(new_planet)
    for each in solar_system:
        print(each)
    solar_system.delete("MercuryMoon")
    print("===after_delete===")
    for each in solar_system:
        print(each) 
