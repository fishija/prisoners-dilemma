import random
from src.funcitons import to_binary, to_binary_length


class Game:
    """
    _summary_
    """
    is_2_PD = False
    N = 0
    two_pd_payoff_func = dict()
    prob_of_init_C = 0
    num_of_tournaments = 0
    num_of_opponents = 0
    prehistory_L = 0
    pop_size = 0
    num_of_gener = 0
    tournament_size = 0
    crossover_prob = 0
    mutation_prob = 0
    seed = None
    debug = False

    def __init__(self, is_2_PD, N, two_pd_payoff_func, prob_of_init_C, num_of_tournaments, num_of_opponents, prehistory_L, pop_size, num_of_gener, tournament_size, crossover_prob, mutation_prob, seed, debug):
        pass

    def play(self):
        # create generations in loop

        # create chart -- either at the end or in create generations loop
        pass


class Generation:
    """
    _summary_

    Attributes:
        history_count (list): Count for every history that occured in 
    """
    pop_size = 0
    tournament_size = 0
    crossover_prob = 0

    history_count = []

    def __init__(self, pop_size, tournament_size, crossover_prob):
        pass

    # create individuals

    # random individuals to PdTournament


class PdTournament:
    """
    Attributes:
        history (list): Like [[0,1,0], [1,0,0], [1,1,1], [0,0,1]]. Which means prehistory_L = 4, players = 3.
    """
    history = []

    def update_history(self, last_play: list):
        """
        Update history with last play of all players.

        Args:
            last_play (list): Like [0,1,1].
        """
        self.history.pop()
        self.history.insert(0, last_play)

    def prep_history_for_individual(self, individual_id: int):
        """
        Return changed history per individual like [[ind_choice, how_many_inds_cooperated], ...]
        """
        to_ret = []

        for i in self.history:
            ind_choice = i[individual_id]

            coop_individuals = 0
            for j in i:
                if not i == ind_choice and j == 1:
                    coop_individuals += 1

            to_ret.append([ind_choice, coop_individuals])

        return to_ret

    def fight(self, ind_1, ind_2):
        pass


class Individual:
    """
    _summary_

    Attributes:
        id (int): Binary individual as decimal number.
        score (int): Total score per individual.
    """
    id = 0
    score = 0
    my_choice = None
 
    def __init__(self, prob_of_init_c: float, N: int, L: int):
        ind_len = '1'
        ind_len += to_binary(N-1)
        ind_len *= L
        ind_len = int(ind_len, 2)

        for i in range(ind_len):
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

    # def prehistory_to_decimal(self):
    #     """
    #     1. Whole prehistory to 
    #     """
    #     whole_binary = ''
    #     for i in self.prehistory:
    #         for j in i:
    #             whole_binary += str(j)

    #     return int(whole_binary, 2)

    def count_score(self, coop_players_count, two_p_payoff_func = None):
        # if 2pPD
        if two_p_payoff_func:
            if self.my_choice == 0 and coop_players_count == 0:
                self.score += two_p_payoff_func['dd_uno']
                pass
            elif self.my_choice == 0 and coop_players_count == 1:
                self.score += two_p_payoff_func['dc_uno']
                pass
            elif self.my_choice == 1 and coop_players_count == 0:
                self.score += two_p_payoff_func['cd_uno']
                pass
            elif self.my_choice == 1 and coop_players_count == 1:
                self.score += two_p_payoff_func['cc_uno']
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
