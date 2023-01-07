import pandas as pd
import numpy as np
import os


def to_binary(i):
    return bin(i)[2:]


def to_binary_length(i, l):
    temp = bin(i)[2:]
    return temp.zfill(l)


def create_results_dir():
    if not os.path.exists("RESULTS"):
        os.makedirs("RESULTS")

    
def write_window_data(PDWindow):
    to_ret = ''

    if PDWindow.two_pd:
        to_ret += '# 2pPd\n'
        to_ret += '# CC [{} | {}]\n'.format(PDWindow.two_pd_payoff_func['cc_uno'], PDWindow.two_pd_payoff_func['cc_dos'])
        to_ret += '# CD [{} | {}]\n'.format(PDWindow.two_pd_payoff_func['cd_uno'], PDWindow.two_pd_payoff_func['cd_dos'])
        to_ret += '# DC [{} | {}]\n'.format(PDWindow.two_pd_payoff_func['dc_uno'], PDWindow.two_pd_payoff_func['dc_dos'])
        to_ret += '# DD [{} | {}]\n'.format(PDWindow.two_pd_payoff_func['dd_uno'], PDWindow.two_pd_payoff_func['dd_uno'])
    else:
        to_ret += '# NpPd\n'
        to_ret += '# n = {}\n'.format(PDWindow.n_players)

    to_ret += '# prob_of_init_c = {}\n'.format(PDWindow.prob_of_init_c)
    to_ret += '# num_of_opponents = {}\n'.format(PDWindow.num_of_opponents)
    to_ret += '# prehistory_l = {}\n'.format(PDWindow.prehistory_l)
    to_ret += '# pop_size = {}\n'.format(PDWindow.pop_size)
    to_ret += '# num_of_gener = {}\n'.format(PDWindow.num_of_gener)
    to_ret += '# tournament_size = {}\n'.format(PDWindow.tournament_size)
    to_ret += '# crossover_prob = {}\n'.format(PDWindow.crossover_prob)
    to_ret += '# mutation_prob = {}\n'.format(PDWindow.mutation_prob)
    to_ret += '# elitist_strategy = {}\n'.format(PDWindow.elitist_strategy)
    to_ret += '# seed = {}\n'.format(PDWindow.seed)
    to_ret += '# num_of_runs = {}\n'.format(PDWindow.num_of_runs)
    to_ret += '# freq_gen_start = {}\n'.format(PDWindow.freq_gen_start)
    to_ret += '# delta_freq = {}\n'.format(PDWindow.delta_freq)

    return to_ret


def create_results_1_single_run(PDWindow, filename, df):
    filename = filename + '.txt'

    create_results_dir()
    df.rename(columns = {'Avg per Best': 'best_fit', 'Avg per Gen': 'avg_fit'}, inplace = True)

    with open(os.path.join("RESULTS", filename), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        to_write += '#\n# 1 2 3\n'

        to_write += '# gen best_fit avg_fit\n'

        for index, row in df.iterrows():
            to_write += "{} {} {}\n".format(index-1, row['best_fit'], row['avg_fit'])

        out_f.write(to_write)


def create_results_2_single_run(PDWindow, filename, whole_game_histories):
    filename = filename + '.txt'

    create_results_dir()

    with open(os.path.join("RESULTS", filename), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        to_write += '#\n# frequency of game histories\n#'

        for i in range(1, len(whole_game_histories[0]) + 2):
            to_write += ' {}'.format(i)

        to_write += '\n# gen'

        for i in range(len(whole_game_histories[0])):
            to_write += ' {}'.format(i)

        to_write += '\n'

        for index, gen_histories in enumerate(whole_game_histories):
            to_write += '{}'.format(index)

            for history in gen_histories:
                to_write += ' {}'.format(history)

            to_write += '\n'
        
        out_f.write(to_write)


def create_results_2_30_single_run(PDWindow, filename, whole_game_histories):
    create_results_dir()

    for gen_num in range(PDWindow.freq_gen_start - 1, len(whole_game_histories), PDWindow.delta_freq):
        out_filename = filename + '{}.txt'.format(gen_num + 1)
        
        with open(os.path.join("RESULTS", out_filename), 'w') as out_f:
            to_write = ''
            to_write += write_window_data(PDWindow)

            to_write += '#\n# 1 2\n'

            to_write += '# history freq_of_game_histories\n'

            for index, val in enumerate(whole_game_histories[gen_num]):
                to_write += '{} {}\n'.format(index, val)

            out_f.write(to_write)


def create_results_3_single_run(PDWindow, filename, best_individual_ids):
    filename = filename + '.txt'
    create_results_dir()

    n = 0
    l = PDWindow.prehistory_l
    if PDWindow.two_pd:
        n = 2
    else:
        n = PDWindow.n_players

    ind_len = '1'
    ind_len += to_binary(n-1)
    ind_len *= l
    ind_len = int(ind_len, 2) + 1

    for i in range(len(best_individual_ids)):
        best_individual_ids[i] = to_binary_length(best_individual_ids[i], ind_len)

    with open(os.path.join("RESULTS", filename), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        to_write += '#\n# best strategy\n#'

        for i in range(1, len(best_individual_ids[0]) + 1):
            to_write += ' {}'.format(i)

        to_write += '\n# gen'

        for i in range(len(best_individual_ids[0])):
            to_write += ' {}'.format(i)

        to_write += '\n'

        for index, id in enumerate(best_individual_ids):
            to_write += '{}'.format(index)
            for bin_number in id:
                to_write += ' {}'.format(bin_number)

            to_write += '\n'

        out_f.write(to_write)


def create_m_result_1_multiple_run(PDWindow, filename, list_of_dfs):
    filename = filename + '.txt'
    create_results_dir()

    for df in list_of_dfs:
        df.rename(columns = {'Avg per Best': 'best_fit', 'Avg per Gen': 'avg_fit'}, inplace=True)

    with open(os.path.join("RESULTS", filename), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        for index, df in enumerate(list_of_dfs):

            to_write += '#\n# Exper {}\n'.format(index + 1)

            to_write += '# 1 2 3\n'

            to_write += '# gen best_fit avg_fit\n'

            for index, row in df.iterrows():
                to_write += "{} {} {}\n".format(index-1, row['best_fit'], row['avg_fit'])

        out_f.write(to_write)


def create_std_result_1_multiple_run(PDWindow, filename, list_of_dfs):
    filename = filename + '.txt'
    create_results_dir()

    for index, df in enumerate(list_of_dfs):
        df.drop('avg_fit', axis=1, inplace=True)
        df.rename(columns = {'best_fit':'{}'.format(index)}, inplace=True)
        list_of_dfs[index] = df.T

    temp_df = pd.concat(list_of_dfs, axis = 0)

    df_ready = pd.DataFrame()

    df_ready['avg_best'] = temp_df.mean()
    df_ready['std_best'] = np.std(temp_df)

    with open(os.path.join("RESULTS", "std_result_1.txt"), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        to_write += '#\n# 1 2 3\n'

        to_write += '# gen avg_best std_best\n'

        for index, row in df_ready.iterrows():
            to_write += "{} {} {}\n".format(index-1, row['avg_best'], row['std_best'])

        out_f.write(to_write)


def create_result_1N_single_run(PDWindow, filename, df):
    filename = filename + '.txt'
    create_results_dir()
    create_results_1_single_run(PDWindow, filename, df)


def create_result_2N_single_run(PDWindow, filename, whole_game_histories):
    filename = filename + '.txt'
    create_results_dir()
    histories_count = len(whole_game_histories[0])

    print(histories_count)

    with open(os.path.join("RESULTS", filename), 'w') as out_f:
        to_write = ''
        to_write += write_window_data(PDWindow)

        to_write += '#\n# 10 best frequencies\n#'

        for i in range(1, 22):
            to_write += ' {}'.format(i)

        to_write += '\n# gen'

        for i in range(0,10):
            to_write += ' history_id freq'

        to_write += '\n'

        for index in range(PDWindow.freq_gen_start-1, len(whole_game_histories), PDWindow.delta_freq):
            to_write += '{}'.format(index)

            sorted_key_list = sorted(range(histories_count), key=lambda k: whole_game_histories[index][k])[0:10]

            for key in sorted_key_list:
                to_write += ' {} {}'.format(to_binary(key), whole_game_histories[index][key])

            to_write += '\n'

        out_f.write(to_write)


def create_result_2N_30_single_run(PDWindow, filename, whole_game_histories):
    create_results_dir()

    for index in range(PDWindow.freq_gen_start-1, len(whole_game_histories), PDWindow.delta_freq):
        temp_filename = "{}{}.txt".format(filename, index + 1)
        temp_history = whole_game_histories[index]

        with open(os.path.join("RESULTS", temp_filename), 'w') as out_f:
            to_write = ''
            to_write += write_window_data(PDWindow)

            to_write += '# 1 2\n'

            to_write += '# history freq_of_history'

            for index, frequency in enumerate(temp_history):
                to_write += '\n{} {}'.format(index,frequency)

            to_write += '\n'

            out_f.write(to_write)
