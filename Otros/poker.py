import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANKS.index(rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(r, s) for s in SUITS for r in RANKS]
        random.shuffle(self.cards)

    def deal(self, num):
        return [self.cards.pop() for _ in range(num)]

class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.hand = []
        self.chips = chips
        self.in_game = True
        self.current_bet = 0
        self.is_dealer = False

    def __str__(self):
        return f"{self.name} ({'Activo' if self.in_game else 'Retirado'}) - Fichas: {self.chips}"

class PokerGame:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.dealer_index = 0
        self.pot = 0
        self.deck = None
        self.community_cards = []

    def rotate_dealer(self):
        self.dealer_index = (self.dealer_index + 1) % len(self.players)
        for i, p in enumerate(self.players):
            p.is_dealer = (i == self.dealer_index)

    def post_blinds(self):
        sb_index = (self.dealer_index + 1) % len(self.players)
        bb_index = (self.dealer_index + 2) % len(self.players)

        small_blind = 10
        big_blind = 20

        self.players[sb_index].chips -= small_blind
        self.players[sb_index].current_bet = small_blind
        self.players[bb_index].chips -= big_blind
        self.players[bb_index].current_bet = big_blind

        self.pot += small_blind + big_blind

        print(f"{self.players[sb_index].name} pone la ciega pequeña: {small_blind}")
        print(f"{self.players[bb_index].name} pone la ciega grande: {big_blind}")

    def deal_hole_cards(self):
        self.deck = Deck()
        for player in self.players:
            player.hand = self.deck.deal(2)
        self.community_cards = []

    def reveal_community_cards(self, stage):
        if stage == "flop":
            self.community_cards += self.deck.deal(3)
        elif stage == "turn":
            self.community_cards += self.deck.deal(1)
        elif stage == "river":
            self.community_cards += self.deck.deal(1)
        print(f"\nCartas del dealer ({stage.capitalize()}): {[str(c) for c in self.community_cards]}")

    def betting_round(self):
        print("\n--- Ronda de Apuestas ---")
        for player in self.players:
            if player.in_game:
                print(f"{player.name}, tus cartas: {[str(c) for c in player.hand]}")
                action = input(f"{player.name}, ¿(c)igualar, (s)ubir, (r)etirarte?: ").lower()
                if action == 'r':
                    player.in_game = False
                    print(f"{player.name} se retira.")
                elif action == 's':
                    amount = int(input("¿Cuánto quieres subir?: "))
                    player.chips -= amount
                    player.current_bet += amount
                    self.pot += amount
                elif action == 'c':
                    to_call = max(p.current_bet for p in self.players) - player.current_bet
                    player.chips -= to_call
                    player.current_bet += to_call
                    self.pot += to_call

    def showdown(self):
        print("\n--- Showdown ---")
        print(f"Cartas comunitarias: {[str(c) for c in self.community_cards]}")
        active_players = [p for p in self.players if p.in_game]
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"{winner.name} gana el bote porque los demás se retiraron.")
        else:
            for p in active_players:
                print(f"{p.name} tiene {[str(c) for c in p.hand]}")
            # Lógica de evaluación real no implementada aún.
            winner = active_players[0]
            print(f"{winner.name} gana el bote.")
        winner.chips += self.pot

    def reset_bets(self):
        for p in self.players:
            p.current_bet = 0
        self.pot = 0

    def play_hand(self):
        print("\n=== Nueva Mano ===")
        self.rotate_dealer()
        self.post_blinds()
        self.deal_hole_cards()

        self.betting_round()

        self.reveal_community_cards("flop")
        self.betting_round()

        self.reveal_community_cards("turn")
        self.betting_round()

        self.reveal_community_cards("river")
        self.betting_round()

        self.showdown()
        self.reset_bets()

    def play_game(self):
        while all(p.chips > 0 for p in self.players):
            self.play_hand()
            input("Presiona Enter para la siguiente mano...")

if __name__ == "__main__":
    nombres = input("Nombres de jugadores separados por coma: ").split(",")
    juego = PokerGame([n.strip() for n in nombres])
    juego.play_game()
