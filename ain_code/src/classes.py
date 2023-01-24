import random
import copy
import pandas as pd
from src.funcitons import to_binary, to_binary_length, save_plot_in_results, create_results_dir, \
                        print_11, print_12, print_13, print_14, print_21, print_22, print_23, print_31

from PyQt5.QtCore import pyqtSignal, QObject



global_num_of_C_N = []
chosen_randoms = []
cross_bits = []
mutation_bits = []
debug = False




class Individual:
    """
    _summary_

    Attributes:
        id (int): Binary individual as decimal number.
        score (int): Total score per individual.
    """
    id = 0
    ind_len = 0
    score = 0
    N = 0
    oponentes_jodidos = 0
    my_choice = None
 
    def __init__(self, prob_of_init_c: float = None, N: int = None, L: int = None, overwrite = None, binary_id: str = None):
        if binary_id:
            self.ind_len = len(binary_id)
            self.N = N
            self.id = int(binary_id, 2)

        elif not overwrite:
            self.ind_len = '1'
            self.ind_len += to_binary(N-1)
            self.ind_len *= L
            self.ind_len = int(self.ind_len, 2) + 1
            self.N = N

            for i in range(self.ind_len):
                x = random.random()
                if (x <= prob_of_init_c):
                    self.id += 2**i
        else:
            self.id = overwrite.id
            self.ind_len = overwrite.ind_len
            self.score = overwrite.score
            self.N = overwrite.N
            self.my_choice = overwrite.my_choice
            self.oponentes_jodidos = overwrite.oponentes_jodidos

    def __gt__(self, other):
        if self.score > other.score:
            return True
        return False

    def __lt__(self, other):
        if self.score < other.score:
            return True
        return False

    def to_binary_for_this_old_fuck(self):
        return to_binary_length(self.id, self.ind_len)

    def choose(self, coop_players_count: list) -> int:
        """
        Attributes:
            coop_players_count (list): History/Prehistory for current individual. Like [[1,3], [1,0], [0,5]] which means - prehistory_l = 3, [[a,b],[a,b]] a = individuals choice, b = how many other individuals cooperated :)
        """
        # [[1,3], [1,0]] -> [[1,011], [1,000]] -> 10111000 -> 184
        # [[1,1], [1,1], [1,1]] -> 111111
        # 0 1 1 0 0 0 = 24

        decimal_history = ''

        for i in coop_players_count:
            i[1] = to_binary_length(i[1], len(to_binary(self.N-1)))
            decimal_history += ('{a}{b}').format(a = str(i[0]), b = i[1])

        decimal_history = int(decimal_history, 2)

        binary_id = to_binary_length(self.id, self.ind_len)

        self.my_choice = int(binary_id[decimal_history])

        # print(decimal_history, binary_id, self.my_choice)

        return decimal_history

    def return_decimal_history(self, coop_players_count: list) -> int:
        decimal_history = ''

        for i in coop_players_count:
            i[1] = to_binary_length(i[1], len(to_binary(self.N-1)))
            decimal_history += ('{a}{b}').format(a = str(i[0]), b = i[1])

        decimal_history = int(decimal_history, 2)

        return decimal_history

    def count_score(self, coop_players_count, two_pd_payoff_func = None):
        # if 2pPD
        if two_pd_payoff_func:
            if self.my_choice == 0 and coop_players_count[0][1] == 0:
                self.score += two_pd_payoff_func['dd_uno']

            elif self.my_choice == 0 and coop_players_count[0][1] == 1:
                self.score += two_pd_payoff_func['dc_uno']

            elif self.my_choice == 1 and coop_players_count[0][1] == 0:
                self.score += two_pd_payoff_func['cd_uno']

            elif self.my_choice == 1 and coop_players_count[0][1] == 1:
                self.score += two_pd_payoff_func['cc_uno']

        else:
            if self.my_choice == 0:
                self.score += 2 * coop_players_count[0][1] + 1
                global_num_of_C_N[-1][0] += coop_players_count[0][1]
                global_num_of_C_N[-1][1] += 1

            elif self.my_choice == 1:
                self.score += (2 * coop_players_count[0][1])
                global_num_of_C_N[-1][0] += coop_players_count[0][1] + 1
                global_num_of_C_N[-1][1] += 1

    def mutation (self, mutation_prob: float):
        print_temp = []
        temp_binary_id = ''
        for index, current_id_bit in enumerate(to_binary_length(self.id, self.ind_len)):
            x = random.random()
            chosen_randoms.append(x)
            if x <= mutation_prob:
                mutation_bits.append(index)
                print_temp.append(len(temp_binary_id)+1)
                #change current ids bit to opposite
                if current_id_bit == '1':
                    current_id_bit = '0'
                else:
                    current_id_bit = '1'

            temp_binary_id += current_id_bit
        

        # if print_temp:     
        #     print('B4 mutation: ind = {}, mutate_at = {}'.format(to_binary_length(self.id, self.ind_len), print_temp))
        #     print('After mutation: ind = {}'.format(to_binary_length(self.id, self.ind_len)))


        self.id = int(temp_binary_id, 2)


class PdTournament:
    """
    Attributes:
        history (list): Like [[0,1,0], [1,0,0], [1,1,1], [0,0,1]]. Which means prehistory_L = 4, players = 3.
    """
    N = 0
    L = 0
    num_of_tournaments = 0
    two_pd_payoff_func = None

    list_of_ind = []
    inds = []
    history = []
    history_count = []
    input_prehistory = ''

    def __init__(self, list_of_ind, N, L, num_of_tournaments, two_pd_payoff_func: dict = None, input_prehistory: str = None, a: bool = None):
        self.list_of_ind = list_of_ind
        self.N = N
        self.L = L
        self.a = True
        self.num_of_tournaments = num_of_tournaments
        self.two_pd_payoff_func = two_pd_payoff_func

        self.history_count = [0] * list_of_ind[0].ind_len
        self.input_prehistory = input_prehistory

    def update_history(self, last_play: list = None, a: bool = None):
        """
        Update history with last play of all players.

        Args:
            last_play (list): Like [0,1,1].
        """
        if last_play:
            self.history.pop()
            self.history.insert(0, last_play)
            
        elif self.input_prehistory and not a:
            self.history = [self.input_prehistory[i:i+self.N] for i in range(0,len(self.input_prehistory), self.N)]
            for index, chunk in enumerate(self.history):
                temp = []
                for c in chunk:
                    temp.append(int(c))
                self.history[index] = temp

        else:
            # self.history = [[0,1],[1,0],[0,0]]
            self.history.clear()
            for _ in range(self.L):
                temp = []
                for n in range(self.N):
                    x = random.random()
                    chosen_randoms.append(x)
                    if x < 0.5:
                        temp.append(0)
                    else:
                        temp.append(1)

                self.history.append(temp)

        # print('History = {}'.format(self.history))

    def prep_history_for_individual(self, individual_id: int):
        """
        Return changed history per individual like [[ind_choice, how_many_inds_cooperated], ...]
        """
        to_ret = []

        for i in self.history:
            ind_choice = i[individual_id]

            coop_individuals = 0
            for j in i:
                if j == 1:
                    coop_individuals += 1

            if ind_choice == 1:
                coop_individuals -= 1

            to_ret.append([ind_choice, coop_individuals])

        return to_ret

    def start_whole_tournament(self, num_of_opponents):
        self.c_opponents = []
        self.sum_with_opponents = [0]*len(self.list_of_ind)
        if self.input_prehistory:
            self.update_history()

        for ind in self.list_of_ind:
            ind.score = 0
            ind.oponentes_jodidos = 0

        while not self.c_opponents or not min(self.c_opponents) == num_of_opponents:
            if not self.c_opponents:
                currently_used_inds = [self.list_of_ind[0]]
                for i in range(1, self.N):
                    currently_used_inds.append(self.list_of_ind[i])
            else:
                temp_index = self.c_opponents.index(min(self.c_opponents))
                currently_used_inds = [self.list_of_ind[temp_index]]
                for random_selected_ind in random.sample(list(self.list_of_ind[:temp_index] + self.list_of_ind[(temp_index+1):]), k=(self.N-1)):
                    currently_used_inds.append(random_selected_ind)

            if self.N == 2 and debug and self.input_prehistory:
                    pass
            elif debug and self.input_prehistory:
                N_players_strat_id = []
                for cur in currently_used_inds:
                    N_players_strat_id.append(self.list_of_ind.index(cur))

                temp_list_of_ind = []
                for ind in currently_used_inds:
                    temp_list_of_ind.append(ind.to_binary_for_this_old_fuck())

                print_22(None, num_of_opponents - ind.oponentes_jodidos, temp_list_of_ind, N_players_strat_id, self.history_count)
            
            for cur_ind in currently_used_inds:
                cur_ind.oponentes_jodidos += 1

            self.c_opponents.clear()
            for ind in self.list_of_ind:
                self.c_opponents.append(ind.oponentes_jodidos)

            if debug and self.N==2 and len(self.list_of_ind)==3:
                    print_12(currently_used_inds[0].to_binary_for_this_old_fuck(), currently_used_inds[1].to_binary_for_this_old_fuck(), currently_used_inds[0].return_decimal_history(self.prep_history_for_individual(0)), currently_used_inds[1].return_decimal_history(self.prep_history_for_individual(1)))
                    print_13(self.c_opponents, self.history_count, currently_used_inds[0].return_decimal_history(self.prep_history_for_individual(0)), currently_used_inds[1].return_decimal_history(self.prep_history_for_individual(1)))

            self.run_one_tournament(currently_used_inds)

            if not min(self.c_opponents) == num_of_opponents:
                self.update_history(a=True)
                
 
    def run_one_tournament(self, currently_used_inds):
        if not self.input_prehistory:
            self.update_history()

        for k in range(self.num_of_tournaments):
            last_play = []

            for index, cur_ind in enumerate(currently_used_inds):
                self.history_count[cur_ind.choose(self.prep_history_for_individual(index))] += 1
                last_play.append(int(cur_ind.my_choice))

            if self.a and self.N == 2 and debug and self.input_prehistory and len(self.list_of_ind) == 2: # for exper 1
                print_12(currently_used_inds[0].to_binary_for_this_old_fuck(), currently_used_inds[1].to_binary_for_this_old_fuck(), currently_used_inds[0].return_decimal_history(self.prep_history_for_individual(0)), currently_used_inds[1].return_decimal_history(self.prep_history_for_individual(1)))

            self.update_history(last_play)

            if self.a and self.N == 2 and debug and self.input_prehistory and len(self.list_of_ind) == 2: # for exper 1
                print_13(self.c_opponents, self.history_count)

            self.a = False

            print_temp = []

            for index, cur_ind in enumerate(currently_used_inds):
                if self.N > 2:
                    cur_ind.count_score(self.prep_history_for_individual(index))
                else:
                    cur_ind.count_score(self.prep_history_for_individual(index), self.two_pd_payoff_func)

                print_temp.append(cur_ind.score)

            # print("Scores = {}".format(print_temp))
            if self.N==2 and debug and len(self.list_of_ind)<10:
                temp_score_uno = 0
                temp_score_dos = 0

                if last_play[0] == 0 and last_play[1] == 0:
                    temp_score_uno += self.two_pd_payoff_func['dd_uno']
                    temp_score_dos += self.two_pd_payoff_func['dd_uno']

                elif last_play[0] == 0 and last_play[1] == 1:
                    temp_score_uno += self.two_pd_payoff_func['dc_uno']
                    temp_score_dos += self.two_pd_payoff_func['cd_uno']

                elif last_play[0] == 1 and last_play[1] == 0:
                    temp_score_uno += self.two_pd_payoff_func['cd_uno']
                    temp_score_dos += self.two_pd_payoff_func['dc_uno']

                elif last_play[0] == 1 and last_play[1] == 1:
                    temp_score_uno += self.two_pd_payoff_func['cc_uno']
                    temp_score_dos += self.two_pd_payoff_func['cc_uno']

                self.sum_with_opponents[self.list_of_ind.index(currently_used_inds[0])] += temp_score_uno
                self.sum_with_opponents[self.list_of_ind.index(currently_used_inds[1])] += temp_score_dos

                print_14(k+1, last_play[0], last_play[1], temp_score_uno, temp_score_dos, self.sum_with_opponents, self.history, self.prep_history_for_individual(0), self.prep_history_for_individual(1), currently_used_inds[0].return_decimal_history(self.prep_history_for_individual(0)), currently_used_inds[1].return_decimal_history(self.prep_history_for_individual(1)), self.history_count)
                
            elif debug and self.N != 2:
                temp_scores = []
                temp_sum_scores = []
                temp_N_players_strat_id = []

                for i in range(0, self.N-1):
                    temp_sum_scores.append(currently_used_inds[i].score)
                    temp_history = self.prep_history_for_individual(i)
                    temp_N_players_strat_id.append(self.list_of_ind.index(currently_used_inds[i]))

                    if temp_history[0][0] == 0:
                        temp_scores.append(2 * temp_history[0][1] + 1)
                    else:
                        temp_scores.append(2 * temp_history[0][1])

                print_23(k, last_play, last_play.count(1), temp_scores, temp_sum_scores, self.history, last_play, temp_N_players_strat_id, self.history_count)

        

class Generation:
    """
    _summary_

    Attributes:
        history_count (list): Count for every history that occured in 
    """
    pop_size = 0
    num_of_tournaments = 0
    tournament_size = 0
    crossover_prob = 0
    mutation_prob = 0
    N = 0
    L = 0

    temp_tournament = None

    two_pd_payoff_func = None

    best_individual = None

    list_of_ind = []
    history_count = []

    def __init__(self, pop_size, num_of_tournaments, tournament_size, crossover_prob, prob_of_init_C, N, L, mutation_prob, two_pd_payoff_func: dict = None, list_of_ind: list = None, input_strategies: list = None, input_prehistory: str = None):
        self.pop_size = pop_size
        self.num_of_tournaments = num_of_tournaments
        self.tournament_size = tournament_size
        self.crossover_prob = crossover_prob
        self.two_pd_payoff_func = two_pd_payoff_func
        self.mutation_prob = mutation_prob
        self.N = N
        self.L = L
        self.list_of_ind = []
        self.input_prehistory = input_prehistory

        if list_of_ind:
            self.list_of_ind = list_of_ind

        elif not list_of_ind and not input_strategies:            
            for _ in range(pop_size):
                self.list_of_ind.append(Individual(prob_of_init_C, N, L))

        else:
            for strat in input_strategies:
                self.list_of_ind.append(Individual(N=N, binary_id=strat))

        self.history_count = [0] * self.list_of_ind[0].ind_len

    def fight_for_death_u_knobs(self, num_of_opponents, a = None):
        if self.two_pd_payoff_func:
            self.temp_tournament = PdTournament(self.list_of_ind, self.N, self.L, self.num_of_tournaments, self.two_pd_payoff_func, self.input_prehistory, a)
        else:
            self.temp_tournament = PdTournament(self.list_of_ind, self.N, self.L, self.num_of_tournaments, self.input_prehistory, a)

        self.temp_tournament.start_whole_tournament(num_of_opponents)

        self.history_count = [sum(x) for x in zip(self.temp_tournament.history_count, self.history_count)]

    def hard_tournament(self):
        best_ind_list = []

        for i in range(self.pop_size):
            random_chosen_individuals = []
            original_list_index = []

            for j in range(self.tournament_size):
                int_of_ind_to_choose = random.randint(0, self.pop_size - 1)

                if random_chosen_individuals:
                    while int_of_ind_to_choose in original_list_index:
                        int_of_ind_to_choose = random.randint(0, self.pop_size - 1)

                random_chosen_individuals.append(Individual(overwrite = self.list_of_ind[int_of_ind_to_choose]))
                original_list_index.append(int_of_ind_to_choose)

            best_ind_list.append(sorted(random_chosen_individuals, key=lambda x: x.score, reverse=True)[0])
      
        self.list_of_ind = best_ind_list

    def cross_two_inds(self, ind_uno: Individual, ind_dos: Individual):
        temp_ind_uno = copy.deepcopy(ind_uno)
        temp_ind_dos = copy.deepcopy(ind_dos)

        ind_len = temp_ind_uno.ind_len

        temp_ind_uno_bits = to_binary_length(temp_ind_uno.id, ind_len)
        temp_ind_dos_bits = to_binary_length(temp_ind_dos.id, ind_len)

        chosen_num = random.randint(1, ind_len-1)
        chosen_randoms.append(chosen_num)
        cross_bits.append(chosen_num)

        # print("Before cross (chosen_num = {})[\nind_uno = {},\nind_dos = {}\n]".format(chosen_num, to_binary_length(temp_ind_uno.id, temp_ind_uno.ind_len), to_binary_length(temp_ind_dos.id, temp_ind_uno.ind_len)))

        temp_ind_uno.id = int(temp_ind_uno_bits[:chosen_num] + temp_ind_dos_bits[chosen_num:], 2)
        temp_ind_dos.id = int(temp_ind_dos_bits[:chosen_num] + temp_ind_uno_bits[chosen_num:], 2)

        # print("After cross[\nind_uno = {},\nind_dos = {}\n]".format(to_binary_length(temp_ind_uno.id, temp_ind_uno.ind_len), to_binary_length(temp_ind_dos.id, temp_ind_uno.ind_len)))

        temp_ind_uno.score = 0
        temp_ind_dos.score = 0

        return Individual(overwrite=temp_ind_uno), Individual(overwrite=temp_ind_dos)
        
    def crossover(self):
        self.best_individual = Individual(overwrite = max(self.list_of_ind))

        crossovered_ind_list = []

        self.temp_strategies =  copy.deepcopy(self.list_of_ind)
        
        self.parent_strategies = []

        for ind in self.list_of_ind:
            x = random.random()
            chosen_randoms.append(x)
            if x > self.crossover_prob:
                # print("crossover x = {}, ind_id = {}".format(x, ind.id))
                self.list_of_ind.remove(ind)
                self.parent_strategies.append(0)
            else:
                self.parent_strategies.append(1)

        # self.parent_strategies = copy.deepcopy(self.list_of_ind)
        
        for i in range(0, len(self.list_of_ind), 2):
            ind_uno, ind_dos = None, None

            if i < len(self.list_of_ind) - 1:
                ind_uno, ind_dos = self.cross_two_inds(self.list_of_ind[i], self.list_of_ind[i+1])
            else:
                ind_uno = self.cross_two_inds(self.list_of_ind[i], self.list_of_ind[0])[0]

            if ind_uno:
                crossovered_ind_list.append(Individual(overwrite = ind_uno))
            if ind_dos:
                crossovered_ind_list.append(Individual(overwrite = ind_dos))

        while len(crossovered_ind_list) != self.pop_size:
            chosen_ind_uno, chosen_ind_dos = random.choices(list(self.list_of_ind), k = 2)

            ind_uno, ind_dos= self.cross_two_inds(chosen_ind_uno, chosen_ind_dos)

            if ind_uno:
                crossovered_ind_list.append(Individual(overwrite = ind_uno))
            if ind_dos and len(crossovered_ind_list) != self.pop_size:
                crossovered_ind_list.append(Individual(overwrite = ind_dos))

        self.list_of_ind = crossovered_ind_list
        self.child_strategies = copy.deepcopy(self.list_of_ind)

    def mutate_individuals(self):
        for ind in self.list_of_ind:
            ind.mutation(self.mutation_prob)
        # print('\n')

        for index, ind in enumerate(self.temp_strategies):
            self.temp_strategies[index] = ind.to_binary_for_this_old_fuck()

        for index, ind in enumerate(self.child_strategies):
            self.child_strategies[index] = ind.to_binary_for_this_old_fuck()

        temp_list_of_ind = []
        for ind in self.list_of_ind:
            temp_list_of_ind.append(ind.to_binary_for_this_old_fuck())

        if debug:
            print_31(self.temp_strategies, self.parent_strategies, self.child_strategies, temp_list_of_ind)

    def do_elitist(self):
        self.hard_tournament()
        worst_individual = min(self.list_of_ind)
        self.list_of_ind.remove(worst_individual)
        self.list_of_ind.append(Individual(overwrite=self.best_individual))


class GameWorker(QObject):
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
    elitist_strategy = False

    input_strategies = []
    input_prehistory = ''
    input_num_of_runs = 0
    num_of_runs_left = 0

    history_count = []

    finished = pyqtSignal(pd.DataFrame, list, list, list)

    def __init__(self, is_2_PD, N, two_pd_payoff_func, prob_of_init_C, num_of_tournaments, num_of_opponents, prehistory_L, pop_size, num_of_gener, tournament_size, crossover_prob, mutation_prob, elitist_strategy, seed, deb, freq_gen_start, delta_freq, canvas_uno, canvas_dos, strategies, prehistory, num_of_runs, num_of_runs_left):
        super(GameWorker, self).__init__()

        if is_2_PD:
            self.is_2_PD = is_2_PD
            self.N = 2
        else:
            self.N = N

        self.two_pd_payoff_func = two_pd_payoff_func
        self.prob_of_init_C = prob_of_init_C
        self.num_of_tournaments = num_of_tournaments
        self.num_of_opponents = num_of_opponents
        self.prehistory_L = prehistory_L
        self.pop_size = pop_size
        self.num_of_gener = num_of_gener
        self.tournament_size = tournament_size
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        global debug 
        debug = deb
        self.elitist_strategy = elitist_strategy
        self.freq_gen_start = freq_gen_start
        self.delta_freq = delta_freq
        self.canvas_uno = canvas_uno
        self.canvas_dos = canvas_dos
        
        self.input_strategies = strategies
        self.input_prehistory = prehistory
        self.input_num_of_runs = num_of_runs
        self.num_of_runs_left = num_of_runs_left

        if seed:
            random.seed(seed)

        if debug:
            create_results_dir()
            with open("RESULTS/DEBUG.txt", 'w') as f:
                pass


    def run(self):
        list_of_ind = []
        avg_data_per_generation = pd.DataFrame(columns=['Avg per Gen', 'Avg per Best'])
        history_count_per_gen = pd.DataFrame()
        whole_history_count = []
        best_individual_ids = []
        global chosen_randoms
        chosen_randoms = []
        global cross_bits
        cross_bits = []
        global mutation_bits
        mutation_bits = []
        global global_num_of_C_N
        global_num_of_C_N = []

        for gen in range(1, self.num_of_gener + 1):
            # print('Generation {}'.format(gen-1))
            global_num_of_C_N.append([0,0])

            if self.input_strategies and self.input_prehistory:
                if not self.is_2_PD and not list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, input_strategies = self.input_strategies, input_prehistory = self.input_prehistory)
                elif self.is_2_PD and not list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, self.two_pd_payoff_func, input_strategies = self.input_strategies, input_prehistory = self.input_prehistory)
                elif not self.is_2_PD and list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, list_of_ind=list_of_ind, input_strategies = self.input_strategies, input_prehistory = self.input_prehistory)
                else:

                    a = ''
                    for _ in range(0, self.prehistory_L*self.N):
                        
                        x = random.random()
                        if x < 0.5:
                            a +='0'
                        else:
                            a +='1'

                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, self.two_pd_payoff_func, list_of_ind, input_strategies = self.input_strategies, input_prehistory = a)
            
                if not list_of_ind:
                    if self.N == 2 and debug:
                        print_11(curr_generation.list_of_ind, self.input_prehistory)

                    elif debug:
                        print_21(curr_generation.list_of_ind, self.input_prehistory)

            else:
                if not self.is_2_PD and not list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob)
                elif self.is_2_PD and not list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, self.two_pd_payoff_func)
                elif not self.is_2_PD and list_of_ind:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, list_of_ind=list_of_ind)
                else:
                    curr_generation = Generation(self.pop_size, self.num_of_tournaments, self.tournament_size, self.crossover_prob, self.prob_of_init_C, self.N, self.prehistory_L, self.mutation_prob, self.two_pd_payoff_func, list_of_ind)

            # for ind in curr_generation.list_of_ind:
            #     print('ind = {}'.format(to_binary_length(ind.id, ind.ind_len)))

            curr_generation.fight_for_death_u_knobs(self.num_of_opponents)

            if debug and self.N==2 and len(curr_generation.list_of_ind)==2:
                break

            sum_of_avg_score_for_gen = 0
            # Count avg scores and all collective oponentes_jodidos
            for ind in curr_generation.list_of_ind:
                ind.score = ind.score/(ind.oponentes_jodidos * self.num_of_tournaments)
                sum_of_avg_score_for_gen += ind.score

            curr_generation.hard_tournament()

            self.history_count = curr_generation.history_count
            h_c_sum = sum(self.history_count)
            for id, h_c in enumerate(self.history_count):
                self.history_count[id] = h_c / h_c_sum
            whole_history_count.append(self.history_count)
            
            curr_generation.crossover()

            best_individual_ids.append(curr_generation.best_individual)


            # UPDATE UPPER PLOT :)
            avg_data_per_generation.loc[len(avg_data_per_generation) + 1] = [(sum_of_avg_score_for_gen/self.pop_size), (curr_generation.best_individual.score)]

            self.canvas_uno.axes.clear()
            self.canvas_uno.fig.set_tight_layout(True)
            self.canvas_uno.axes.set_xlabel('Generations', fontsize=10)
            self.canvas_uno.axes.set_title('Average total payoff', fontsize=14)
            avg_data_per_generation.plot(ax=self.canvas_uno.axes)
            self.canvas_uno.draw()


            # UPDATE LOWER PLOT :)
            if gen == self.freq_gen_start or (gen > self.freq_gen_start and (((gen - self.freq_gen_start) % self.delta_freq) == 0)):
                history_count_per_gen["gen {}".format(gen)] = self.history_count
                # history_count_per_gen.loc[len(history_count_per_gen) + 1] = self.history_count

                self.canvas_dos.axes.clear()
                self.canvas_dos.fig.set_tight_layout(True)
                self.canvas_dos.axes.set_xlabel('Strategies', fontsize=10)
                self.canvas_dos.axes.set_title('Frequencies of applied strategies', fontsize=14)
                history_count_per_gen.plot(ax=self.canvas_dos.axes)
                self.canvas_dos.draw()

            curr_generation.mutate_individuals()

            if self.elitist_strategy:
                curr_generation.do_elitist()

            list_of_ind = curr_generation.list_of_ind

        # if self.input_num_of_runs > 1:
        #     temp_num = abs(self.num_of_runs_left - self.input_num_of_runs) + 1
            # save_plot_in_results(self.canvas_uno.fig, "Average_data_run_num_{}.jpg".format(temp_num))
            # save_plot_in_results(self.canvas_dos.fig, "Frequencies_run_num_{}.jpg".format(temp_num))

        # print("Random table: ", chosen_randoms)
        # print("Crossover bit: ", cross_bits)
        # print("Mutation bits: ", mutation_bits)
        self.finished.emit(avg_data_per_generation, whole_history_count, best_individual_ids, global_num_of_C_N)
