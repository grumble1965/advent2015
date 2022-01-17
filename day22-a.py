import sys
import copy
from collections import deque


class Game:
    _spells = {'Magic Missile': {'mana': 53},
               'Drain': {'mana': 73},
               'Shield': {'mana': 113, 'turns': 5},
               'Poison': {'mana': 173, 'turns': 6},
               'Recharge': {'mana': 229, 'turns': 5}}

    def __init__(self, player_hp, player_mana, boss_hp, boss_damage, debug=False):
        self._debug = debug
        self._player_hp = player_hp
        self._player_mana = player_mana
        self._player_armor = 0
        self._boss_hp = boss_hp
        self._boss_damage = boss_damage
        self._timers = {}
        for spell in self._spells:
            self._timers[spell] = 0
        self._turn = 0
        self._winner = None
        self.spent_mana = 0
        self.history = []

    def game_over(self):
        return self._turn < 0 or self._turn > 1

    def winner(self):
        return self._winner

    def can_cast(self):
        can_afford = [spell for spell, spell_dict in self._spells.items() if self._player_mana >= spell_dict['mana']]
        return [spell for spell in can_afford if self._timers[spell] == 0]

    def whose_turn(self):
        tt = None
        if self._turn == 0:
            tt = 'Player'
        elif self._turn ==1:
            tt = 'Boss'
        return tt

    def _print_state(self):
        if self._debug:
            print(f"- Player has {self._player_hp} hit points, {self._player_armor} armor, {self._player_mana} mana")
            print(f"- Boss has {self._boss_hp} hit points")

    def _handle_effects(self):
        effects = [spell for spell, timer in self._timers.items() if timer > 0]
        for spell in effects:
            self._timers[spell] -= 1
            if spell == 'Shield':
                if self._debug:
                    print(f"{spell}'s timer is now {self._timers[spell]}")
            elif spell == 'Poison':
                self._boss_hp -= 3
                if self._debug:
                    print(f"{spell} deals 3 damage; its timer is now {self._timers[spell]}")
            elif spell == 'Recharge':
                self._player_mana += 101
                if self._debug:
                    print(f"{spell} provides 101 mana; its timer is now {self._timers[spell]}")
            else:
                if self._debug:
                    print(f"Unknown spell {spell}")

            if self._timers[spell] == 0:
                if self._debug:
                    print(f"{spell} wears off.")
                if spell == 'Shield':
                    self._player_armor -= 7

    def _handle_death(self):
        if self._player_hp < 1:
            self._turn = -1
            self._winner = 'Boss'
            if self._debug:
                print(f"The player is dead")
        elif self._boss_hp < 1:
            self._turn = -1
            self._winner = 'Player'
            if self._debug:
                print(f"The Boss is dead")

    def _handle_mana(self):
        if self._player_mana < self._spells['Magic Missile']['mana']:
            self._turn = -1
            self._winner = 'Boss'
            if self._debug:
                print(f"Insufficient player mana")

    def player_turn(self, spell):
        if self.whose_turn() != 'Player':
            print("Not the player's turn!")
            return
        if self._debug:
            print('-- Player turn --')
        self._print_state()
        self._handle_effects()
        self._handle_death()
        self._handle_mana()
        if self._turn != 0:
            if self._debug:
                print("Game over.")
            return

        if spell not in self._spells:
            print(f"Unknown spell {spell}")
            return

        mana = self._spells[spell]['mana']
        if self._player_mana < mana:
            print(f"Not enough mana ({self._player_mana}) to cast {spell} ({mana})")
            return
        elif self._timers[spell] > 0:
            print(f"{spell} is still in effect!")
            return
        elif spell == 'Magic Missile':
            self._player_mana -= mana
            self.spent_mana += mana
            self._boss_hp -= 4
            self.history.append(spell)
            if self._debug:
                print(f"Player casts {spell}, dealing 4 damage.")
        elif spell == 'Drain':
            self._player_mana -= mana
            self.spent_mana += mana
            self._player_hp += 2
            self._boss_hp -= 2
            self.history.append(spell)
            if self._debug:
                print(f"Player casts {spell}, dealing 2 damage, and healing 2 hit points.")
        elif spell == 'Shield':
            self._player_mana -= mana
            self.spent_mana += mana
            self._player_armor += 7
            self._timers[spell] = 6
            self.history.append(spell)
            if self._debug:
                print(f"Player casts {spell}, increasing armor by 7.")
        elif spell == 'Poison':
            self._player_mana -= mana
            self.spent_mana += mana
            self._timers[spell] = 6
            self.history.append(spell)
            if self._debug:
                print(f"Player casts {spell}.")
        elif spell == 'Recharge':
            self._player_mana -= mana
            self.spent_mana += mana
            self._timers[spell] = 5
            self.history.append(spell)
            if self._debug:
                print(f"Player casts {spell}.")
        else:
            print(f"Error when casting {spell}")

        self._turn = 1
        self._handle_death()
        if self._debug:
            print()

    def boss_turn(self):
        if self.whose_turn() != 'Boss':
            print("Not the Boss's turn!")
            return

        if self._debug:
            print('-- Boss turn --')
        self._print_state()
        self._handle_effects()
        self._handle_death()
        if self._turn != 1:
            if self._debug:
                print("Game over.")
            return

        attack = max(self._boss_damage - self._player_armor, 1)
        self._player_hp -= attack
        if self._debug:
            print(f"Boss attacks for {self._boss_damage} - {self._player_armor} = {attack} damage.")

        self._turn = 0
        self._handle_death()
        if self._debug:
            print()


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    boss_hp, boss_damage = None, None
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")
            words = tmp.split(':')
            if words[0] == 'Hit Points':
                boss_hp = int(words[1])
            elif words[0] == 'Damage':
                boss_damage = int(words[1])
            else:
                print(f"Couldn't parse {words}")

    game = Game(50, 500, boss_hp, boss_damage)
    q = deque()
    q.append(game)

    lowest_mana, lowest_history = None, None
    win_ctr, loss_ctr = 0, 0
    q_ctr = 0
    while q:
        g = q.pop()
        if q_ctr % 100 == 0:
            print(f"After {q_ctr} queue steps, queue has length {len(q)}, {win_ctr} wins, {loss_ctr} losses")
        q_ctr += 1

        if g.winner() is not None or g.game_over():
            print("WTF^2")
            break

        if g.whose_turn() == 'Boss':
            g.boss_turn()

            if g.winner() is None:
                q.append(g)
            elif g.winner() == 'Player':
                win_ctr += 1
                if lowest_mana is None or g.spent_mana < lowest_mana:
                    lowest_mana = g.spent_mana
                    lowest_history = g.history
            elif g.winner() == 'Boss':
                loss_ctr += 1
            else:
                print("WTF?")
        elif g.whose_turn() == 'Player':
            spells = g.can_cast()
            if not spells:
                loss_ctr += 1
            else:
                for spell in g.can_cast():
                    g_prime = copy.deepcopy(g)
                    g_prime.player_turn(spell)

                    if g_prime.winner() is None:
                        q.append(g_prime)
                    elif g_prime.winner() == 'Player':
                        win_ctr += 1
                        if lowest_mana is None or g_prime.spent_mana < lowest_mana:
                            lowest_mana = g_prime.spent_mana
                            lowest_history = g_prime.history
                    elif g_prime.winner() == 'Boss':
                        loss_ctr += 1
                    else:
                        print("WTF?")

    print(f"Total of {win_ctr+loss_ctr} games, {win_ctr} wins, {loss_ctr} losses")
    print(f"Least mana spent in a winning game: {lowest_mana}, {lowest_history}")

    #
    # # attacks = ['Poison', 'Magic Missile']
    # attacks = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']
    # while game.winner() is None:
    #     print(f"Player can cast {game.can_cast()}")
    #     att = attacks.pop(0)
    #     game.player_turn(att)
    #     game.boss_turn()
    # print(f"The {game.winner()} wins spending {game.spent_mana} mana.")


if __name__ == '__main__':
    main()
