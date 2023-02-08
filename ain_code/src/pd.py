from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog, QFileDialog
from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QThread

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from matplotlib.figure import Figure

from ui.main_window import Ui_MainWindow
from ui.load_dialog import Ui_LoadDialog

from src.classes import GameWorker
from src.funcitons import create_results_1_single_run,\
                          create_results_2_single_run,\
                          create_results_2_30_single_run,\
                          create_results_3_single_run,\
                          create_m_result_1_multiple_run,\
                          create_std_result_1_multiple_run,\
                          create_result_1N_single_run,\
                          create_result_2N_single_run,\
                          create_result_2N_30_single_run,\
                          to_binary

import pandas as pd
import random
import sys
import os


matplotlib.use('Qt5Agg')

global_num_of_C_N = [0,0]


class LoadDialog(Ui_LoadDialog, QDialog):
    strategies = []
    prehistory = ''

    def __init__(self, parent):
        super(LoadDialog, self).__init__()

        self.setupUi(self)

        QDialog.setModal(self,True)

        self.strategies_path = ''
        self.prehistory_path = ''
        self.strategies = []
        self.prehistory = ''
        self.parent = parent

        # connect buttons
        self.choose_strategies_button.clicked.connect(self.choose_strategies)
        self.choose_prehistory_button.clicked.connect(self.choose_prehistory)
        self.run_button.clicked.connect(self.check_and_run)
        self.cancel_button.clicked.connect(self.reject)

        self.show()

    def choose_strategies(self):
        chosen_path = QFileDialog.getOpenFileName(self, "Choose STRATEGIES .txt file", '', "Text file (*.txt)")[0]

        if chosen_path != '':
            self.strategies_path = chosen_path
            self.strategies_textEdit.setPlainText(chosen_path)

    def choose_prehistory(self):
        chosen_path = QFileDialog.getOpenFileName(self, "Choose PREHISTORY .txt file", '', "Text file (*.txt)")[0]

        if chosen_path != '':
            self.prehistory_path = chosen_path
            self.prehistory_textEdit.setPlainText(chosen_path)

    def read_file(self, f_path):
        to_ret = []
        with open(f_path, 'r') as f:
            file_lines = f.read().splitlines()

            for line in file_lines:
                line = line.replace(' ', '')

                if line:
                    if line[0] == '#':
                        continue
                    to_ret.append(line)
        
        return to_ret

    def check_and_run(self):
        # create temporary variables
        N = 0
        L = self.parent.prehistory_l
        pop_size = self.parent.pop_size
        num_of_opponents = self.parent.num_of_opponents

        if self.parent.two_pd:
            N = 2
        else:
            N = self.parent.n_players

        ind_len = '1'
        ind_len += to_binary(N-1)       
        ind_len *= L       
        ind_len = int(ind_len, 2) + 1

        if self.strategies_path == '':
            QMessageBox.warning(self, 'ERROR', 'Archivo "Strategies" no seleccionado')
            
        elif self.prehistory_path == '':
            QMessageBox.warning(self, 'ERROR', 'Archivo "Prehistory" no seleccionado')

        elif not os.path.exists(self.strategies_path):
            QMessageBox.warning(self, 'ERROR', 'Archivo "Strategies" no encontrado')

        elif not os.path.exists(self.prehistory_path):
            QMessageBox.warning(self, 'ERROR', 'Archivo "Prehistory" no encontrado')

        else:
            self.strategies = self.read_file(self.strategies_path)
            self.prehistory = ''.join(self.read_file(self.prehistory_path))

            if len(self.strategies) < N:
                QMessageBox.warning(self, 'ERROR', 'No hay suficiente estrategia')

            elif len(self.prehistory) != (N * L):
                QMessageBox.warning(self, 'ERROR', 'Prehistoria de mala duración')

            elif len(self.strategies[0]) < ind_len:
                QMessageBox.warning(self, 'ERROR', 'Estrategia de longitud incorrecta')

            elif len(self.strategies) != pop_size:
                QMessageBox.warning(self, 'ERROR', 'Una población demasiado pequeña')

            # elif len(self.strategies) < num_of_opponents:
            #     QMessageBox.warning(self, 'ERROR', 'Demasiados "num_of_opponents"')

            else:
                self.accept()


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)


class PDWindow(Ui_MainWindow, QMainWindow):
    # Pd game params
    two_pd = False
    n_pd = False
    n_players = 0
    two_pd_payoff_func = dict(cc_uno = 0, cc_dos = 0, cd_uno = 0, cd_dos = 0, dc_uno = 0, dc_dos = 0, dd_uno = 0, dd_dos = 0)
    prob_of_init_c = 0
    num_of_tournaments = 0
    num_of_opponents = 0
    prehistory_l = 0

    # GA params
    pop_size = 0
    num_of_gener = 0
    tournament_size = 0
    crossover_prob = 0
    mutation_prob = 0
    elitist_strategy = False

    # Other params
    seed = 0
    num_of_runs = 0
    debug = False

    # loaded
    strategies = []
    prehistory = ''

    def __init__(self):
        super(PDWindow, self). __init__()

        self.setupUi(self)

        # set seed input validator
        self.seed_line.setValidator(QRegExpValidator(QRegExp(r'\d+')))

        # connect buttons
        self.run_button.clicked.connect(self.run)

        # create canvas_uno
        self.canvas_uno = MplCanvas(self)
        self.canvas_uno.fig.set_tight_layout(True)
        self.canvas_uno.axes.set_xlabel('Generations', fontsize=10)
        self.canvas_uno.axes.set_title('Average total payoff', fontsize=14)

        # create canvas_dos
        self.canvas_dos = MplCanvas(self)
        self.canvas_dos.fig.set_tight_layout(True)
        self.canvas_dos.axes.set_xlabel('Strategies', fontsize=10)
        self.canvas_dos.axes.set_title('Frequencies of applied strategies', fontsize=14)

        # set loaded data
        self.strategies = []
        self.prehistory = ''

        layout = QVBoxLayout()
        layout.addWidget(self.canvas_uno)
        self.avg_frame.setLayout(layout)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas_dos)
        self.freq_frame.setLayout(layout)

        self.show()

    def data_loaded(self):
        self.load_dialog = LoadDialog(self)
        load_accepted = self.load_dialog.exec_()
        if load_accepted:
            return True
        return False

    def set_seed_conditionally(self):
        if self.seed_line.text() == '':
            self.seed = random.randint(0, sys.maxsize)
        else:
            self.seed = float(self.seed_line.text())

    def set_attributes(self):
        # Pd game params
        self.two_pd = self.two_pd_radioButton.isChecked()
        self.n_pd = self.n_pd_radioButton.isChecked()
        self.n_players = self.n_spinBox.value()
        self.prob_of_init_c = self.prob_of_init_c_spinBox.value()
        self.num_of_tournaments = self.num_of_tournaments_spinBox.value()
        self.num_of_opponents = self.num_of_opponents_spinBox.value()
        self.prehistory_l = self.prehistory_l_spinBox.value()

        self.two_pd_payoff_func['cc_uno'] = self.cc_uno_spinBox.value()
        self.two_pd_payoff_func['cc_dos'] = self.cc_dos_spinBox.value()
        self.two_pd_payoff_func['cd_uno'] = self.cd_uno_spinBox.value()
        self.two_pd_payoff_func['cd_dos'] = self.cd_dos_spinBox.value()
        self.two_pd_payoff_func['dc_uno'] = self.dc_uno_spinBox.value()
        self.two_pd_payoff_func['dc_dos'] = self.dc_dos_spinBox.value()
        self.two_pd_payoff_func['dd_uno'] = self.dd_uno_spinBox.value()
        self.two_pd_payoff_func['dd_dos'] = self.dd_dos_spinBox.value()

        # GA params
        self.pop_size = self.pop_size_spinBox.value()
        self.num_of_gener = self.num_of_gener_spinBox.value()
        self.tournament_size = self.tournament_size_spinBox.value()
        self.crossover_prob = self.crossover_prob_spinBox.value()
        self.mutation_prob = self.mutation_prob_spinBox.value()
        self.elitist_strategy = self.elitist_strategy_checkBox.isChecked()

        # Other params
        self.num_of_runs = self.num_of_runs_spinBox.value()
        self.debug = self.debug_checkBox.isChecked()
        self.freq_gen_start = self.freq_gen_start_spinBox.value()
        self.delta_freq = self.delta_freq_spinBox.value()

        # Additional structures
        self.multiple_run_data_storage = []

    def input_valid(self):
        # cd_uno/dc_dos < dd_uno/dd_dos < cc_uno/cc_dos < dc_uno/cd_uno

        cc_uno, cc_dos = (self.cc_uno_spinBox.value(), self.cc_dos_spinBox.value())
        cd_uno, cd_dos = (self.cd_uno_spinBox.value(), self.cd_dos_spinBox.value())
        dc_uno, dc_dos = (self.dc_uno_spinBox.value(), self.dc_dos_spinBox.value())
        dd_uno, dd_dos = (self.dd_uno_spinBox.value(), self.dd_dos_spinBox.value())

        if self.two_pd:
            if not dc_uno > cc_uno or not dc_uno > cc_dos or\
               not cd_dos > cc_uno or not cd_dos > cc_dos or\
               not cc_uno > dd_uno or not cc_uno > dd_dos or\
               not cc_dos > dd_uno or not cc_dos > dd_dos or\
               not dd_uno > cd_uno or not dd_uno > dc_dos or\
               not dd_dos > cd_uno or not dd_dos > dc_dos:

                QMessageBox.warning(self, 'Input ERROR', 'Data in 2p PD payoff function has to look like:\n\nCD_left/DC_right < DD_left/DD_right < CC_left/CC_right < DC_left/CD_left')
                return False

        # if self.num_of_opponents >= self.pop_size:
        #     QMessageBox.warning(self, 'Input ERROR', 'Number of opponents cannot be greater nor equal to size of population')
        #     return False

        if self.num_of_gener < self.freq_gen_start:
            QMessageBox.warning(self, 'Input ERROR', 'Number of generations must be greater or equal to frequency gen start')
            return False

        if self.pop_size < self.tournament_size:
            QMessageBox.warning(self, 'Input ERROR', 'Size of population must be greater or equal to tournament size')
            return False

        if not self.two_pd and self.pop_size < self.n_players:
            QMessageBox.warning(self, 'Input ERROR', 'Size of population must be greater or equal to players count')
            return False

        return True

    def manage_created_output_files(self, avg_data_per_generation, whole_history_count, best_individual_ids):

        if self.two_pd and self.num_of_runs_spinBox.value() == 1:
            create_results_1_single_run(self, 'result_1', avg_data_per_generation)
            create_results_2_single_run(self, 'result_2', whole_history_count)
            create_results_2_30_single_run(self, 'result_2_', whole_history_count)
            create_results_3_single_run(self, 'result_3', best_individual_ids)

        elif self.two_pd and self.num_of_runs_spinBox.value() > 1:
            create_m_result_1_multiple_run(self, 'm_result_1', self.multiple_run_data_storage)
            create_std_result_1_multiple_run(self, 'std_result_1', self.multiple_run_data_storage)

        elif not self.two_pd and self.num_of_runs_spinBox.value() == 1:
            create_result_1N_single_run(self, 'result_1N', avg_data_per_generation, global_num_of_C_N, self.n_players)
            create_result_2N_single_run(self, 'result_2N', whole_history_count)
            create_result_2N_30_single_run(self, 'result_2N_', whole_history_count)

    def thread_finished(self, avg_data_per_generation: pd.DataFrame, whole_history_count: list, best_individual_ids: list, num_of_C_N: list):
        global global_num_of_C_N
        global_num_of_C_N = num_of_C_N
        self.num_of_runs -= 1
        self.multiple_run_data_storage.append(avg_data_per_generation)

        if self.num_of_runs:
            # del avg_data_per_generation
            # del whole_history_count
            # del best_individual_ids
            self.run()
        else:
            # Unlock app
            if not (self.debug and self.two_pd and len(self.strategies)==2):
                self.manage_created_output_files(avg_data_per_generation, whole_history_count, best_individual_ids)

            self.run_button.setEnabled(True)
            self.num_of_runs_spinBox.setEnabled(True)
            self.strategies = []
            self.prehistory = ''
            # del avg_data_per_generation
            # del whole_history_count
            # del best_individual_ids
                
    def run(self):

        self.canvas_uno.axes.clear()
        self.canvas_dos.axes.clear()

        self.canvas_uno.fig.set_tight_layout(True)
        self.canvas_uno.axes.set_xlabel('Generations', fontsize=10)
        self.canvas_uno.axes.set_title('Average total payoff', fontsize=14)

        self.canvas_dos.fig.set_tight_layout(True)
        self.canvas_dos.axes.set_xlabel('Strategies', fontsize=10)
        self.canvas_dos.axes.set_title('Frequencies of applied strategies', fontsize=14)
        self.canvas_uno.draw()
        self.canvas_dos.draw()

        if self.run_button.isEnabled():
            self.set_attributes()

        if self.input_valid():

            if self.load_checkBox.isChecked() and (not self.strategies or not self.prehistory):
                if self.data_loaded():
                    self.strategies = self.load_dialog.strategies
                    self.prehistory = self.load_dialog.prehistory
                    self.run()

            else:

                # Lock app
                self.run_button.setDisabled(True)
                self.num_of_runs_spinBox.setDisabled(True)

                self.set_seed_conditionally()
                    
                self.thread = QThread()
                self.worker = GameWorker(self.two_pd, 
                                        self.n_players, 
                                        self.two_pd_payoff_func, 
                                        self.prob_of_init_c, 
                                        self.num_of_tournaments, 
                                        self.num_of_opponents,
                                        self.prehistory_l,
                                        self.pop_size,
                                        self.num_of_gener,
                                        self.tournament_size,
                                        self.crossover_prob,
                                        self.mutation_prob,
                                        self.elitist_strategy,
                                        self.seed,
                                        self.debug,
                                        self.freq_gen_start,
                                        self.delta_freq,
                                        self.canvas_uno,
                                        self.canvas_dos,
                                        self.strategies,
                                        self.prehistory,
                                        self.num_of_runs_spinBox.value(),
                                        self.num_of_runs)
                
                self.worker.moveToThread(self.thread)

                self.thread.started.connect(self.worker.run)
                self.worker.finished.connect(self.thread.quit)
                self.worker.finished.connect(self.worker.deleteLater)
                self.worker.finished.connect(self.thread_finished)
                self.thread.finished.connect(self.thread.deleteLater)

                self.thread.start()
