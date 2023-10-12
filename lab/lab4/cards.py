# All cards available in a standard deck.
from classes import *

#TAs
kavi = TACard('Kavi Gupta', 1500, 1800)
danelle = TACard('Danelle Nachos', 2000, 1300)
dalton = TACard('Dalton, Purveyor of Fate and Omens', 2300, 1000)
tiffany = TACard('Tall Tiff', 1400, 2000)
gibbes = TACard('Gibbes, Free Energy Detective Pirate', 1000, 2000)
keon = TACard('Keon-u Reeves', 2300, 1100)
derrick = TACard('EZ4ENCE', 1000, 2400)
griffin = TACard('Griffin, Maximizer of Gains', 1100, 2300)
kevin_w = TACard('Kevin, the human embodiment of ma po tofu', 1700, 1700)
michelle = TACard('Michelle, Ice Cream Consumer', 2100, 1100)
anita = TACard("Anita, the Amazin' Avocado", 1500, 1900)
lindsay = TACard('Lion Lindsay', 2000, 1400)
derek = TACard('Derek, The Wan and Only', 1500, 1500)
tim = TACard('Tim, the Forester', 2200, 1000)
lillian = TACard('Lillian', 1600, 1700)
cesar = TACard("Cesar 'Yung Steaz' P.Z.", 1600, 1700)
cameron = TACard('Sensei Cameron', 1500, 1600)
audrey = TACard('Audrey, Traverser of Trees', 1600, 1800)
nancy = TACard('Banancy', 1000, 2400)
albert = TACard('Albert boi xu', 1000, 2000)
jacob = TACard('Jacob the Jubilant', 1700, 1700)
chris_a = TACard('Chris, Caller of Men', 2100, 1200)
shea = TACard('Shea Butter', 2200, 1100)
alex = TACard('President Lieutenant Stennet for Senate', 1600, 1700)
caroline = TACard('Caroline, The Always Offline', 1600, 1800)
amy_h = TACard('Amy, Always Hung-ry', 1600, 1800)
kate = TACard('Kate, Jar of Exponential Runtime', 2300, 1000)

#Tutors
rachel = TutorCard('Rachel "Genes of Jeans" De Jaen', 1600, 1500)
carl = TutorCard('Carl the Qi', 1600, 1500)
evan_l = TutorCard('Evan, rhymes with Seven', 1500, 1900)
abhinav = TutorCard('Abhinav, Fan of Durant', 1700, 1500)
jacqueline = TutorCard('Jacqueline, The Yeung One', 1800, 1600)
addison = TutorCard('Addison, from operator import add', 2200, 1100)
amy_m = TutorCard('Amy M', 1000, 2000)
jemmy = TutorCard('Joking Jem', 2000, 1400)
kevin_y = TutorCard('Kevin, Minion of Oski', 2400, 1000)
ailyn = TutorCard('Ailyn, pronounced Eye-Lean', 1700, 1700)
sam = TutorCard('Sam, The Exception-al Man', 1100, 2200)
nikhita = TutorCard('Nikhita the Fastest Cheetah', 1700, 1700)
shide = TutorCard('edihs', 1500, 1900)
jack = TutorCard('Jack, The Coil King', 2100, 1200)
evan_c = TutorCard("Evan's Curse of Infinite Recursion", 1700, 1700)
risham = TutorCard('Rish, the squisy fish', 2400, 1000)
uma = TutorCard('Uma, Empress of Eigenvalues', 2000, 1100)
star = TutorCard('Star, Operator of Yin and Yang', 1500, 1700)
shayna = TutorCard('Jedi Master Shayna', 1200, 2200)
boren = TutorCard('Boren, Brewer of Bucha', 1500, 1800)
frank = TutorCard('Frank the Tank', 1500, 1700)
richard = TutorCard("Richard 'Chardizard' Roggenkemper", 1600, 1700)
aini = TutorCard('Aini the Macaroni Attackaroni', 1600, 1800)
jade = TutorCard('Jade, Singher of Songs', 1600, 1700)
jusin = TutorCard('Justin Time', 1200, 2200)
rebecca = TutorCard('Rebz', 1500, 1700)
ajan = TutorCard('Ragin Ajan', 2000, 1400)
chris_z = TutorCard('Christopher the Redeemer', 1500, 1700)


# Professors
garcia = ProfessorCard('Dan Garcia, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [kavi, danelle, dalton, tiffany, gibbes, keon, derrick, griffin, kevin_w, michelle, 
				  anita, lindsay, derek, tim, lillian, cesar, cameron, audrey, nancy, albert, jacob, chris_a, 
				  shea, alex, caroline, amy_h, kate, rachel, carl, evan_l, abhinav, jacqueline, addison, amy_m, 
				  jemmy, kevin_y, ailyn, sam, nikhita, shide, jack, evan_c, risham, uma, star, shayna, boren, frank, 
				  richard, aini, jade, jusin, rebecca, ajan, chris_z, garcia]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()