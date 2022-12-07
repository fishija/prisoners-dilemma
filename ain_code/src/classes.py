import queue
import random
from src.funcitons import to_binary


class Game:
    """
    _summary_

    Attributes:
        prehistory (list): Like [[0,1,0], [1,0,0], [1,1,1], [0,0,1]]. Which means prehistory_l = 4, players = 3.
    """
    player_count = 0
    prehistory = []

    def update_prehistory(self, last_play: list):
        """
        Update prehistory with last play of all players.

        Args:
            last_play (list): Like [0,1,1].
        """
        self.prehistory.pop()
        self.prehistory.insert(0, last_play)

    # def prehistory_to_decimal(self):
    #     """
    #     1. Whole prehistory to 
    #     """
    #     whole_binary = ''

    #     for i in self.prehistory:
    #         for j in i:
    #             whole_binary += str(j)

    #     return int(whole_binary, 2)

    def prep_prehistory_for_individual(self, individual_id: int):
        """
        Return changed prehistory per individual like [[ind_choice, how_many_inds_cooperated], ...]
        """
        to_ret = []

        for i in self.prehistory:
            ind_choice = i[individual_id]

            coop_individuals = 0
            for j in i:
                if not i == ind_choice and j == 1:
                    coop_individuals += 1

            to_ret.append([ind_choice, coop_individuals])

        return to_ret


class Generation:
    pass


class Individual:
    """
    _summary_

    Attributes:
        id (int): Binary individual as decimal number.
        score (int): AVG of total payoff function.
        tournament_history (str): History from individuals perspective.
    """
    id = 0
    score = 0
    my_choice = None
 
    def __init__(self, prob_of_init_c: float, N: int, L: int):
        len = 2**(N*L)

        for i in range(len):
            if (random.random() <= prob_of_init_c):
                id += 2**i

    def choice(self, coop_players_count: list) -> int:
        """
        Attributes:
            coop_players_count (list): History/Prehistory for current individual. Like [[1,3], [1,0], [0,5]] which means - prehistory_l = 3, [[a,b],[a,b]] a = individuals choice, b = how many other individuals cooperated :)
        """
        # temp = to_binary(coop_players_count[-1][0]) + to_binary(coop_players_count[-1][0])
        # temp = self.my_choice and coop_players_count -> binary

        # dec_hist = whole self.coop_players_count to decimal
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

    def mutation (self, id: int, mutation_prob: float):
        self.id=id
        for current_id_bit in self.id:
            if random.random() <= mutation_prob:
                #change current id bit to opposite
                pass
            pass
