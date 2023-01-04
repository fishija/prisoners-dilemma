from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QRegExp

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QThread

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from matplotlib.figure import Figure

from ui.main_window import Ui_MainWindow

from src.classes import GameWorker

import pandas as pd
import random
import sys


matplotlib.use('Qt5Agg')


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

    def __init__(self):
        super(PDWindow, self). __init__()

        self.setupUi(self)

        # set seed input validator
        self.seed_line.setValidator(QRegExpValidator(QRegExp(r'\d+')))

        # connect run button
        self.run_button.clicked.connect(self.run)

        # create canvas_uno
        self.canvas_uno = MplCanvas(self)
        self.canvas_uno.fig.set_tight_layout(True)
        self.canvas_uno.axes.set_xlabel('Generations', fontsize=10)
        self.canvas_uno.axes.set_ylabel('Avg. score', fontsize=10)
        self.canvas_uno.axes.set_title('Average total payoff', fontsize=14)

        # create canvas_dos
        self.canvas_dos = MplCanvas(self)
        self.canvas_dos.fig.set_tight_layout(True)
        self.canvas_dos.axes.set_xlabel('Strategies', fontsize=10)
        self.canvas_dos.axes.set_ylabel('Frequency', fontsize=10)
        self.canvas_dos.axes.set_title('Frequencies of applied strategies', fontsize=14)


        layout = QVBoxLayout()
        layout.addWidget(self.canvas_uno)
        self.avg_frame.setLayout(layout)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas_dos)
        self.freq_frame.setLayout(layout)

        self.show()

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
        # self.two_pd_payoff_func['cc_dos'] = self.cc_dos_spinBox.value()
        self.two_pd_payoff_func['cd_uno'] = self.cd_uno_spinBox.value()
        # self.two_pd_payoff_func['cd_dos'] = self.cd_dos_spinBox.value()
        self.two_pd_payoff_func['dc_uno'] = self.dc_uno_spinBox.value()
        # self.two_pd_payoff_func['dc_dos'] = self.dc_dos_spinBox.value()
        self.two_pd_payoff_func['dd_uno'] = self.dd_uno_spinBox.value()
        # self.two_pd_payoff_func['dd_dos'] = self.dd_dos_spinBox.value()

        # GA params
        self.pop_size = self.pop_size_spinBox.value()
        self.num_of_gener = self.num_of_gener_spinBox.value()
        self.tournament_size = self.tournament_size_spinBox.value()
        self.crossover_prob = self.crossover_prob_spinBox.value()
        self.mutation_prob = self.mutation_prob_spinBox.value()
        self.elitist_strategy_checkBox.isChecked()

        # Other params
        if self.seed_line.text() == '':
            self.seed = random.randint(0, sys.maxsize)
        else:
            self.seed = float(self.seed_line.text())

        self.num_of_runs = self.num_of_runs_spinBox.value()
        self.debug = self.debug_checkBox.isChecked()
        self.freq_gen_start = self.freq_gen_start_spinBox.value()
        self.delta_freq = self.delta_freq_spinBox.value()

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

        if self.num_of_opponents > self.pop_size:
            QMessageBox.warning(self, 'Input ERROR', 'Number of opponents cannot be greater than size of population')
            return False

        if self.num_of_gener < self.freq_gen_start:
            QMessageBox.warning(self, 'Input ERROR', 'Number of generations must be greater or equal to frequency gen start')
            return False

        if self.pop_size < self.tournament_size:
            QMessageBox.warning(self, 'Input ERROR', 'Size of population must be greater or equal to tournament size')
            return False

        return True

    def thread_finished(self):
        self.num_of_runs -= 1

        if self.num_of_runs:
            self.run()
        else:
            # Unlock app
            self.run_button.setEnabled(True)
                
    def run(self):

        self.canvas_uno.axes.clear()
        self.canvas_dos.axes.clear()

        self.canvas_uno.fig.set_tight_layout(True)
        self.canvas_uno.axes.set_xlabel('Generations', fontsize=10)
        self.canvas_uno.axes.set_ylabel('Avg. score', fontsize=10)
        self.canvas_uno.axes.set_title('Average total payoff', fontsize=14)

        self.canvas_dos.fig.set_tight_layout(True)
        self.canvas_dos.axes.set_xlabel('Strategies', fontsize=10)
        self.canvas_dos.axes.set_ylabel('Frequency', fontsize=10)
        self.canvas_dos.axes.set_title('Frequencies of applied strategies', fontsize=14)
        self.canvas_uno.draw()
        self.canvas_dos.draw()

        if self.run_button.isEnabled():
            self.set_attributes()

        if self.input_valid():

            # Lock app
            self.run_button.setDisabled(True)
                
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
                                    self.canvas_dos)
            
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(self.thread_finished)

            self.thread.start()
