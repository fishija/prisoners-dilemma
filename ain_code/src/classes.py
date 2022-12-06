import queue
from src.funcitons import to_binary


class Individual:
    """
    _summary_

    Attributes:
        id (int): Binary individual as decimal number.
        score (int): AVG of total payoff function.
        prehistory (int): Binary prehistory as decimal number. Do not change!
        tournament_history (str): History from individuals perspective.
    """
    id = 0
    score = 0
    prehistory = 0
    my_choice = None
    tournament_history = []
 
    def __init__(self, id: int, prehistory: int):
        self.id = id
        self.prehistory = prehistory
        self.tournament_history = to_binary(prehistory)

    def choice(self, coop_players_count: int) -> int:
        temp = to_binary(self.my_choice) + to_binary(coop_players_count)
        # temp = self.my_choice and coop_players_count -> binary

        # self.tournament_history.drop(0)
        # self.tournament_history.append(temp)

        # dec_hist = whole self.tournament_history to decimal
        # binary_id_list = id to binary (ex. list of 0 and 1)
        # self.my_choice = binary_id_list(dec_hist)
        # return self.my_choice
        pass

    def count_score(self, coop_players_count, two_p_payoff_func = None):
        # if 2pPD
        if two_p_payoff_func:
            if self.my_choice == 0 and coop_players_count == 0:
                # score += two_p_payoff_func[dd]
                pass
            elif self.my_choice == 0 and coop_players_count == 1:
                # score += two_p_payoff_func[dc]
                pass
            elif self.my_choice == 1 and coop_players_count == 0:
                # score += two_p_payoff_func[cd]
                pass
            elif self.my_choice == 1 and coop_players_count == 1:
                # score += two_p_payoff_func[cc]
                pass

        else:
            if self.my_choice == 0:
                self.score += 2 * coop_players_count

            elif self.my_choice == 1:
                self.score += (2 * coop_players_count) + 1

    def mutation (self, id: int):
        self.id=id
        for current_id_bit in self.id:
            if random.random()<=mutation_prob:
                #change current id bit to opposite
                pass
            pass
