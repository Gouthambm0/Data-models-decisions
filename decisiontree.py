import math 

# decision tree for Bob's summer job dilemma
# he has an offer from Bob (12k)
# Vanessa might offer him 14k (60% chance)
# recruitment cycle gives expected 11.58k (40% chance)
# he's deciding whether to accept Bob's offer or wait it out

emvbob = 12000
emvVanessa = 14000
emvrecruitment = 11580

# expected value of rejecting Bob's offer
emvB = (emvVanessa * 0.6 + emvrecruitment * 0.4)

def DecisionA(emvbob, emvB):
    """ decide if Bob's offer is worth rejecting """
    if emvB > emvbob:
        print("Reject Bob's Offer")

def EventA(emvVanessa, emvrecruitment):
    """ figure out what happens if Bob's rejected """
    z = max(emvVanessa, emvrecruitment)
    return z 

def Final(z, emvVanessa):
    """ outcome after rejecting Bob """
    if z == emvVanessa:
        print("Accept Vanessa's job offer")
    else:
        print("Go for recruitment")

def main():
    if emvB > emvbob:
        print("Reject Bob's offer")
        z = EventA(emvVanessa, emvrecruitment)
        Final(z, emvVanessa)
    else:
        print("Accept Bob's offer")

if __name__ == '__main__':
    main()